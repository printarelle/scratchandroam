# Bright edition templates: header, footer, guide page, home page.
import re, html
from voice import STORIES

IC = {
 "clock": '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
 "share": '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="M8.6 13.5l6.8 4M15.4 6.5l-6.8 4"/></svg>',
 "search": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>',
 "menu": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
 "bulb": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-4 10.5c.7.6 1 1.4 1 2.5h6c0-1.1.3-1.9 1-2.5A6 6 0 0 0 12 3z"/></svg>',
 "warn": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3 2 20h20L12 3z"/><path d="M12 10v4M12 17v.5"/></svg>',
 "plane": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 16l20-8-6 14-3-6-6-3z"/></svg>',
 "cal": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 22s7-6.3 7-12a7 7 0 1 0-14 0c0 5.7 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></svg>',
 "heart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s-7-4.6-9.3-9A5.2 5.2 0 0 1 12 6.6 5.2 5.2 0 0 1 21.3 12C19 16.4 12 21 12 21z"/></svg>',
 "book": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h7a3 3 0 0 1 3 3v13a2 2 0 0 0-2-2H4zM20 4h-7a3 3 0 0 0-3 3v13a2 2 0 0 1 2-2h8z"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
}

def _t(x): return re.sub(r'<[^>]+>','',html.unescape(str(x)))

def nav_b(SOC, NAV_SHOP):
    return f'''<header class="hb"><div class="wrap"><a class="logo" href="/" aria-label="Scratch and Roam with Natali, home"><span class="mark">Scratch <em>&amp;</em> Roam</span><span class="with">with Natali</span></a>
<nav id="menu"><a href="/">Home</a><a href="/china/">China guides</a>{NAV_SHOP()}<a href="/where-ive-been/">Where I've been</a><a href="/#december">December trip</a><a href="/travel-deals/">Travel deals</a><a href="/about/">About</a></nav>
<div class="right"><button class="icbtn" id="sbtn" type="button" aria-label="Search guides" aria-haspopup="dialog">{IC["search"]}</button><a class="btn" href="{SOC['YouTube']}?sub_confirmation=1" rel="me noopener">Subscribe</a><button class="icbtn mbtn" id="menuBtn" aria-expanded="false" aria-controls="menu" aria-label="Menu">{IC["menu"]}</button></div></div></header>'''

def footer_b(SOC, FOOT_GROUPS, CARDS):
    by={c["slug"]:c for c in CARDS}
    cols=""
    for h,l in FOOT_GROUPS:
        sl=[x for x in l if x in by]
        cols+=f'<div><h3>{html.escape(h)}</h3><nav>'+"".join(f'<a href="/guides/{x}/">{html.escape(by[x]["short"])}</a>' for x in sl)+'</nav></div>'
    links="".join(f'<a href="{u}" rel="me noopener">{n}</a>' for n,u in SOC.items())
    return f'''<footer class="ft"><div class="wrap"><div class="grid"><div><a class="logo" href="/"><span class="mark">Scratch <em>&amp;</em> Roam</span><span class="with">with Natali</span></a><p class="tag">Real first-timer China. Real screenshots. Real prices, with the date I checked them.</p><h3 style="margin-top:22px">Follow along</h3><nav>{links}</nav></div>{cols}<div class="stamp">Scratch to reveal<span>Roam</span>to discover</div></div><div class="fine"><span>© 2026 Scratch &amp; Roam with Natali, Ireland. As an Amazon Associate I earn from qualifying purchases.</span><span><a href="/about/">About</a> · <a href="/travel-deals/">Travel deals</a> · <a href="/klook/">Klook</a> · <a href="/affiliate-disclosure/">Affiliate disclosure</a> · <a href="/feed.xml">RSS</a> · scratchandroam@gmail.com</span></div></div></footer>'''

NAVJS_B='<script>(function(){var b=document.getElementById("menuBtn"),m=document.getElementById("menu");if(b){b.addEventListener("click",function(){var o=m.classList.toggle("open");b.setAttribute("aria-expanded",o?"true":"false");});}var L=[].slice.call(document.querySelectorAll(".toc a[href^=\\"#\\"]"));if(L.length&&"IntersectionObserver" in window){var map={};L.forEach(function(a){map[a.getAttribute("href").slice(1)]=a;});var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){L.forEach(function(a){a.classList.remove("on")});var a=map[e.target.id];if(a)a.classList.add("on");}});},{rootMargin:"-20% 0px -70% 0px"});Object.keys(map).forEach(function(id){var el=document.getElementById(id);if(el)io.observe(el);});L[0].classList.add("on");}})();</script>'

def callout(kind, text):
    return f'<div class="callout {kind}">{IC["bulb" if kind=="tip" else "warn"]}<div>{text}</div></div>'

def stats_b(n_guides, title="A bit about my trips to China."):
    S=[("plane","2","Trips to China"),("cal","Dec 2025","First trip, Christmas"),("pin","Apr 2026","Second trip, Easter"),("book",str(n_guides),"Dated guides"),("heart","Dec 2026","Next: Chengdu, Chongqing, Xi'an")]
    return f'<section class="stats"><div class="wrap"><h2>{html.escape(title)}</h2><div class="row">'+"".join(f'<div class="stat">{IC[i]}<b>{v}</b><span>{l}</span></div>' for i,v,l in S)+'</div></div></section>'

def band_b(SOC):
    return f'''<section class="band"><div class="wrap"><div class="bcard">{IC["mail"]}<h2>Planning a China trip? Start with the arrival card.</h2><p>Every guide here is dated and rechecked against the official source. Start with the two things that catch first-timers out: the arrival card and Alipay. Save the checklists on Pinterest so they are there when you pack.</p><div class="acts"><a class="btn" href="/guides/china-arrival-card-pc/">Arrival card, step by step</a><a class="btn ghost" href="/guides/first-time-in-china/">13 things before you fly</a></div><small>No sign-up, no newsletter. Just the guides.</small></div></div></section>'''

def social_b(SOC, img_yt, img_ig):
    return f'''<section class="social"><div class="wrap"><div class="box"><h2>Let's keep roaming together!</h2><p class="sub">Follow along for the videos behind these guides, the screenshots as I take them, and the next trip as it happens.</p><div class="socs">
<div class="soc yt"><img src="/img/{img_yt}.jpg" alt="" loading="lazy"><div class="in"><div class="brand"><i>&#9654;</i>YouTube</div><h3>Watch the guides</h3><p>Full videos with chapters, filmed on the trip, step by step on screen.</p><ul><li><i>&#9654;</i>Arrival card, Alipay, metro walkthroughs</li><li><i>&#10003;</i>Shanghai at night, from the Bund to the river</li><li><i>&#9733;</i>December: Chengdu, Chongqing, Xi'an</li></ul><a class="btn" href="{SOC['YouTube']}?sub_confirmation=1" rel="noopener">Subscribe on YouTube</a></div></div>
<div class="soc tt"><img src="/img/{img_ig}.jpg" alt="" loading="lazy"><div class="in"><div class="brand"><i>&#9835;</i>TikTok</div><h3>Follow the trip</h3><p>The short versions of every guide, and the trip as it happens.</p><ul><li><i>&#9835;</i>Shorts from Shanghai and the next cities</li><li><i>&#9679;</i>Photo carousels of each checklist</li><li><i>&#9679;</i>Behind the scenes of the videos</li></ul><a class="btn" href="{SOC['TikTok']}" rel="noopener">Follow on TikTok</a></div></div>
</div><div class="thanks"><b>Thank you for being here.</b>Every guide is written from my own trip, checked on the date shown, and free to read. If one saved you a queue, share it with the next first-timer.</div></div></div></section>'''

