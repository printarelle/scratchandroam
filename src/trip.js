// Private Trip Hub for Natali, at /trip/ (PIN protected, never indexed).
// The phone only talks to scratchandroam.com. This Worker passes files on to Dropbox,
// into the day folders the nightly Claude task reads, and reads Claude's notes back.
//
// Secrets (Cloudflare dashboard > Workers > scratchandroam > Settings > Variables and Secrets):
//   TRIP_PIN               the PIN she types (8 digits or more)
//   DROPBOX_APP_KEY        from her Dropbox app
//   DROPBOX_APP_SECRET     from her Dropbox app
//   DROPBOX_REFRESH_TOKEN  shown once by /trip/connect/ after she approves the app
// Optional: DROPBOX_ROOT_NS (team folder namespace, default below).
import HUB from "./trip-hub.html";

const ROOT_NS = "732279378"; // "DexPixel Ltd" team folder
const TRIP = "/Scratch and Roam/01_RAW/China/2026-12 December Trip";
const DAYS = [
  ["01", "2026-12-06", "Chengdu arrival"], ["02", "2026-12-07", "Chengdu"], ["03", "2026-12-08", "Chengdu"],
  ["04", "2026-12-09", "Chongqing"], ["05", "2026-12-10", "Chongqing"], ["06", "2026-12-11", "Chongqing"],
  ["07", "2026-12-12", "Chongqing drone show"], ["08", "2026-12-13", "Chongqing"], ["09", "2026-12-14", "Xian"],
  ["10", "2026-12-15", "Xian"], ["11", "2026-12-16", "Xian"], ["12", "2026-12-17", "Xian"],
  ["13", "2026-12-18", "Xian to Chengdu"], ["14", "2026-12-19", "Chengdu"], ["15", "2026-12-20", "Chengdu"],
  ["16", "2026-12-21", "Chengdu"], ["17", "2026-12-22", "Chengdu"], ["18", "2026-12-23", "Chengdu"],
  ["19", "2026-12-24", "Chengdu Christmas Eve"], ["20", "2026-12-25", "Chengdu Christmas Day"], ["21", "2026-12-26", "Chengdu"],
  ["22", "2026-12-27", "Chengdu"], ["23", "2026-12-28", "Chengdu"], ["24", "2026-12-29", "Flight home"],
];
const MON = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
function folderOf(d) {
  const [n, iso, label] = d;
  const [, m, dd] = iso.split("-");
  return `${TRIP}/Day ${n} - ${dd} ${MON[+m - 1]} - ${label}`;
}
const dayByNum = n => DAYS.find(d => d[0] === n);

const NOINDEX = { "X-Robots-Tag": "noindex, nofollow, noarchive", "Cache-Control": "private, no-store" };
const json = (o, s = 200) => new Response(JSON.stringify(o), { status: s, headers: { "Content-Type": "application/json", ...NOINDEX } });
const enc = new TextEncoder();

