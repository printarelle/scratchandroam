// Amazon short links.
//   /go/amazon?k=<search>   search link
//   /go/<name>              product link from src/amazon-links.json
// Ireland -> Amazon.ie (scratchandroa-21). Everyone else -> Amazon.com (scratchandroa-20),
// where Amazon OneLink sends UK, DE, FR, IT, ES, CA, JP, AU, NL and others to their own store with the right tag.
import LINKS from "./amazon-links.json";

const IE = ["www.amazon.ie", "scratchandroa-21"];
const COM = ["www.amazon.com", "scratchandroa-20"];

function go(dest) {
  return new Response(null, { status: 302, headers: {
    Location: dest, "Cache-Control": "private, no-store", "X-Robots-Tag": "noindex, nofollow" } });
}
const search = ([h, t], k) => k ? `https://${h}/s?k=${encodeURIComponent(k)}&tag=${t}` : `https://${h}/?tag=${t}`;
const product = ([h, t], asin) => `https://${h}/dp/${asin}?tag=${t}`;

export default {
  async fetch(req, env) {
    const u = new URL(req.url);
    // One address for every page: https://scratchandroam.com/<page>/ (Google indexed www. and http:// copies).
    // Host, protocol and trailing slash are fixed in ONE permanent redirect. Without the slash step here,
    // the assets layer (html_handling auto-trailing-slash) adds a second hop as a temporary 307.
    if (u.hostname.endsWith("scratchandroam.com")) {
      const last = u.pathname.split("/").pop();
      const needsSlash = !u.pathname.endsWith("/") && !last.includes(".") && !u.pathname.startsWith("/go/");
      if (u.hostname !== "scratchandroam.com" || u.protocol === "http:" || needsSlash) {
        u.hostname = "scratchandroam.com"; u.protocol = "https:"; u.port = "";
        if (needsSlash) u.pathname += "/";
        return Response.redirect(u.toString(), 301);
      }
    }
    const m = u.pathname.match(/^\/go\/([a-z0-9-]+)\/?$/);
    if (m) {
      const ie = ((req.cf && req.cf.country) || "") === "IE";
      const store = ie ? IE : COM;
      if (m[1] === "amazon") return go(search(store, (u.searchParams.get("k") || "").slice(0, 120)));
      const p = LINKS[m[1]];
      if (p && !m[1].startsWith("_")) {
        const asin = ie ? p.ie : p.com;
        return go(asin ? product(store, asin) : search(store, p.q || ""));
      }
    }
    return env.ASSETS.fetch(req);
  },
};