TEXT_GALLERIES={"shanghai-circus-world-era-show"}  # galleries whose frames carry text: never cropped
def _stack_tables(h):
    # label every cell with its column header so tables turn into cards on phones; wrap for scrolling
    def one(m):
        t=m.group(0)
        heads=[re.sub(r'<[^>]+>','',x).strip() for x in re.findall(r'<th[^>]*>(.*?)</th>',t,re.S)]
        if not heads: return t
        def row(r):
            i=[0]
            def cell(c):
                lab=heads[i[0]] if i[0]<len(heads) else ''
                i[0]+=1
                return c.group(0).replace('<td','<td data-label="'+html.escape(lab)+'"',1) if 'data-label' not in c.group(0) else c.group(0)
            return re.sub(r'<td[^>]*>',cell,r.group(0))
        t=re.sub(r'<tr[^>]*>.*?</tr>',row,t,flags=re.S)
        t=re.sub(r'<table( class="([^"]*)")?',lambda k:'<table class="stack '+(k.group(2) or '')+'"',t,1)
        return t
    h=re.sub(r'<table.*?</table>',one,h,flags=re.S)
    h=re.sub(r'(?<!sp-tw">)(<table class="stack[^"]*">.*?</table>)',r'<div class="tablewrap">\1</div>',h,flags=re.S)
    return h

def guide_b(*, slug, h1, desc, intro, steps, faq, sources, vid, gallery, chapters, related, checked, published, steps_title, shorts, extra, video_note, shotnote, IMGREG, SOC, yt, start, CARDS, n_guides, title):
    def figs(keys):
        if not keys: return ""
        return '<div class="shots">'+"".join(f'<figure><a href="/img/{k}.jpg"><img src="/img/{k}.jpg" alt="" loading="lazy"></a><figcaption>{html.escape(IMGREG[k+".jpg"]["cap"])}</figcaption></figure>' for k in keys)+'</div><p class="shotnote">'+(shotnote or 'Screenshots from my own phone. The app is in Chinese, the English labels are mine. Tap a picture to open it larger.')+'</p>'
    rd=max(3,round(len(_t(intro)+" ".join(_t(s[1]) for s in steps)+" ".join(_t(a) for q,a in faq))/900))
    kind='Video + steps' if vid else ('Place guide' if gallery else 'Checklist')
    # hero photo: first gallery photo, else the guide cover
    by={c["slug"]:c for c in CARDS}
    cover=by[slug]["img"]
    CLEAN=["the-bund-pudong-skyline-and-shanghai-tower-at-night","nanjing-road-curved-corner-building-neon-lights","huangpu-river-pudong-skyline-with-gold-reflections","the-bund-peace-hotel-green-roofs-lit-at-night","the-bund-pink-lit-pearl-tower-over-the-crowd","the-bund-oriental-pearl-tower-from-the-promenade"]
    hero_img=gallery[0][0] if gallery else CLEAN[sum(map(ord,slug))%len(CLEAN)]
    hero_cap=(IMGREG.get(hero_img+".jpg",{}).get("cap") or "") if gallery else "Shanghai, October 2026"
    # body pieces
    toc=[]
    body=[]
    body.append(f'<div class="intro">{intro}</div>')
    if slug in STORIES:
        st_t,st_h=STORIES[slug]
        body.append(f'<h2 id="our-trip">{html.escape(st_t)}</h2><div class="story">{st_h}</div>'); toc.append(("our-trip",st_t))
    if vid:
        body.append(f'<h2 id="video">Watch the video</h2>'); toc.append(("video","Watch the video"))
        body.append(yt(vid,title,start).replace('class="video"','class="video"'))
        if video_note: body.append(video_note)
        if chapters:
            body.append('<div class="chapters"><h3>In the video</h3><ol>'+"".join(f'<li><span>{t}</span>{html.escape(c)}</li>' for t,c in chapters)+'</ol></div>')
    if gallery and len(gallery)>1:
        gs=gallery[1:5]
        cc=' class="cover"' if slug in TEXT_GALLERIES else ''
        body.append('<div class="gal2">'+"".join(f'<figure><img src="/img/{g[0]}.jpg" alt="" loading="lazy"{cc}><figcaption>{html.escape(IMGREG.get(g[0]+".jpg",{}).get("cap") or "")}</figcaption></figure>' for g in gs)+'</div>')
    if faq:
        body.append('<h2 id="quick">Quick answers</h2>'); toc.append(("quick","Quick answers"))
        body.append('<div class="faq">'+"".join(f'<div><h3>{html.escape(q)}</h3><p>{a}</p></div>' for q,a in faq)+'</div>')
    if steps:
        body.append(f'<h2 id="steps">{html.escape(steps_title)}</h2>'); toc.append(("steps",steps_title))
        body.append('<ol class="steps">'+"".join(f'<li id="step-{i+1}"><div class="n">{i+1}</div><div><h3>{html.escape(s[0])}</h3><p>{s[1]}</p>{figs(s[2] if len(s)>2 else None)}</div></li>' for i,s in enumerate(steps))+'</ol>')
    if extra:
        # lift h2 ids out of extra for the toc
        ex=extra
        for m in re.finditer(r'<h2(?: id="([^"]+)")?>(.*?)</h2>',extra,re.S):
            idv=m.group(1) or re.sub(r'[^a-z0-9]+','-',_t(m.group(2)).lower()).strip('-')[:40]
            toc.append((idv,_t(m.group(2))))
            if not m.group(1): ex=ex.replace(m.group(0),f'<h2 id="{idv}">{m.group(2)}</h2>',1)
        body.append(ex)
    if AFFILIATES_LIVE and slug in OFFERS: body.append(offers_b(OFFERS[slug],slug)); toc.append(("book",OFFER_HEAD.get(slug,("Where to book",))[0]))
    if slug in AMAZON:
        body.append(amazon_b(slug)); toc.append(("amazon",AMAZON[slug][0]))
    if slug in GUIDE_DEALS:
        body.append(guide_deals_b(slug)); toc.append(("links","Links for this guide"))
    if slug in GYG_WIDGET_SLUGS:
        body.append('<h2 id="more-shanghai">More things to do in Shanghai</h2><p>A live list of Shanghai tours and tickets from GetYourGuide. These are affiliate links: if you book through one, I earn a small commission and you pay the same price. I have not done every one of these, so read the details before you book.</p><div class="gygw">'+GYG_SHANGHAI_WIDGET+'</div>'); toc.append(("more-shanghai","More things to do in Shanghai"))
    body.append(callout("tip",f'Rules change. Everything on this page was checked on {checked} against the sources below. Before you fly, open the official page once more.'))
    body.append('<h2 id="sources">Sources</h2>'); toc.append(("sources","Sources"))
    body.append('<ul class="sources">'+"".join(f'<li><a href="{u}" rel="noopener">{html.escape(n)}</a>{" (official)" if off else ""}</li>' for n,u,off in sources)+'</ul>')
    _ord=["TikTok","YouTube","Pinterest","Instagram","Facebook"]
    shorts_links=" · ".join(f'<a href="{u}" rel="noopener">{n}</a>' for n,u in sorted((shorts or {}).items(),key=lambda kv:_ord.index(kv[0]) if kv[0] in _ord else 9))
    body.append(f'<div class="enjoy"><div><b>Enjoy the guide? Watch it short.</b>The same guide as a vertical video{": "+shorts_links if shorts_links else ""}.</div><div class="row"><a href="{SOC["TikTok"]}" rel="noopener">TikTok</a><a href="{SOC["Instagram"]}" rel="noopener">Instagram</a><a href="{SOC["Pinterest"]}" rel="noopener">Pinterest</a></div></div>')
    toc_html='<ol>'+"".join(f'<li><a href="#{i}">{html.escape(t)}</a></li>' for i,t in toc)+'</ol>'
    # sidebar
    rel=related or []
    more=rel[:4]
    if len(more)<4:
        for c in CARDS:
            if c["slug"]!=slug and all(c["slug"] not in u for u,_,_,_ in more): more.append((f'/guides/{c["slug"]}/',c["img"],"Guide",c.get("short") or c["slug"]))
            if len(more)>=4: break
    more_html="".join(f'<a href="{u}"><img src="/img/{cl}.jpg" alt="" loading="lazy"><span><span class="cat">Guide</span><b>{html.escape(n)}</b><small>{html.escape(t)}</small></span></a>' for u,cl,t,n in more)
    cloud="".join(f'<a href="{u}">{n}</a>' for n,u in [("China","/china/"),("Shanghai","/#shanghai"),("Arrival card","/guides/china-arrival-card-pc/"),("Alipay","/guides/china-travel-apps/"),("Visa free","/guides/china-visa-free-30-days/"),("Metro","/guides/alipay-metro-qr-code-china/"),("Taobao","/guides/taobao-for-foreigners/"),("Food","/guides/how-to-order-food-in-china-without-speaking-chinese/")])
    crumb_last=html.escape(_t(h1).split(":")[0])
    return f'''<main>
<section class="ghero"><div class="wrap">
<div class="hcard">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span><a href="/china/">Asia</a><span>/</span><a href="/china/">China</a><span>/</span><span>{crumb_last}</span></nav>
<div class="tags"><a class="pill mint" href="/china/">Guide</a><a class="pill mint" href="/china/">China</a><a class="pill mint" href="/#shanghai">Shanghai</a><span class="pill mint">{kind}</span></div>
<div class="meta"><span class="pill coral">{IC["clock"]}{rd} min read</span><a class="pill blue" href="#share">{IC["share"]}Share</a></div>
<h1>{h1}</h1>
<p class="lede">{desc}</p>
<div class="author"><img src="/img/natali-portrait-at-her-desk.jpg" alt=""><div><b>By Natali</b><p>A maker from Ireland who films her trips and writes down the parts nobody explains. First-timer China, with the screenshots to prove it.</p></div></div>
<p class="dates">Last updated: {checked}{f"<br>Published: {published}" if published else ""}</p>
</div>
<figure class="polaroid"><img src="/img/{hero_img}.jpg" alt="" data-hero{"" if (gallery and slug not in TEXT_GALLERIES) else " class=\"cover\""}><figcaption>{html.escape(hero_cap)[:60]}</figcaption></figure>
</div></section>
<p class="strip">Every price and rule on this page was checked on {checked}.{(" "+AFF_NOTE) if (AFFILIATES_LIVE and (slug in OFFERS or slug in AFF_INLINE or slug in GUIDE_DEALS or slug in AMAZON)) else " Nothing here is sponsored."}</p>
<div class="wrap cols">
<aside><nav class="toc" id="toc"><b>On this page</b>{toc_html}</nav></aside>
<article class="art"><details class="mtoc"><summary>On this page</summary>{toc_html}</details>{_stack_tables("".join(body))}</article>
<aside class="side" id="share">
<div class="scard me"><img src="/img/natali-portrait-at-her-desk.jpg" alt=""><h3>Hi, I'm Natali</h3><p>I'm a maker from Ireland. I film my trips, then write down the parts nobody explains, with the date I checked each one.</p><a href="/about/">More about my story →</a></div>
<div class="scard"><span class="eyebrow">More guides</span><div class="mlist">{more_html}</div></div>
<div class="scard"><span class="eyebrow">Popular topics</span><div class="cloud">{cloud}</div></div>
</aside>
</div>
{stats_b(n_guides)}
{band_b(SOC)}
{social_b(SOC,"the-bund-pudong-skyline-and-shanghai-tower-at-night","nanjing-road-curved-corner-building-neon-lights")}
</main>'''

