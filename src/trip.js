// Private China Trip Hub for Natali, at /trip/ (PIN protected, never indexed).
// Same app as the claude.ai "China Trip Studio" artifact, but it runs on her own site so she
// never has to open Claude in China. The phone only talks to scratchandroam.com; this Worker
// keeps the hub data in Dropbox (_hub/hub.json), saves uploads into the Dropbox day folders the
// nightly Claude task reads, and serves Claude's nightly notes (_hub/notes/*.json) back.
//
// Secrets (Cloudflare > Workers > scratchandroam > Settings > Variables and secrets):
//   TRIP_PIN, DROPBOX_APP_KEY, DROPBOX_APP_SECRET, DROPBOX_REFRESH_TOKEN
// Optional: DROPBOX_ROOT_NS (team folder namespace, default below).
import HUB from "./trip-hub.html";
import SEED from "./trip-seed.json";

const ROOT_NS = "732279378"; // "DexPixel Ltd" team folder
const TRIP = "/Scratch and Roam/01_RAW/China/2026-12 December Trip";
const HUBDIR = TRIP + "/_hub";
const DATA = HUBDIR + "/hub.json";
const NOTES = HUBDIR + "/notes";
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
function folderOf(d) { const [n, iso, label] = d; const [, m, dd] = iso.split("-"); return `${TRIP}/Day ${n} - ${dd} ${MON[+m - 1]} - ${label}`; }
// Where an upload goes: the day folder for trip dates, otherwise a dated folder under _hub/other.
function dirFor(spec) {
  if (spec === "receipts") return HUBDIR + "/receipts";
  const m = /^day:(\d{4}-\d\d-\d\d)$/.exec(spec || "");
  if (m) { const d = DAYS.find(x => x[1] === m[1]); return d ? folderOf(d) : `${HUBDIR}/other/${m[1]}`; }
  return HUBDIR + "/other";
}

const NOINDEX = { "X-Robots-Tag": "noindex, nofollow, noarchive", "Cache-Control": "private, no-store" };
const json = (o, s = 200) => new Response(JSON.stringify(o), { status: s, headers: { "Content-Type": "application/json", ...NOINDEX } });
const enc = new TextEncoder();

// ---------- session ----------
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
  let pin = ""; try { pin = String((await req.json()).pin || ""); } catch {}
  if (!safeEq(pin, String(env.TRIP_PIN))) { await new Promise(r => setTimeout(r, 1500)); return json({ error: "Wrong PIN" }, 401); }
  const exp = String(Date.now() + 60 * 86400e3);
  const v = encodeURIComponent(exp + "." + await hmac(env, exp));
  return new Response(JSON.stringify({ ok: true }), { headers: { "Content-Type": "application/json", ...NOINDEX,
    "Set-Cookie": `trip=${v}; Path=/trip/; Max-Age=${60 * 86400}; HttpOnly; Secure; SameSite=Lax` } });
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
const argHeader = o => JSON.stringify(o).replace(/[\u007f-￿]/g, c => "\\u" + c.charCodeAt(0).toString(16).padStart(4, "0"));
const rootHeader = env => JSON.stringify({ ".tag": "namespace_id", namespace_id: env.DROPBOX_ROOT_NS || ROOT_NS });
async function rpc(env, path, body) {
  const r = await fetch("https://api.dropboxapi.com/2/" + path, { method: "POST", headers: {
    Authorization: "Bearer " + await token(env), "Content-Type": "application/json", "Dropbox-API-Path-Root": rootHeader(env) },
    body: JSON.stringify(body) });
  const t = await r.text(); let j; try { j = JSON.parse(t); } catch { j = { error_summary: t }; }
  if (!r.ok) { const e = new Error(j.error_summary || ("Dropbox error " + r.status)); e.dbx = j; throw e; }
  return j;
}
async function content(env, path, arg, body) {
  return fetch("https://content.dropboxapi.com/2/" + path, { method: "POST", headers: {
    Authorization: "Bearer " + await token(env), "Content-Type": "application/octet-stream",
    "Dropbox-API-Arg": argHeader(arg), "Dropbox-API-Path-Root": rootHeader(env) }, body });
}
async function contentJSON(env, path, arg, body) {
  const r = await content(env, path, arg, body); const t = await r.text();
  if (!r.ok) { const e = new Error("Dropbox error " + r.status + ": " + t.slice(0, 200)); e.status = r.status; e.body = t; throw e; }
  return t ? JSON.parse(t) : {};
}

