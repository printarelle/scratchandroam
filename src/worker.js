// Amazon links: /go/amazon?k=<search>
// Ireland -> Amazon.ie (scratchandroa-21). Everyone else -> Amazon.com (scratchandroa-20),
// where Amazon OneLink sends UK, DE, FR, IT, ES, CA, JP, AU, NL and others to their own store with the right tag.
const STORES = { IE: ["www.amazon.ie", "scratchandroa-21"] };
const DEFAULT = ["www.amazon.com", "scratchandroa-20"];

export default {
  async fetch(req, env) {
    const u = new URL(req.url);
    if (u.pathname === "/go/amazon" || u.pathname === "/go/amazon/") {
      const country = (req.cf && req.cf.country) || "";
      const [host, tag] = STORES[country] || DEFAULT;
      const k = (u.searchParams.get("k") || "").slice(0, 120);
      const dest = k
        ? `https://${host}/s?k=${encodeURIComponent(k)}&tag=${tag}`
        : `https://${host}/?tag=${tag}`;
      return new Response(null, { status: 302, headers: {
        Location: dest, "Cache-Control": "private, no-store", "X-Robots-Tag": "noindex, nofollow" } });
    }
    return env.ASSETS.fetch(req);
  },
};