def home_b(*, CARDS, SOC, n_guides):
    by={c["slug"]:c for c in CARDS}
    def gcard(c,small=False):
        return f'<a class="gc" href="/guides/{c["slug"]}/"><img src="/img/{c["img"]}.jpg" alt="{html.escape(c["alt"])}" loading="lazy"><div class="in"><span class="cat">{html.escape(c["meta"][0] if c.get("meta") else "Guide")}</span><h3>{html.escape(c.get("t") or c["short"])}</h3>{"" if small else f"<p>{html.escape(c.get(chr(112),chr(32)))}</p>"}<small>{html.escape(c["meta"][1] if c.get("meta") else "Shanghai")}</small></div></a>'
    start=[by[s] for s in ("china-arrival-card-pc","first-time-in-china","china-travel-apps")]
    before=[c for c in CARDS if c["sec"] in ("before","shop") and c not in start]
    places=[c for c in CARDS if c["sec"]=="place"]
    dests=f'''<a class="dest" href="/china/"><img src="/img/the-bund-pink-lit-pearl-tower-over-the-crowd.jpg" alt=""><div class="in"><h3>Shanghai</h3><small>{n_guides} guides</small><p>Two trips: Christmas 2025 and Easter 2026. The arrival card, Alipay, the metro QR, the Bund at night, the river cruise and the ERA show.</p></div></a>
<a class="dest soon" href="/#december"><img src="/img/huangpu-river-pudong-skyline-with-gold-reflections.jpg" alt=""><div class="in"><h3>Chengdu, Chongqing, Xi'an</h3><small>December 2026, filming</small><p>Trains between the three, the metro cards, and the first pandas. Guides go up as I check each one.</p></div></a>
<a class="dest soon" href="{SOC['YouTube']}?sub_confirmation=1" rel="noopener"><img src="/img/the-bund-peace-hotel-green-roofs-lit-at-night.jpg" alt=""><div class="in"><h3>Japan</h3><small>Next trip</small><p>The next country on the list. Subscribe and the first guide lands in your feed.</p></div></a>'''
    return f'''<main>
<section class="hhero"><div class="wrap"><div><p class="eyebrow">Real first-timer China. Real screenshots.</p><h1>China travel guides, step by step, from someone who just did it</h1><p class="lede">I'm Natali, a maker from Ireland. I filmed my first trip to China and wrote down every form, app and queue that nobody explains, with the date I checked each one.</p><div class="acts"><a class="btn" href="/guides/china-arrival-card-pc/">Start with the arrival card</a><a class="btn ghost" href="/china/">{IC["pin"]} Browse China guides</a></div><a class="small" href="{SOC['YouTube']}?sub_confirmation=1" rel="noopener">{IC["mail"]} Watch the videos behind the guides</a></div>
<div class="collage"><figure><img src="/img/the-bund-gold-lit-historic-buildings-at-night.jpg" alt=""><figcaption>The Bund</figcaption></figure><figure><img src="/img/nanjing-road-curved-corner-building-neon-lights.jpg" alt=""><figcaption>Nanjing Road</figcaption></figure></div></div></section>
{stats_b(n_guides,"A bit about my travels.")}
<section class="sec"><div class="wrap"><div class="sechead"><p class="eyebrow">Where I've been</p><h2>Where I've been. Where I can help.</h2><p>First-timer guides from the trips I've actually taken, with the screenshots from my own phone and the prices I actually paid.</p></div><div class="dests">{dests}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="sechead left"><div><h2>Planning a China trip? Start here.</h2><p>The three guides first-timers need before anything else.</p></div><a class="more" href="/china/">All China guides →</a></div><div class="gcards">{"".join(gcard(c) for c in start)}</div></div></section>
<section class="sec mint"><div class="wrap"><div class="sechead left"><div><h2>Before you fly</h2><p>Visa rules, the arrival card, apps, food, shopping and what not to pack.</p></div></div><div class="gcards sm">{"".join(gcard(c,True) for c in before)}</div></div></section>
<section class="sec" id="shanghai"><div class="wrap"><div class="sechead left"><div><p class="eyebrow">Shanghai</p><h2>Shanghai after dark</h2><p>The Bund, Nanjing Road, the river cruise and the ERA show, with the metro exit and the time the lights go off.</p></div></div><div class="gcards sm">{"".join(gcard(c,True) for c in places)}</div></div></section>
<section class="sec mint" id="december" style="padding:48px 0"><div class="wrap"><div class="sechead"><p class="eyebrow">Coming next</p><h2>December: Chengdu, Chongqing and Xi'an</h2><p>High-speed trains between the three, metro cards in each city, and the pandas. Guides go up as I check each one.</p><a class="btn" style="margin-top:18px" href="{SOC['YouTube']}?sub_confirmation=1" rel="noopener">Subscribe to catch them</a></div></div></section>
{band_b(SOC)}
{social_b(SOC,"the-bund-pudong-skyline-and-shanghai-tower-at-night","nanjing-road-curved-corner-building-neon-lights")}
</main>'''