// ---------- hub data (one JSON document in Dropbox) ----------
async function readData(env) {
  const r = await content(env, "files/download", { path: DATA }, null);
  if (r.status === 409) { // not created yet: start from the data copied from the claude.ai hub
    const meta = await contentJSON(env, "files/upload", { path: DATA, mode: "add", autorename: false, mute: true }, enc.encode(JSON.stringify(SEED)));
    return { data: JSON.parse(JSON.stringify(SEED)), rev: meta.rev };
  }
  if (!r.ok) throw new Error("Could not read hub data (" + r.status + ")");
  const meta = JSON.parse(r.headers.get("Dropbox-API-Result") || "{}");
  return { data: await r.json(), rev: meta.rev };
}
const COLS = ["places", "videos", "tasks", "days", "notes", "ideas", "expenses", "meta"];
function applyOps(data, ops) {
  for (const o of ops) {
    if (!COLS.includes(o.col) || !o.id || typeof o.id !== "string" || o.id.length > 120) throw new Error("Bad write");
    const c = data[o.col] || (data[o.col] = {});
    if (o.op === "set") c[o.id] = o.data || {};
    else if (o.op === "update") c[o.id] = Object.assign({}, c[o.id] || {}, o.data || {});
    else if (o.op === "delete") delete c[o.id];
    else throw new Error("Bad op");
  }
}
async function writeOps(env, ops) {
  for (let attempt = 0; attempt < 4; attempt++) {
    const { data, rev } = await readData(env);
    applyOps(data, ops);
    try {
      await contentJSON(env, "files/upload", { path: DATA, mode: { ".tag": "update", update: rev }, mute: true }, enc.encode(JSON.stringify(data)));
      return data;
    } catch (e) { if (e.status !== 409) throw e; await new Promise(r => setTimeout(r, 300 * (attempt + 1))); }
  }
  throw new Error("Busy, try again");
}
// Claude's nightly notes: one file per run, "<YYYY-MM-DD> run <HHMM>.json"; newest per date wins.
const noteCache = new Map(); // id -> {rev, obj}
async function nightlyNotes(env) {
  let entries = [];
  try {
    let j = await rpc(env, "files/list_folder", { path: NOTES, limit: 2000 });
    entries = j.entries; while (j.has_more) { j = await rpc(env, "files/list_folder/continue", { cursor: j.cursor }); entries.push(...j.entries); }
  } catch { return {}; }
  const latest = {};
  for (const e of entries) {
    const m = /^(\d{4}-\d\d-\d\d)\b.*\.json$/i.exec(e.name);
    if (e[".tag"] !== "file" || !m) continue;
    if (!latest[m[1]] || e.name > latest[m[1]].name) latest[m[1]] = e;
  }
  const out = {};
  await Promise.all(Object.entries(latest).map(async ([date, e]) => {
    let c = noteCache.get(e.id);
    if (!c || c.rev !== e.rev) {
      const r = await content(env, "files/download", { path: e.id }, null);
      if (!r.ok) return;
      try { c = { rev: e.rev, obj: await r.json() }; noteCache.set(e.id, c); } catch { return; }
    }
    out[date] = c.obj;
  }));
  return out;
}