// ---------- session cookie ----------
async function hmac(env, msg) {
  const key = await crypto.subtle.importKey("raw", enc.encode("trip:" + env.TRIP_PIN + ":" + (env.DROPBOX_APP_SECRET || "")),
    { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const sig = await crypto.subtle.sign("HMAC", key, enc.encode(msg));
  return btoa(String.fromCharCode(...new Uint8Array(sig))).replace(/[+/=]/g, c => ({ "+": "-", "/": "_", "=": "" }[c]));
}
function safeEq(a, b) {
  if (typeof a !== "string" || typeof b !== "string" || a.length !== b.length) return false;
  let r = 0; for (let i = 0; i < a.length; i++) r |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return r === 0;
}
async function authed(req, env) {
  if (!env.TRIP_PIN) return false;
  const c = (req.headers.get("Cookie") || "").match(/(?:^|;\s*)trip=([^;]+)/);
  if (!c) return false;
  const [exp, sig] = decodeURIComponent(c[1]).split(".");
  if (!exp || !sig || Date.now() > +exp) return false;
  return safeEq(sig, await hmac(env, exp));
}
async function login(req, env) {
  if (!env.TRIP_PIN) return json({ error: "The Hub PIN is not set up yet." }, 503);
  let pin = "";
  try { pin = String((await req.json()).pin || ""); } catch {}
  if (!safeEq(pin, String(env.TRIP_PIN))) {
    await new Promise(r => setTimeout(r, 1500)); // slows down guessing
    return json({ error: "Wrong PIN" }, 401);
  }
  const exp = String(Date.now() + 45 * 86400e3);
  const v = encodeURIComponent(exp + "." + await hmac(env, exp));
  return new Response(JSON.stringify({ ok: true }), { headers: { "Content-Type": "application/json", ...NOINDEX,
    "Set-Cookie": `trip=${v}; Path=/trip/; Max-Age=${45 * 86400}; HttpOnly; Secure; SameSite=Strict` } });
}

// ---------- Dropbox ----------
let tok = { v: "", exp: 0 };
async function token(env) {
  if (tok.v && Date.now() < tok.exp) return tok.v;
  if (!env.DROPBOX_REFRESH_TOKEN) throw new Error("Dropbox is not connected yet (open /trip/connect/).");
  const r = await fetch("https://api.dropboxapi.com/oauth2/token", { method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({ grant_type: "refresh_token", refresh_token: env.DROPBOX_REFRESH_TOKEN,
      client_id: env.DROPBOX_APP_KEY, client_secret: env.DROPBOX_APP_SECRET }) });
  const j = await r.json();
  if (!j.access_token) throw new Error("Dropbox sign-in failed: " + (j.error_description || j.error || r.status));
  tok = { v: j.access_token, exp: Date.now() + (j.expires_in - 300) * 1000 };
  return tok.v;
}
// Dropbox-API-Arg must be ASCII: escape everything else.
const argHeader = o => JSON.stringify(o).replace(/[\u007f-￿]/g, c => "\\u" + c.charCodeAt(0).toString(16).padStart(4, "0"));
function rootHeader(env) {
  return JSON.stringify({ ".tag": "namespace_id", namespace_id: env.DROPBOX_ROOT_NS || ROOT_NS });
}
async function rpc(env, path, body) {
  const r = await fetch("https://api.dropboxapi.com/2/" + path, { method: "POST", headers: {
    Authorization: "Bearer " + await token(env), "Content-Type": "application/json", "Dropbox-API-Path-Root": rootHeader(env) },
    body: JSON.stringify(body) });
  const t = await r.text();
  let j; try { j = JSON.parse(t); } catch { j = { error_summary: t }; }
  if (!r.ok) { const e = new Error(j.error_summary || ("Dropbox error " + r.status)); e.dbx = j; throw e; }
  return j;
}
async function content(env, path, arg, body) {
  const r = await fetch("https://content.dropboxapi.com/2/" + path, { method: "POST", headers: {
    Authorization: "Bearer " + await token(env), "Content-Type": "application/octet-stream",
    "Dropbox-API-Arg": argHeader(arg), "Dropbox-API-Path-Root": rootHeader(env) }, body });
  return r;
}
async function contentJSON(env, path, arg, body) {
  const r = await content(env, path, arg, body);
  const t = await r.text();
  if (!r.ok) throw new Error("Dropbox upload error " + r.status + ": " + t.slice(0, 200));
  return t ? JSON.parse(t) : {};
}
async function listAll(env, path, recursive) {
  let j = await rpc(env, "files/list_folder", { path, recursive, limit: 2000 });
  const out = [...j.entries];
  while (j.has_more) { j = await rpc(env, "files/list_folder/continue", { cursor: j.cursor }); out.push(...j.entries); }
  return out;
}

const cleanName = s => String(s || "file").replace(/[\\/:*?"<>|\u0000-\u001f]/g, "_").slice(0, 180) || "file";
const KIND = n => /\.(jpe?g|png|heic|webp|gif)$/i.test(n) ? "photo" : /\.(mp4|mov|lrf|m4v|webm)$/i.test(n) ? "video"
  : /\.(m4a|mp3|aac|wav|ogg|opus|amr)$/i.test(n) ? "voice" : /^Claude notes/i.test(n) ? "claude" : /\.(txt|md)$/i.test(n) ? "note" : "file";

// ---------- API ----------
async function api(req, env, u) {
  const p = u.pathname.replace(/^\/trip\/api\//, "").replace(/\/$/, "");
  if (p === "login" && req.method === "POST") return login(req, env);
  if (!(await authed(req, env))) return json({ error: "PIN needed" }, 401);
  try {
    if (p === "days") {
      // One recursive listing, grouped by day folder.
      const entries = await listAll(env, TRIP, true);
      const days = DAYS.map(d => {
        const f = folderOf(d).toLowerCase() + "/";
        const files = entries.filter(e => e[".tag"] === "file" && e.path_lower.startsWith(f));
        const c = { photo: 0, video: 0, voice: 0, note: 0, file: 0, claude: 0 };
        files.forEach(e => c[KIND(e.name)]++);
        return { n: d[0], date: d[1], label: d[2], counts: c, total: files.length - c.claude };
      });
      return json({ days });
    }
    if (p === "day") {
      const d = dayByNum(u.searchParams.get("n"));
      if (!d) return json({ error: "No such day" }, 404);
      const entries = (await listAll(env, folderOf(d), false)).filter(e => e[".tag"] === "file");
      entries.sort((a, b) => (b.server_modified || "").localeCompare(a.server_modified || ""));
      const files = entries.map(e => ({ id: e.id, name: e.name, size: e.size, kind: KIND(e.name), at: e.server_modified }));
      // Read Claude's notes and her typed notes (small text files only).
      const texts = [];
      for (const f of files.filter(f => (f.kind === "claude" || f.kind === "note") && f.size < 200000).slice(0, 12)) {
        const r = await content(env, "files/download", { path: f.id }, null);
        if (r.ok) texts.push({ id: f.id, name: f.name, kind: f.kind, at: f.at, text: await r.text() });
      }
      return json({ day: { n: d[0], date: d[1], label: d[2] }, files: files.filter(f => f.kind !== "claude" && f.kind !== "note"), texts });
    }
    if (p === "thumb") {
      const r = await content(env, "files/get_thumbnail_v2",
        { resource: { ".tag": "path", path: u.searchParams.get("id") }, format: "jpeg", size: "w256h256", mode: "fitone_bestfit" }, null);
      if (!r.ok) return new Response("", { status: 404, headers: NOINDEX });
      return new Response(r.body, { headers: { "Content-Type": "image/jpeg", "Cache-Control": "private, max-age=86400", "X-Robots-Tag": "noindex" } });
    }
    if (p === "note" && req.method === "POST") {
      const { n, text } = await req.json();
      const d = dayByNum(n);
      if (!d || !String(text || "").trim()) return json({ error: "Nothing to save" }, 400);
      const stamp = new Date(Date.now() + 8 * 3600e3).toISOString().slice(0, 16).replace("T", " ").replace(":", "");
      const r = await contentJSON(env, "files/upload",
        { path: `${folderOf(d)}/Natali note ${stamp}.txt`, mode: "add", autorename: true }, enc.encode(String(text).slice(0, 100000)));
      return json({ ok: true, name: r.name });
    }
    // Chunked upload: start (first chunk), append, finish (last chunk). Chunks are 8 MB, under the Worker body limit.
    if (p === "up/start" && req.method === "POST") {
      const r = await contentJSON(env, "files/upload_session/start", { close: false }, await req.arrayBuffer());
      return json({ sid: r.session_id });
    }
    if (p === "up/append" && req.method === "POST") {
      const r = await content(env, "files/upload_session/append_v2",
        { cursor: { session_id: u.searchParams.get("sid"), offset: +u.searchParams.get("off") }, close: false }, await req.arrayBuffer());
      if (!r.ok) return json({ error: "Chunk failed: " + (await r.text()).slice(0, 200) }, 502);
      return json({ ok: true });
    }
    if (p === "up/finish" && req.method === "POST") {
      const d = dayByNum(u.searchParams.get("n"));
      if (!d) return json({ error: "No such day" }, 404);
      const r = await contentJSON(env, "files/upload_session/finish", {
        cursor: { session_id: u.searchParams.get("sid"), offset: +u.searchParams.get("off") },
        commit: { path: `${folderOf(d)}/${cleanName(u.searchParams.get("name"))}`, mode: "add", autorename: true, mute: true } }, await req.arrayBuffer());
      return json({ ok: true, name: r.name, size: r.size });
    }
    return json({ error: "Not found" }, 404);
  } catch (e) {
    return json({ error: String(e.message || e) }, 502);
  }
}

// ---------- one-time Dropbox connection ----------
async function connect(req, env, u) {
  const page = (body) => new Response(`<!doctype html><meta name=viewport content="width=device-width,initial-scale=1"><meta name=robots content=noindex><title>Connect Dropbox</title><body style="font:16px system-ui;max-width:560px;margin:40px auto;padding:0 18px;color:#243127">${body}</body>`,
    { headers: { "Content-Type": "text/html; charset=utf-8", ...NOINDEX } });
  if (!(await authed(req, env))) return Response.redirect("https://scratchandroam.com/trip/", 302);
  if (!env.DROPBOX_APP_KEY || !env.DROPBOX_APP_SECRET) return page("<h2>Almost there</h2><p>Add DROPBOX_APP_KEY and DROPBOX_APP_SECRET as secrets in Cloudflare first, then open this page again.</p>");
  const redirect = "https://scratchandroam.com/trip/connect/";
  const code = u.searchParams.get("code");
  if (!code) {
    const a = new URL("https://www.dropbox.com/oauth2/authorize");
    a.search = new URLSearchParams({ client_id: env.DROPBOX_APP_KEY, response_type: "code", token_access_type: "offline", redirect_uri: redirect });
    return Response.redirect(a.toString(), 302);
  }
  const r = await fetch("https://api.dropboxapi.com/oauth2/token", { method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({ code, grant_type: "authorization_code", redirect_uri: redirect,
      client_id: env.DROPBOX_APP_KEY, client_secret: env.DROPBOX_APP_SECRET }) });
  const j = await r.json();
  if (!j.refresh_token) return page(`<h2>That did not work</h2><p>${String(j.error_description || j.error || r.status).replace(/</g, "&lt;")}</p><p><a href="/trip/connect/">Try again</a></p>`);
  return page(`<h2>Dropbox approved</h2><p>Copy this and save it in Cloudflare as a secret called <b>DROPBOX_REFRESH_TOKEN</b>:</p>
<textarea readonly style="width:100%;height:110px;font:13px monospace" onclick="this.select()">${j.refresh_token}</textarea>
<p>Then open <a href="/trip/">the Hub</a>. You only do this once.</p>`);
}

export async function trip(req, env, u) {
  if (u.pathname.startsWith("/trip/api/")) return api(req, env, u);
  if (u.pathname === "/trip/connect/" || u.pathname === "/trip/connect") return connect(req, env, u);
  if (u.pathname === "/trip" ) return Response.redirect("https://scratchandroam.com/trip/", 301);
  if (u.pathname === "/trip/") return new Response(HUB, { headers: { "Content-Type": "text/html; charset=utf-8", ...NOINDEX,
    "Content-Security-Policy": "default-src 'self'; img-src 'self' blob: data:; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline'; connect-src 'self'; frame-ancestors 'none'" } });
  return new Response("Not found", { status: 404, headers: NOINDEX });
}