# ===== affiliate / partner components =====
AFFILIATES_LIVE=True   # per guide: only guides listed in OFFERS show booking cards and the disclosure
PARTNER_PAGES=True     # /klook/ live (her general Klook link); add more partner pages to PARTNERS when she sends links
AFF_NOTE='This page has affiliate links. If you book through one I earn a small commission at no extra cost to you. I always say which ones we booked ourselves. <a href="/affiliate-disclosure/">Affiliate disclosure</a>.'
# Placeholder partner links. Replace "#TODO" with the real affiliate URLs / codes.
PARTNERS={
 "klook":dict(name="Klook",code=None,url="https://klook.tpm.li/jfysgwVe",qr="klook-scratch-and-roam-link-qr-code"),
}
KLOOK_CRUISE="https://klook.tpm.li/Gt6dONHf"
GYG_CRUISE="https://gyg.me/3PFkogxt"
OFFERS={
 # Only links Natali gave. "pick"/badge only where she says she booked it. Prices only if she gives them.
 "shanghai-circus-world-era-show":[
  dict(k="Klook",price=None,title="ERA: Intersection of Time, Shanghai Circus World",
       text="This is where we booked our ERA tickets. You choose a zone and the date, and the ticket comes through Klook. The zones and how to pick one are explained in the steps below.",
       url="https://klook.tpm.li/YtyjQpDu",pick=True,badge="Where we booked",cta="See ERA tickets on Klook",
       qr="klook-era-shanghai-circus-world-tickets-qr-code",qralt="QR code for the Klook ERA ticket page"),
  dict(k="GetYourGuide",price=None,title="Shanghai: ERA Circus Show Ticket",
       text="ERA tickets on GetYourGuide. Pick your date and zone, and check the price for your date before you pay. The zones and how to pick one are explained in the steps below.",
       url="https://gyg.me/kRBIqnuP",cta="See ERA tickets on GetYourGuide",alt=True),
 ],
 "huangpu-river-night-cruise":[
  dict(k="Klook",price=None,title="Huangpu River Night Cruise Experience",
       text="The night cruise on Klook. Check which pier the ticket is for before you book, because a ticket only works at its own pier (step 1 below).",
       url=KLOOK_CRUISE,cta="See the night cruise on Klook",
       qr="klook-huangpu-river-night-cruise-qr-code",qralt="QR code for the Klook Huangpu River night cruise page"),
  dict(k="GetYourGuide",price=None,title="Shanghai: night experience with city views and buffet dining",
       text="A Shanghai night out with city views and a buffet dinner, on GetYourGuide. Read what is included, the meeting point and the time for your date before you pay.",
       url=GYG_CRUISE,cta="See it on GetYourGuide",alt=True,
       qr="getyourguide-shanghai-night-buffet-dining-qr-code",qralt="QR code for the GetYourGuide Shanghai night experience page"),
 ],
}
OFFER_HEAD={
 "shanghai-circus-world-era-show":("Where we booked our tickets",
   "We booked ERA through Klook, and this is the link I use. The same show is on GetYourGuide too. Both are affiliate links: if you book through one, I earn a small commission and you pay the same price. Ticket prices change by date and zone, so check today's price on the page."),
 "huangpu-river-night-cruise":("Where to book the cruise",
   "Two places to book. Both are affiliate links: if you book through one, I earn a small commission and you pay the same price. Prices change by date and boat, so check today's price on the page."),
}
# guides that mention the cruise in passing and carry the same links inline (they show the affiliate note too)
AFF_INLINE={"the-bund-shanghai-at-night","nanjing-road-shanghai","huangpu-river-night-cruise","shanghai-circus-world-era-show"}
# GetYourGuide city widget (Shanghai = location 178), shown on the Shanghai guides. Script is in every page head (build.py).
GYG_WIDGET_SLUGS={"the-bund-shanghai-at-night","nanjing-road-shanghai","huangpu-river-night-cruise","shanghai-circus-world-era-show"}
GYG_SHANGHAI_WIDGET='<div data-gyg-href="https://widget.getyourguide.com/default/city.frame" data-gyg-location-id="178" data-gyg-locale-code="en-US" data-gyg-widget="city" data-gyg-partner-id="BKZ1KWD"></div>'
def offers_b(items, slug=None):
    cards=""
    for o in items:
        price=f'<div class="price">{html.escape(o["price"])}</div>' if o.get("price") else ''
        qr=(f'<figure class="qr"><img src="/img/{o["qr"]}.jpg" alt="{html.escape(o.get("qralt","QR code"))}" width="180" height="180" loading="lazy"><figcaption>On a computer? Scan this with your phone camera to open the same page.</figcaption></figure>') if o.get("qr") else ''
        cards+=(f'<div class="offer{" pick" if o.get("pick") else ""}{" alt" if o.get("alt") else ""}{" withqr" if qr else ""}">'
                f'{"<span class=\"badge\">"+html.escape(o.get("badge","What I booked"))+"</span>" if o.get("pick") else ""}'
                f'<div class="otext"><span class="k">{html.escape(o["k"])}</span>{price}<b>{html.escape(o["title"])}</b><p>{html.escape(o["text"])}</p>'
                f'<a class="btn" href="{o["url"]}" rel="sponsored noopener" target="_blank">{html.escape(o.get("cta","Check price on "+o["k"]))}</a>'
                f'<span class="via">Affiliate link: I earn a small commission if you book, at no extra cost to you.</span></div>{qr}</div>')
    h,t=OFFER_HEAD.get(slug,("Where to book","These are affiliate links: if you book through one, I earn a small commission and you pay the same price."))
    return f'<h2 id="book">{html.escape(h)}</h2><p>{html.escape(t)}</p><div class="offers">{cards}</div>'