const cleanName = s => String(s || "file").replace(/[\\/:*?"<>|\u0000-\u001f]/g, "_").slice(0, 180) || "file";
const MIME = n => { const x = (n.split(".").pop() || "").toLowerCase();
  return ({ jpg: "image/jpeg", jpeg: "image/jpeg", png: "image/png", gif: "image/gif", webp: "image/webp", heic: "image/heic",
    mp4: "video/mp4", mov: "video/quicktime", m4v: "video/mp4", webm: "video/webm", lrf: "video/mp4",
    m4a: "audio/mp4", mp3: "audio/mpeg", aac: "audio/aac", wav: "audio/wav", ogg: "audio/ogg", opus: "audio/ogg", amr: "audio/amr",
    pdf: "application/pdf", txt: "text/plain; charset=utf-8", md: "text/plain; charset=utf-8", json: "application/json" })[x] || "application/octet-stream"; };

// ---------- API ----------
async function api(req, env, u) {
  const p = u.pathname.replace(/^\/trip\/api\//, "").replace(/\/$/, "");
  if (p === "login" && req.method === "POST") return login(req, env);
  if (!(await authed(req, env))) return json({ error: "PIN needed" }, 401);
  try {
    if (p === "db" && req.method === "GET") {
      const [{ data }, nightly] = await Promise.all([readData(env), nightlyNotes(env)]);
      data.notes = Object.assign({}, data.notes || {}, nightly);
      return json({ data });
    }
    if (p === "db" && req.method === "POST") {
      const { ops } = await req.json();
      if (!Array.isArray(ops) || !ops.length || ops.length > 50) return json({ error: "Nothing to save" }, 400);
      await writeOps(env, ops);
      return json({ ok: true });
    }
    if (p === "blob") {
      const id = u.searchParams.get("id") || "";
      if (!/^id:[\w-]+$/.test(id)) return new Response("", { status: 404, headers: NOINDEX });
      if (u.searchParams.get("t")) {
        const r = await content(env, "files/get_thumbnail_v2",
          { resource: { ".tag": "path", path: id }, format: "jpeg", size: "w640h480", mode: "fitone_bestfit" }, null);
        if (r.ok) return new Response(r.body, { headers: { "Content-Type": "image/jpeg", "Cache-Control": "private, max-age=604800", "X-Robots-Tag": "noindex" } });
      }
      const r = await content(env, "files/download", { path: id }, null);
      if (!r.ok) return new Response("", { status: 404, headers: NOINDEX });
      const meta = JSON.parse(r.headers.get("Dropbox-API-Result") || "{}");
      return new Response(r.body, { headers: { "Content-Type": MIME(meta.name || ""),
        "Content-Disposition": `inline; filename*=UTF-8''${encodeURIComponent(meta.name || "file")}`, "Cache-Control": "private, max-age=604800", "X-Robots-Tag": "noindex" } });
    }
    // Chunked upload: start (first chunk), append, finish (last chunk). 8 MB chunks keep every request small.
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
      const r = await contentJSON(env, "files/upload_session/finish", {
        cursor: { session_id: u.searchParams.get("sid"), offset: +u.searchParams.get("off") },
        commit: { path: `${dirFor(u.searchParams.get("dir"))}/${cleanName(u.searchParams.get("name"))}`, mode: "add", autorename: true, mute: true } },
        await req.arrayBuffer());
      return json({ id: r.id, name: r.name, size: r.size, path: r.path_display });
    }
    return json({ error: "Not found" }, 404);
  } catch (e) {
    return json({ error: String(e.message || e) }, 502);
  }
}

// ---------- one-time Dropbox connection ----------
async function connect(req, env, u) {
  const page = (body) => new Response(`<!doctype html><meta name=viewport content="width=device-width,initial-scale=1"><meta name=robots content=noindex><title>Connect Dropbox</title><body style="font:16px system-ui;max-width:560px;margin:40px auto;padding:0 18px;color:#1F2A26">${body}</body>`,
    { headers: { "Content-Type": "text/html; charset=utf-8", ...NOINDEX } });
  const code = u.searchParams.get("code");
  let ok = await authed(req, env);
  if (!ok && code) {
    const [exp, sig] = String(u.searchParams.get("state") || "").split(".");
    ok = !!exp && Date.now() < +exp && safeEq(sig || "", await hmac(env, "state" + exp));
  }
  if (!ok) return Response.redirect("https://scratchandroam.com/trip/", 302);
  if (!env.DROPBOX_APP_KEY || !env.DROPBOX_APP_SECRET) return page("<h2>Almost there</h2><p>Add DROPBOX_APP_KEY and DROPBOX_APP_SECRET as secrets in Cloudflare first, then open this page again.</p>");
  const redirect = "https://scratchandroam.com/trip/connect/";
  if (!code) {
    const a = new URL("https://www.dropbox.com/oauth2/authorize");
    const exp = String(Date.now() + 15 * 60e3);
    a.search = new URLSearchParams({ client_id: env.DROPBOX_APP_KEY, response_type: "code", token_access_type: "offline",
      redirect_uri: redirect, state: exp + "." + await hmac(env, "state" + exp) });
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

const SW = '// Trip Hub service worker: lets the Hub open with no internet and keeps thumbnails.\nconst C = "trip-shell-v2";\nconst SHELL = ["/trip/", "/favicon.svg", "/fonts/trip/dmsans-normal-400-latin-ext.woff2", "/fonts/trip/dmsans-normal-400-latin.woff2", "/fonts/trip/dmsans-normal-500-latin-ext.woff2", "/fonts/trip/dmsans-normal-500-latin.woff2", "/fonts/trip/dmsans-normal-600-latin-ext.woff2", "/fonts/trip/dmsans-normal-600-latin.woff2", "/fonts/trip/fraunces-italic-500-latin-ext.woff2", "/fonts/trip/fraunces-italic-500-latin.woff2", "/fonts/trip/fraunces-normal-500-latin-ext.woff2", "/fonts/trip/fraunces-normal-500-latin.woff2"];\nself.addEventListener("install", e => { e.waitUntil(caches.open(C).then(c => c.addAll(SHELL)).then(() => self.skipWaiting())); });\nself.addEventListener("activate", e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k.startsWith("trip-shell") && k !== C).map(k => caches.delete(k)))).then(() => self.clients.claim())); });\nself.addEventListener("fetch", e => {\n  if (e.request.method !== "GET") return;\n  const u = new URL(e.request.url);\n  if (u.origin !== location.origin) return;\n  if (u.pathname === "/trip/" || u.pathname === "/trip") {\n    e.respondWith(fetch(e.request).then(r => { if (r.ok) { const cp = r.clone(); caches.open(C).then(c => c.put("/trip/", cp)); } return r; }).catch(() => caches.match("/trip/")));\n    return;\n  }\n  if (u.pathname.startsWith("/fonts/trip/") || u.pathname === "/favicon.svg" || u.pathname === "/trip/manifest.webmanifest") {\n    e.respondWith(caches.match(e.request).then(r => r || fetch(e.request).then(res => { if (res.ok) { const cp = res.clone(); caches.open(C).then(c => c.put(e.request, cp)); } return res; })));\n    return;\n  }\n  if (u.pathname === "/trip/api/blob" && u.searchParams.get("t")) {\n    e.respondWith(caches.open("trip-thumbs").then(c => c.match(e.request).then(r => r || fetch(e.request).then(res => { if (res.ok) c.put(e.request, res.clone()); return res; }))));\n  }\n});\n';
const MANIFEST = '{"name":"China Trip Studio","short_name":"Trip Hub","start_url":"/trip/#today","scope":"/trip/","display":"standalone","background_color":"#F6F7F3","theme_color":"#2F5A47","icons":[{"src":"/favicon.svg","sizes":"any","type":"image/svg+xml"}]}';

export async function trip(req, env, u) {
  if (u.pathname === "/trip/sw.js") return new Response(SW, { headers: { "Content-Type": "text/javascript; charset=utf-8", "Cache-Control": "no-cache", "Service-Worker-Allowed": "/trip/", "X-Robots-Tag": "noindex" } });
  if (u.pathname === "/trip/manifest.webmanifest") return new Response(MANIFEST, { headers: { "Content-Type": "application/manifest+json", "Cache-Control": "no-cache", "X-Robots-Tag": "noindex" } });
  if (u.pathname.startsWith("/trip/api/")) return api(req, env, u);
  if (u.pathname === "/trip/connect/" || u.pathname === "/trip/connect") return connect(req, env, u);
  if (u.pathname === "/trip") return Response.redirect("https://scratchandroam.com/trip/", 301);
  if (u.pathname === "/trip/") return new Response(HUB, { headers: { "Content-Type": "text/html; charset=utf-8", ...NOINDEX,
    "Content-Security-Policy": "default-src 'self'; img-src 'self' blob: data:; media-src 'self' blob:; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline'; font-src 'self'; connect-src 'self'; worker-src 'self'; manifest-src 'self'; frame-ancestors 'none'" } });
  return new Response("Not found", { status: 404, headers: NOINDEX });
}