def partner_b(key, SOC):
    p=PARTNERS[key]; n=html.escape(p["name"])
    qr=f'<figure class="pqr"><img src="/img/{p["qr"]}.jpg" alt="QR code that opens {n}" width="200" height="200"><figcaption>On a computer? Scan with your phone camera.</figcaption></figure>' if p.get("qr") else ''
    code=f'<span class="k">Use this code at checkout</span><div class="codebox" id="code"><span>{html.escape(p["code"])}</span><button type="button" data-copy="{html.escape(p["code"])}">Copy</button></div>' if p.get("code") else ''
    items=[(s_,o) for s_,lst in OFFERS.items() for o in lst if o["k"]==p["name"]]
    titles={"shanghai-circus-world-era-show":"Shanghai Circus World ERA show","huangpu-river-night-cruise":"Huangpu River night cruise"}
    cards="".join(f'<div class="offer{" pick" if o.get("pick") else ""}">{"<span class=\"badge\">"+html.escape(o.get("badge",""))+"</span>" if o.get("pick") else ""}<div class="otext"><span class="k">{html.escape(titles.get(s_,s_))}</span><b>{html.escape(o["title"])}</b><p>{html.escape(o["text"].replace(" in the steps below"," in my guide").replace(" (step 1 below)"," (my guide explains the piers)"))}</p><a class="btn" href="{o["url"]}" rel="sponsored noopener" target="_blank">{html.escape(o.get("cta","See it on "+n))}</a><span class="via"><a href="/guides/{s_}/">Read my guide first</a></span></div></div>' for s_,o in items)
    return f'''<main>
<section class="phero"><div class="wrap"><nav class="crumbs"><a href="/">Home</a><span>/</span><span>{n}</span></nav><p class="eyebrow">Travel deals</p><h1>{n}: my link, and what we booked</h1><p class="lede">We booked our ERA show tickets in Shanghai on {n}. This page has my {n} link, and the things on this site you can book there, each with the guide that explains it.</p></div></section>
<section class="pcode"><div class="wrap"><div class="plink"><div><h2>Open {n} with my link</h2><p>It opens the normal {n} site. If you book through it, I earn a small commission and you pay the same price.</p>{code}<div class="acts"><a class="btn" href="{p["url"]}" rel="sponsored noopener" target="_blank">Open {n}</a><a class="btn ghost" href="/china/">See the China guides</a></div><small>Affiliate link. <a href="/affiliate-disclosure/">How affiliate links work on this site</a>.</small></div>{qr}</div></div></section>
<section class="sec mint"><div class="wrap"><div class="sechead left"><div><h2>On {n}, from my guides</h2><p>Each card says whether we booked it ourselves. Read the guide first: it has the pier, the zone, the times and the things to check.</p></div></div><div class="offers">{cards}</div></div></section>
{band_b(SOC)}
</main>'''

def disclosure_b(SOC):
    return f'''<main>
<section class="phero"><div class="wrap"><nav class="crumbs"><a href="/">Home</a><span>/</span><span>Affiliate disclosure</span></nav><p class="eyebrow">Affiliate disclosure</p><h1>How affiliate links work on this site</h1><p class="lede">Some links on Scratch &amp; Roam are affiliate links. Here is what that means for you, in plain words.</p></div></section>
<section class="sec" style="padding-top:10px"><div class="wrap"><article class="art" style="max-width:720px">
<h2 style="margin-top:0">What an affiliate link is</h2><p>When you book through one of my affiliate links, the booking site pays me a small commission. You pay the same price as you would going to the site yourself. It is one of the ways I keep the guides free to read.</p>
<h2>Which links are affiliate links</h2><p>Links to Klook, GetYourGuide, Tiqets, Airalo, Yesim, Saily, Welcome Pickups, GetTransfer and Kiwi.com on this site are affiliate links.</p><p>On the Travel deals page, a card marked "I use this" is something I use myself, and "We booked here" means we booked through it. Every guide that has them says so at the top, next to the date it was checked, and again next to the links. Guides with no affiliate links say "Nothing here is sponsored".</p><p>Some Shanghai guides also show a box of Shanghai tours from GetYourGuide. Those are affiliate links too, and I have not done every tour in that box, so read the details before you book.</p>
<h2>Amazon</h2><p>As an Amazon Associate I earn from qualifying purchases. Some guides link to Amazon for things the guide tells you to pack. In Ireland the links open Amazon.ie. Everywhere else they open Amazon.com, which sends you on to your own country's Amazon store if there is one.</p>\n<h2>Referral codes</h2><p>Some cards on the Travel deals page have a referral code instead of an affiliate link. With the Firsty code, for example, you get €3 off your first purchase over €4 and I get €3 credit in my app.</p>
<h2>What we booked ourselves</h2><p>When we booked something ourselves, the card says so, for example "Where we booked" on the ERA show tickets. When a card does not say that, it is an option I am sharing, not something we have tried.</p>
<h2>What it does not change</h2><p>No company pays me to write a guide or to say good things. The steps, the prices and the rules in each guide come from our own trips and from the sources listed at the bottom of each page, with the date I checked them.</p>
<h2>Tracking</h2><p>To count bookings that come from my links, pages on this site load small scripts from GetYourGuide and Travelpayouts (the network that runs most of my partner links). They are used to match a booking to my link.</p>
<h2>Questions</h2><p>Email me at <b>scratchandroam@gmail.com</b>. All my partner links are on the <a href="/travel-deals/">Travel deals</a> page, and what we booked on Klook is on the <a href="/klook/">Klook page</a>.</p>
</article></div></section>
</main>'''

COPYJS='<script>document.addEventListener("click",function(e){var b=e.target.closest("[data-copy]");if(!b)return;var t=b.getAttribute("data-copy");(navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(function(){b.textContent="Copied"},function(){var r=document.createRange();r.selectNodeContents(b.previousElementSibling);var s=getSelection();s.removeAllRanges();s.addRange(r)});});document.addEventListener("click",function(e){var l=e.target.closest(".lite");if(!l||l.querySelector("iframe"))return;var f=document.createElement("iframe");f.src="https://www.youtube-nocookie.com/embed/"+l.getAttribute("data-id")+"?autoplay=1";f.allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture";f.allowFullscreen=true;l.appendChild(f);});</script>'

# ===== where I've been =====
VIDEOS=[("33pgztdZT8Q","China arrival card on a PC, step by step","Video + steps · 3:41"),("YDdwz1ChMFE","China arrival card in Alipay on your phone","Video + steps · 3:20"),("TuP9NS00Ugg","First time in China: 13 things before you fly","Video + checklist · 6 min")]
def where_b(*, CARDS, SOC, n_guides):
    vids="".join(f'<a class="vid" href="https://www.youtube.com/watch?v={v}" rel="noopener"><div class="thumb"><img src="https://i.ytimg.com/vi/{v}/hqdefault.jpg" alt="" loading="lazy"><div class="play"><span>&#9654;</span></div></div><div class="in"><span class="k">YouTube</span><h3>{html.escape(t)}</h3><small>{m}</small></div></a>' for v,t,m in VIDEOS)
    def visit(i,l,v): return f'<div>{IC[i]}<span><small>{l}</small>{v}</span></div>'
    def cc(img,flag,name,trips,days,desc,explore,count,first,last,soon=False):
        return f'''<article class="cc{" soon" if soon else ""}"><div class="top"><img src="/img/{img}.jpg" alt=""><span class="flag">{flag}</span><h2>{name}</h2><div class="pills"><span>{IC["plane"]}{trips}</span><span>{IC["pin"]}{days}</span></div></div><div class="body"><p>{desc}</p><a class="explore" href="{explore[1]}">{IC["book"]} {explore[0]} <span>→</span></a><div class="count"><b>{count[0]}</b>{count[1]}</div></div><div class="visits">{visit("cal","First visit",first)}{visit("plane","Last visit",last)}</div></article>'''
    cards=cc("the-bund-pink-lit-pearl-tower-over-the-crowd","🇨🇳","China","2 trips","Christmas + Easter","Our first trip was Christmas 2025 in Shanghai, with Disneyland, then New Year on the Bund. We went back for Easter 2026, fully prepared this time. Every guide on this site so far comes from those two trips.",("Explore China","/china/"),(str(n_guides),"guides"),"Dec 2025","Apr 2026")
    cards+=cc("huangpu-river-pudong-skyline-with-gold-reflections","🇨🇳","Chengdu, Chongqing, Xi'an","Trip 2","Dec 2026","The next trip: three cities by high-speed train, the metro cards in each, the pandas, and the food. Guides go up as I check each one.",("Follow the trip",SOC["YouTube"]),("0","guides yet"),"Dec 2026","Coming",True)
    cards+=cc("the-bund-peace-hotel-green-roofs-lit-at-night","🇯🇵","Japan","Next","Planning","Japan is the next country on the list. Subscribe and the first guide lands in your feed.",("Subscribe",SOC["YouTube"]+"?sub_confirmation=1"),("0","guides yet"),"Soon","Soon",True)
    return f'''<main>
<section class="whero"><img src="/img/the-bund-pudong-skyline-and-shanghai-tower-at-night.jpg" alt=""><div class="wrap"><nav class="crumbs"><a href="/">Home</a><span>/</span><span>Where I've been</span></nav><p class="eyebrow">Where I've been</p><h1>Where I've been</h1><p class="lede">Two trips to China so far, three new cities in December, and the list grows from there.</p></div></section>
<section class="sec"><div class="wrap"><div class="countries">{cards}</div></div></section>
<section class="sec mint"><div class="wrap"><div class="sechead left"><div><p class="eyebrow">Watch</p><h2>The videos behind the guides</h2><p>Each video has a written guide with the same steps and the screenshots, so you can follow along without pausing.</p></div><a class="more" href="{SOC['YouTube']}" rel="noopener">All videos →</a></div><div class="vids">{vids}</div></div></section>
<section class="sec"><div class="wrap"><div class="sechead left"><div><h2>Watch it in the page</h2><p>Option two: the video plays right here. The thumbnail loads first, the player only when you tap it, so the page stays fast.</p></div></div><div class="lite" data-id="33pgztdZT8Q" role="button" tabindex="0" aria-label="Play: China arrival card on a PC"><img src="https://i.ytimg.com/vi/33pgztdZT8Q/maxresdefault.jpg" alt=""><div class="play"><span>&#9654;</span></div></div></div></section>
<section class="sec mint" style="padding-top:0"><div class="wrap"><div class="sechead left" style="padding-top:48px"><div><p class="eyebrow">Shorts</p><h2>The short versions</h2><p>Option three: vertical covers that open the reel on TikTok or Instagram. No third-party script on the page, so nothing slows down or gets blocked.</p></div></div><div class="tt"><a href="{SOC['TikTok']}" rel="noopener"><img src="/img/the-bund-shanghai-after-dark-cover-4x5.jpg" alt=""><i>TikTok</i><span>The Bund after dark, in 30 seconds</span></a><a href="{SOC['Instagram']}" rel="noopener"><img src="/img/nanjing-road-shanghai-neon-shop-fronts-cover-4x5.jpg" alt=""><i>Reel</i><span>Nanjing Road when the neon comes on</span></a><a href="{SOC['TikTok']}" rel="noopener"><img src="/img/huangpu-river-night-cruise-from-the-water-cover-4x5.jpg" alt=""><i>TikTok</i><span>The river cruise, which pier</span></a><a href="{SOC['Instagram']}" rel="noopener"><img src="/img/shanghai-circus-world-full-show-cover.jpg" alt=""><i>Reel</i><span>ERA show at Shanghai Circus World</span></a></div></div></section>
{social_b(SOC,"the-bund-pudong-skyline-and-shanghai-tower-at-night","nanjing-road-curved-corner-building-neon-lights")}
</main>'''

# ===== about =====
def about_b(*, SOC, n_guides):
    method=[("Film the real screens and the real streets","The actual arrival card form, the actual metro exit. No stock footage."),("Check every rule against the official page","Visa lists, fees, opening hours. Official sources are marked on each guide."),("Write the steps so they work without sound","Each step heading is the thing you would type into a search box."),("Date it, and recheck it","When a rule changes, the guide gets updated, not left to go stale.")]
    mh="".join(f'<li><div class="n">{i+1}</div><div><h3>{html.escape(t)}</h3><p>{html.escape(d)}</p></div></li>' for i,(t,d) in enumerate(method))
    socs=[("YouTube","Full guides and long videos"),("TikTok","The short versions and photo carousels"),("Instagram","Reels and facts carousels"),("Pinterest","Carousels and covers to save"),("Facebook","Everything, a day later")]
    sh="".join(f'<a class="gc" href="{SOC[n]}" rel="me noopener"><div class="in"><span class="cat">{n}</span><h3>{d}</h3><small>@scratchandroam</small></div></a>' for n,d in socs)
    return f'''<main>
<section class="hhero"><div class="wrap"><div><nav class="crumbs"><a href="/">Home</a><span>/</span><span>About</span></nav><p class="eyebrow">About</p><h1>A maker from Ireland who travels with a camera</h1><p class="lede">I am Natali. I make things for a living and film the trips in between: Shanghai so far, Chengdu, Chongqing and Xi'an in December, Japan after that. The guides on this site are the parts I wish someone had written down for me before my first trip.</p><div class="acts"><a class="btn" href="/china/">Read the China guides</a><a class="btn ghost" href="{SOC['YouTube']}?sub_confirmation=1" rel="noopener">Subscribe on YouTube</a></div></div>
<div class="collage"><figure><img src="/img/natali-portrait-at-her-desk.jpg" alt="Natali at her desk"><figcaption>me, in the studio</figcaption></figure><figure><img src="/img/the-bund-gold-lit-historic-buildings-at-night.jpg" alt=""><figcaption>the Bund, late</figcaption></figure></div></div></section>
{stats_b(n_guides,"A bit about me.")}
<section class="sec"><div class="wrap"><div class="cols about2"><article class="art"><h2 style="margin-top:0">Making things by day, filming by night</h2><p>I have a background in graphic design and I run a small studio in Ireland. Travel is the thing I do with the time in between, and the camera comes along because I want to remember the practical bits as much as the views: which exit, which pier, what it cost.</p><p>My husband and family turn up in the videos sometimes, and so does the work on the days I am not travelling.</p><p>Nothing here is sponsored by a brand. If a rule or a price is on a page, I checked it on the date written next to it.</p>
<h2 id="idea">Why a scratch card?</h2><p>A place stays hidden until you scratch it, and then it is all there. Every video opens that way: the name of the place under silver foil, a coin, and then the real thing. On the site a city gets scratched off once we have actually been, so the foil over Chengdu, Chongqing and Xi'an comes off in December.</p><p>It is also a reminder of how I like to travel: not knowing everything in advance, but having the practical parts sorted so the rest can be a surprise.</p>
<h2 id="method">How a guide gets made</h2><ol class="steps">{mh}</ol>
<h2 id="affiliates">How the affiliate links work</h2><p>Some guides link to booking sites such as Klook and GetYourGuide. If you book through one of those links I earn a small commission and you pay the same price. Those links are marked, they never change what I recommend, and a guide with none of them says "nothing here is sponsored" at the top.</p>
</article><aside class="side"><div class="scard me"><img src="/img/natali-portrait-at-her-desk.jpg" alt=""><h3>Say hello</h3><p>Questions about a trip, or a place you want covered? Email is best. I read everything, and the guides often start with a question someone sent.</p><p><b>scratchandroam@gmail.com</b></p><a href="/china/">Start with the guides →</a></div><div class="scard"><span class="eyebrow">Handle everywhere</span><div class="cloud">{"".join(f'<a href="{u}" rel="me noopener">{n}</a>' for n,u in SOC.items())}</div></div></aside></div></div></section>
<section class="sec mint"><div class="wrap"><div class="sechead left"><div><p class="eyebrow">Follow along</p><h2>Same trips, different lengths</h2><p>Long videos on YouTube, the short versions on TikTok, carousels to save on Pinterest.</p></div></div><div class="gcards sm">{sh}</div></div></section>
{band_b(SOC)}
</main>'''

# ===== china index =====
def china_b(*, CARDS, SOC, QCARDS, QS_CHINA, n_guides):
    def gcard(c,small=False):
        return f'<a class="gc" href="/guides/{c["slug"]}/"><img src="/img/{c["img"]}.jpg" alt="{html.escape(c["alt"])}" loading="lazy"><div class="in"><span class="cat">{html.escape(c["meta"][0] if c.get("meta") else "Place guide")}</span><h3>{html.escape(c.get("t") or c["short"])}</h3>{"" if small else f"<p>{html.escape(c.get(chr(112)) or chr(32))}</p>"}<small>{html.escape(c["meta"][1] if c.get("meta") else "Shanghai")}</small></div></a>'
    qs="".join(f'<a class="gc" href="/guides/{QCARDS[k][3]}/"><div class="in"><span class="cat">{html.escape(QCARDS[k][0])}</span><h3>{html.escape(QCARDS[k][1])}</h3><small>{html.escape(QCARDS[k][2])}</small></div></a>' for k in QS_CHINA)
    before=[c for c in CARDS if c["sec"]=="before"]; shop=[c for c in CARDS if c["sec"]=="shop"]; places=[c for c in CARDS if c["sec"]=="place"]
    return f'''<main>
<section class="whero"><img src="/img/the-bund-pudong-skyline-and-shanghai-tower-at-night.jpg" alt=""><div class="wrap"><nav class="crumbs"><a href="/">Home</a><span>/</span><span>China</span></nav><p class="eyebrow">China guides</p><h1>China guides for first-timers: entry, paying, trains</h1><p class="lede">The practical part first, in the order you will need it: before you fly, at the border, then paying and getting around. Shanghai is filmed and written up; Chengdu, Chongqing and Xi'an land after December.</p></div></section>
<section class="sec" style="padding-top:40px"><div class="wrap"><div class="sechead left"><div><h2>Pick the thing you need to sort out</h2></div></div><div class="gcards sm">{qs}</div></div></section>
<section class="sec mint" id="before"><div class="wrap"><div class="sechead left"><div><p class="eyebrow">Before you fly</p><h2>The setup guides</h2><p>Each one is the video plus the written steps, checked against the official page on the date shown.</p></div></div><div class="gcards">{"".join(gcard(c) for c in before)}</div></div></section>
<section class="sec" id="shopping"><div class="wrap"><div class="sechead left"><div><p class="eyebrow">Once you are there</p><h2>Shopping, ordering and paying</h2><p>The things you do on your phone in China once the basics are set up, step by step, with the real screens.</p></div></div><div class="gcards">{"".join(gcard(c) for c in shop)}</div></div></section>
<section class="sec mint" id="shanghai"><div class="wrap"><div class="sechead left"><div><p class="eyebrow">Shanghai, answered</p><h2>What we filmed, turned into the practical answers</h2><p>Four place guides from the trip, mostly at night: how to get there, when to go, what it costs.</p></div><a class="more" href="{SOC['YouTube']}" rel="noopener">All videos →</a></div><div class="gcards sm">{"".join(gcard(c,True) for c in places)}</div></div></section>
<section class="sec" id="december"><div class="wrap"><div class="sechead"><p class="eyebrow">Still under the foil</p><h2>December: Chengdu, Chongqing, Xi'an</h2><p>Pandas, hotpot, a metro that runs through a building, and the Terracotta Army. The guides from this trip land here first, then the videos.</p><a class="btn" style="margin-top:18px" href="{SOC['YouTube']}?sub_confirmation=1" rel="noopener">Subscribe to catch them</a></div></div></section>
{band_b(SOC)}
</main>'''

# ===== travel deals (all partner links in one place) =====
# Only links Natali gave. Descriptions say what the company does; "booked" only where she said she booked.
DEALS=[
 dict(cat="Tours and tickets",name="Klook",url="https://klook.tpm.li/jfysgwVe",qr="klook-scratch-and-roam-link-qr-code",booked=True,
      text="Tickets for attractions, shows, tours and day trips, with a lot of choice in Asia. We booked our ERA show tickets in Shanghai here.",more=("/klook/","What we booked on Klook")),
 dict(cat="Tours and tickets",name="Tiqets",url="https://tiqets.tpm.li/nIjCsWXe",qr="tiqets-travel-deal-link-qr-code",
      text="Tickets for museums and attractions. The link opens Tiqets on a city page; switch the city at the top of their site."),
 dict(cat="eSIM and data",name="Firsty",url="https://www.firsty.app/",used=True,code="6TKZ-8RGM",codenote="Referral code: you get €3 off your first purchase over €4, and I get €3 credit.",
      text="The eSIM I use myself. I used Firsty in Japan and in Saudi Arabia with no problems, and I plan to use it in China too. Before China, check in the app how it handles Google and WhatsApp there."),
 dict(cat="eSIM and data",name="Airalo",url="https://airalo.tpm.li/2QR6sBuX",qr="airalo-travel-deal-link-qr-code",
      text="eSIM data plans for travel, bought and installed in an app. The link opens the Airalo app in the App Store."),
 dict(cat="eSIM and data",name="Yesim",url="https://yesim.tpm.li/AfoDqUbw",qr="yesim-travel-deal-link-qr-code",
      text="eSIM data plans for travel, for one country or a region."),
 dict(cat="eSIM and data",name="Saily",url="https://saily.tpm.li/r3wbWW2R",
      text="eSIM data plans for travel, from Nord Security, the company behind NordVPN."),
 dict(cat="Packing and gear",name="Amazon",url="/go/amazon",
      text="Travel adapters, packing cubes, carry-on bags and the other things my guides tell you to pack. As an Amazon Associate I earn from qualifying purchases."),
 dict(cat="Airport transfers",name="Welcome Pickups",url="https://tpm.li/IwbyltvW",qr="welcome-pickups-travel-deal-link-qr-code",
      text="Pre-booked airport and city transfers with a driver who meets you on arrival."),
 dict(cat="Airport transfers",name="GetTransfer",url="https://gettransfer.tpm.li/G1nHwTwh",
      text="Book a transfer or ride by entering your route, then pick from the offers drivers and companies send you."),
 dict(cat="Flights",name="Kiwi.com",url="https://kiwi.tpm.li/hGsxQiah",qr="kiwi-travel-deal-link-qr-code",
      text="Flight search and booking, including routes that combine different airlines. The link opens a sample route page; type your own route."),
]
def deals_b(SOC):
    cats=[]
    for d in DEALS:
        if d["cat"] not in cats: cats.append(d["cat"])
    chips='<button type="button" class="chip on" data-f="all">All</button>'+"".join(f'<button type="button" class="chip" data-f="{html.escape(c)}">{html.escape(c)}</button>' for c in cats)
    cards=""
    for d in DEALS:
        qr=f'<img class="dqr" src="/img/{d["qr"]}.jpg" alt="QR code for {html.escape(d["name"])}" width="110" height="110" loading="lazy">' if d.get("qr") else ''
        badge='<span class="dbadge booked">We booked here</span>' if d.get("booked") else ('<span class="dbadge booked">I use this</span>' if d.get("used") else '<span class="dbadge">Link only</span>')
        more=f'<a class="dmore" href="{d["more"][0]}">{html.escape(d["more"][1])} →</a>' if d.get("more") else ''
        cards+=f'''<article class="deal" data-cat="{html.escape(d["cat"])}"><div class="dtop"><div><span class="dcat">{html.escape(d["cat"])}</span><h3>{html.escape(d["name"])}</h3>{badge}</div>{qr}</div><p>{html.escape(d["text"])}</p>{('<div class="dcode has"><span>Code</span><b>'+html.escape(d["code"])+'</b><button type="button" data-copy="'+html.escape(d["code"])+'">Copy</button></div><small class="dcn">'+html.escape(d.get("codenote",""))+'</small>') if d.get("code") else '<div class="dcode"><span>Code</span><b>No code needed</b></div>'}<div class="dact"><a class="btn" href="{d["url"]}" rel="{"noopener" if d.get("code") and "tpm.li" not in d["url"] else "sponsored noopener"}" target="_blank">Open {html.escape(d["name"])}</a>{more}</div></article>'''
    return f'''<main>
<section class="phero"><div class="wrap"><nav class="crumbs"><a href="/">Home</a><span>/</span><span>Travel deals</span></nav><p class="eyebrow">Travel deals</p><h1>My travel links, all in one place</h1><p class="lede">Tickets, eSIMs, airport transfers and flights. These are my partner links: if you book through one, I earn a small commission and you pay the same price. Each card says whether we booked there or I use it myself.</p></div></section>
<section class="sec" style="padding-top:8px"><div class="wrap">
<div class="dnote"><b>Before you click</b><p>Where I have a code, it is on the card with a Copy button. For China, read my <a href="/guides/china-travel-apps/">China travel apps guide</a> before you buy an eSIM: check that the plan routes data outside China, or Google and WhatsApp will not work. <a href="/affiliate-disclosure/">How affiliate links work on this site</a>.</p></div>
<div class="chips" role="group" aria-label="Filter by category">{chips}</div>
<div class="deals" id="deals">{cards}</div>
</div></section>
{band_b(SOC)}
</main>
<script>(function(){{var b=document.querySelectorAll(".chips .chip"),c=document.querySelectorAll(".deal");b.forEach(function(x){{x.addEventListener("click",function(){{b.forEach(function(y){{y.classList.toggle("on",y===x)}});var f=x.getAttribute("data-f");c.forEach(function(d){{d.hidden=!(f==="all"||d.getAttribute("data-cat")===f)}})}})}})}})();</script>'''


# ===== "Links for this guide" boxes (partner links that fit the guide's topic) =====
GUIDE_DEALS={
 "china-travel-apps":(["Firsty","Airalo","Yesim","Saily"],"eSIMs for step 8. Whichever you pick, read the plan description first: for China you want one that routes data outside China, so Google and WhatsApp keep working."),
 "top-25-china-apps":(["Firsty","Airalo","Yesim","Saily"],"eSIMs for pass number 4. For China, read the plan description first: you want one that routes data outside China."),
 "first-time-in-china":(["Firsty","Airalo","Kiwi.com","Welcome Pickups","GetTransfer"],"An eSIM for the internet on landing, flights, and a transfer from the airport so the first hour is easy."),
 "china-before-you-fly-checklist":(["Firsty","Airalo","Welcome Pickups","GetTransfer"],"An eSIM for step 4, and an airport transfer for step 10, so your first day stays simple."),
 "china-visa-free-30-days":(["Kiwi.com"],"Flights for a trip that fits inside the 30 days and before 31 December 2026."),
}
def guide_deals_b(slug):
    names,note=GUIDE_DEALS[slug]
    by={d["name"]:d for d in DEALS}
    cards=""
    for n in names:
        d=by[n]
        badge='<span class="dbadge booked">I use this</span>' if d.get("used") else ('<span class="dbadge booked">We booked here</span>' if d.get("booked") else '<span class="dbadge">Link only</span>')
        code=(f'<div class="dcode has"><span>Code</span><b>{html.escape(d["code"])}</b><button type="button" data-copy="{html.escape(d["code"])}">Copy</button></div><small class="dcn">{html.escape(d.get("codenote",""))}</small>') if d.get("code") else ''
        rel="noopener" if d.get("code") and "tpm.li" not in d["url"] else "sponsored noopener"
        cards+=f'<div class="gdeal"><div class="gdh"><span class="dcat">{html.escape(d["cat"])}</span><b>{html.escape(d["name"])}</b>{badge}</div><p>{html.escape(d["text"])}</p>{code}<a class="btn" href="{d["url"]}" rel="{rel}" target="_blank">Open {html.escape(d["name"])}</a></div>'
    return (f'<h2 id="links">Links for this guide</h2><p>{html.escape(note)} These are my partner links: if you book through one, I earn a small commission and you pay the same price. '
            f'All of them are on my <a href="/travel-deals/">Travel deals</a> page.</p><div class="gdeals">{cards}</div>')


# ===== Amazon (Amazon.ie Associates, tracking id scratchandroa-21) =====
AMZ_TAG="scratchandroa-21"
AMZ_LINE="As an Amazon Associate I earn from qualifying purchases."
def amz(q): return "/go/amazon?k="+q.replace(" ","+")  # src/worker.js: IE -> amazon.ie -21, others -> amazon.com -20 + OneLink
# Only items the guide itself tells people to pack or use. Search links, so readers pick the product.
AMAZON={
 "china-dos-and-donts":("Things from this list to pack",[("Travel plug adapter for China","Number 12. A UK to China adapter, or a universal one that covers Type A and Type I sockets.","uk to china travel adapter"),
   ("Travel hand sanitiser","Number 14. Many public toilets have no soap.","travel hand sanitiser"),
   ("Travel-size toiletries","Number 13. Your own deodorant and SPF in travel sizes.","travel size toiletries bottles")]),
 "china-before-you-fly-checklist":("Things from this checklist to pack",[("Travel first aid kit","Step 8: a tiny medical kit with plasters and the basics. Add your own medicines.","travel first aid kit small"),
   ("Passport and document holder","Step 6: keep your passport and copies together.","passport holder travel wallet")]),
 "first-time-in-china":("Packing light",[("Carry-on backpack","Step 13: one bag you can lift makes stations and metros easier.","carry on travel backpack"),
   ("Packing cubes","Keeps one bag tidy on a trip with lots of hotel changes.","packing cubes")]),
 "build-spice-tolerance-before-china":("Things for the 6 week plan",[("Sriracha","Week 3: a sriracha-level sauce on whole meals.","sriracha sauce"),
   ("Chilli crisp","Week 4: heat that comes in oil, closer to Sichuan food.","chilli crisp"),
   ("Sichuan peppercorns","Week 5: the numbing half of mala. Start with a tiny pinch.","sichuan peppercorns")]),
}
def amazon_b(slug):
    title,items=AMAZON[slug]
    cards="".join(f'<div class="amz"><b>{html.escape(n)}</b><p>{html.escape(t)}</p><a class="btn alt2" href="{amz(q)}" rel="sponsored nofollow noopener" target="_blank">See on Amazon</a></div>' for n,t,q in items)
    return f'<h2 id="amazon">{html.escape(title)}</h2><p>These open a search on Amazon in your country, so you can pick the one that suits you. {AMZ_LINE}</p><div class="amzs">{cards}</div>'
