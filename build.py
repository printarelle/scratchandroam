import re
import os, json, datetime, html
SITE="https://scratchandroam.com"
import sys; sys.path.insert(0,"src")
from images import R as IMGREG, OGALT
import struct
def _size(p):
    # image width and height without Pillow (the Cloudflare build has no Pillow)
    d=open(p,"rb").read()
    if d[:8]==b"\x89PNG\r\n\x1a\n": return struct.unpack(">II",d[16:24])
    i=2
    while i<len(d):
        if d[i]!=0xFF: i+=1; continue
        m=d[i+1]
        if m in (0xC0,0xC1,0xC2): h,w=struct.unpack(">HH",d[i+5:i+9]); return w,h
        i+=2+struct.unpack(">H",d[i+2:i+4])[0]
    raise SystemExit("cannot read size of "+p)
TODAY="2026-10-15"
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Mr+Dafoe&family=Caveat:wght@700&family=Archivo+Black&family=Special+Elite&family=Libre+Franklin:ital,wght@0,400;0,500;0,700;1,400&display=swap">'
CSS=open('src/site.css').read()
SOC={"YouTube":"https://www.youtube.com/@scratchandroam","Instagram":"https://www.instagram.com/scratchandroam/","TikTok":"https://www.tiktok.com/@scratchandroam","Facebook":"https://www.facebook.com/scratchandroam","Pinterest":"https://www.pinterest.com/scratchandroam/"}
SAMEAS=json.dumps(list(SOC.values()))

def nav(dark=False):
    return f'''<header class="hdr{' dark' if dark else ''}"><nav class="nav wrap"><a class="logo" href="/" aria-label="Scratch and Roam with Natali, home"><span class="mark">Scratch <em>&amp;</em> Roam</span><span class="with">with Natali</span></a>
<button class="menu-btn" id="menuBtn" aria-expanded="false" aria-controls="menu">Menu</button>
<div class="links" id="menu"><a href="/china/">China guides</a>{NAV_SHOP()}<a href="/#shanghai">Shanghai</a><a href="/#december">December trip</a><a href="/about/">About</a><a class="yt" href="{SOC['YouTube']}?sub_confirmation=1" rel="me noopener">Subscribe</a></div></nav></header>'''
def NAV_SHOP():
    # "Shopping" menu link appears automatically once any guide is registered with sec="shop"
    return '<a href="/china/#shopping">Shopping</a>' if any(c["sec"]=="shop" for c in globals().get("CARDS",[])) else ''
def FOOT_GUIDES():
    return "".join(f'<a href="/guides/{c["slug"]}/">{html.escape(c["short"])}</a>' for c in globals().get("CARDS",[]))
NAVJS='<script>(function(){var b=document.getElementById("menuBtn"),m=document.getElementById("menu");if(!b)return;b.addEventListener("click",function(){var o=m.classList.toggle("open");b.setAttribute("aria-expanded",o?"true":"false");});})();</script>'
def footer():
    links="".join(f'<a href="{u}" rel="me noopener">{n}</a>' for n,u in SOC.items())
    return f'''<footer><div class="wrap"><div class="in"><div><a class="logo" href="/"><span class="mark">Scratch <em>&amp;</em> Roam</span><span class="with">with Natali</span></a><p class="tag">Scratch to reveal. Roam to discover.</p><p style="margin-top:10px;max-width:46ch">Travel guides and videos from a maker in Ireland. First-timer China now, Japan and the next trip after that.</p></div><div><p class="eyebrow" style="color:#9a93a3">Guides</p><div class="fg">{FOOT_GUIDES()}</div></div><div><p class="eyebrow" style="color:#9a93a3">Follow along</p><div class="follow">{links}</div></div></div><div class="fine"><span>© 2026 Scratch &amp; Roam with Natali, Ireland</span><span>scratchandroam@gmail.com</span></div></div></footer>{NAVJS}'''

def page(path,title,desc,body,schema=None,og_image=None,extra_head="",dark=False,published=None,modified=None):
    url=SITE+path
    img=og_image or SITE+"/og/shanghai-circus-world-photo-dump.jpg"
    ART_META=(f'<meta property="article:published_time" content="{published}">\n' if published else "")+(f'<meta property="article:modified_time" content="{modified}">\n' if modified else "")
    sj="".join(f'<script type="application/ld+json">{json.dumps(s,ensure_ascii=False)}</script>' for s in (schema or []))
    doc=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{'article' if path.startswith('/guides/') else 'website'}">
<meta property="og:site_name" content="Scratch &amp; Roam with Natali">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{html.escape(OGALT.get(img.rsplit('/',1)[-1],title))}">
{ART_META}<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{img}">
<meta name="twitter:image:alt" content="{html.escape(OGALT.get(img.rsplit('/',1)[-1],title))}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
{FONTS}
{extra_head}
<style>{CSS}</style>
{sj}
</head>
<body>
{nav(dark)}
{body}
{footer()}
</body>
</html>'''
    doc=finish_images(doc,path,img)
    out="docs"+path+("index.html" if path.endswith("/") else "")
    os.makedirs(os.path.dirname(out),exist_ok=True)
    open(out,"w").write(doc)
    PAGES.append((path,TODAY))

BAD_NAME=re.compile(r"^(img|image|pic|photo|dsc|screenshot|untitled|copy)[-_ ]?\d*$|^[a-z]{0,3}[-_]?\d+$|-(s\d{1,2}|slide-?\d{1,2})$|^(taobao|bund|river|nanjing|circus|dd)-\d")
PAGEIMGS={}
USED=set()
def finish_images(doc,path,og):
    """Image rules, checked on every build (the build stops on a mistake):
    file name descriptive, listed in src/images.py with a true alt, alt 15-160 chars, width and height set,
    lazy loading except the hero (data-hero), decoding async. Empty alt only for a picture that sits next to its own caption."""
    urls=[og]
    def fix(m):
        t=m.group(0)
        src=re.search(r'src="([^"]*)"',t).group(1)
        if not src.startswith("/img/"):
            raise SystemExit(f"{path}: image outside /img/: {src}")
        key=src[5:]; USED.add(key)
        stem=os.path.splitext(os.path.basename(key))[0]
        assert os.path.exists("docs/img/"+key), f"{path}: missing file {src}"
        assert not BAD_NAME.search(stem) and stem.count("-")>=2, f"{path}: image name {key!r} is not descriptive (say what the picture shows, 3+ words)"
        assert key in IMGREG, f"{path}: {key} is not in src/images.py (add its alt text)"
        am=re.search(r'\salt="([^"]*)"',t)
        decor = am is not None and am.group(1)=="" and doc[m.end():m.end()+30].startswith(('<div class="cap">','</div><div class="cap">'))
        alt=IMGREG[key]["alt"]
        assert 15<=len(alt)<=200 and not re.search(r"\b(image|picture|photo|pic) of\b|\.(jpg|png)$",alt,re.I), f"{key}: weak alt {alt!r}"
        t=re.sub(r'\salt="[^"]*"','',t)
        t=t[:-1].rstrip(" /")+(' alt=""' if decor else f' alt="{html.escape(alt,quote=True)}"')
        if "width=" not in t:
            w,h=_size("docs/img/"+key); t+=f' width="{w}" height="{h}"'
        hero="data-hero" in t
        t=t.replace(" data-hero","").replace("data-hero","")
        t=re.sub(r'\sloading="[^"]*"','',t)
        t+=' fetchpriority="high"' if hero else ' loading="lazy"'
        t+=' decoding="async">'
        urls.append(SITE+src)
        return t
    doc=re.sub(r"<img\b[^>]*>",fix,doc)
    PAGEIMGS[path]=list(dict.fromkeys(urls))
    return doc
PAGES=[]

def yt(vid,title,start=None):
    if not vid:
        return f'<div class="video soon" style="background-image:url(/img/first-time-in-china-13-things-before-you-fly.jpg)"><div><b>Video goes live on YouTube on Friday 16 October</b><br><small>This page will embed it as soon as it is up.</small></div></div>'
    return f'''<div class="video"><iframe src="https://www.youtube-nocookie.com/embed/{vid}{"?start="+str(start) if start else ""}" title="{html.escape(title)}" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>'''

def guide(slug,title,h1,desc,keyword,vid,intro,steps,faq,sources,og,chapters=None,related=None,checked=TODAY,minutes=None,upload=None,gallery=None,place=None,steps_title='Step by step',shorts=None,start=None,vschema=True,video_note=None,extra=None,lift=None,head="",published=None,og_alt=None):
    assert slug in globals().get("CARD_SLUGS",set()), f"guide {slug!r} is not in CARDS (src/content.py): add it so it shows on the home page, /china/, the menu and the footer"
    path=f"/guides/{slug}/"
    url=SITE+path
    def _figs(keys):
        if not keys: return ""
        return '<div class="shots">'+"".join(f'<figure><a href="/img/{k}.jpg"><img src="/img/{k}.jpg" alt=""></a><figcaption>{html.escape(IMGREG[k+".jpg"]["cap"])}</figcaption></figure>' for k in keys)+'</div><p class="shotnote">Screenshots from my own phone. The app is in Chinese, the English labels are mine. Tap a picture to open it larger.</p>'
    steps_html="".join(f'<li id="step-{i+1}"><div class="n">{i+1}</div><div><h3>{html.escape(s[0])}</h3><p>{s[1]}</p>{_figs(s[2] if len(s)>2 else None)}</div></li>' for i,s in enumerate(steps))
    faq_html="".join(f'<details{" open" if i==0 else ""}><summary>{html.escape(q)}</summary><p>{a}</p></details>' for i,(q,a) in enumerate(faq))
    src_html="".join(f'<li><a href="{u}" rel="noopener">{html.escape(n)}</a>{" (official)" if off else ""}</li>' for n,u,off in sources)
    ch_html=""
    if chapters:
        ch_html='<div class="chapters"><h3>In the video</h3><ol>'+"".join(f'<li><span>{t}</span>{html.escape(c)}</li>' for t,c in chapters)+'</ol></div>'
    rel_html=""
    if related:
        rel_html='<section class="related"><h2>Related guides</h2><div class="tickets">'+"".join(f'<a class="tk" href="{u}"><img src="/img/{cl}.jpg" alt="{html.escape(n)} cover" loading="lazy"><span class="num">{html.escape(t)}</span><div class="cb"><h3>{html.escape(n)}</h3><span class="go">Read the guide</span></div></a>' for u,cl,t,n in related)+'</div></section>'
    gal=""
    if gallery:
        gal='<div class="gal">'+"".join(f'<figure><img src="/img/{g[0]}.jpg" alt=""{" data-hero" if i==0 else ""}><figcaption>{html.escape(IMGREG[g[0]+".jpg"]["cap"] or "")}</figcaption></figure>' for i,g in enumerate(gallery))+'</div>'
    short_html=""
    if shorts:
        short_html='<div class="sidebox"><h3>Watch the short</h3><p>'+" · ".join(f'<a href="{u}" rel="noopener">{n}</a>' for n,u in shorts.items())+'</p></div>'
    mins=""
    if minutes:
        import re as _re
        m=_re.match(r"PT(?:(\d+)M)?(?:(\d+)S)?",minutes)
        if m and m.group(1): mins=f'<span>{m.group(1)} min video</span>'
    kind='<span class="hot">Video + steps</span>' if vid else ('<span class="hot">Place guide</span>' if gallery else '<span class="hot">Checklist</span>')
    cityp=f'<span>{html.escape(place["city"])}</span>' if place else ''
    rel2=""
    if related:
        rel2='<section class="related2"><h2>Keep going</h2><div class="rows">'+"".join(f'<a class="row" href="{u}"><img src="/img/{cl}.jpg" alt="{html.escape(n)} cover" loading="lazy"><span><span class="k">{html.escape(t)}</span><b>{html.escape(n)}</b><span class="go">Read the guide</span></span></a>' for u,cl,t,n in related)+'</div></section>'
    body=f'''<main class="guide2">
<section class="ghero"><div class="wrap">
<p class="eyebrow"><a href="/">Home</a> · <a href="/china/">China guides</a> · {f"published {published} · " if published else ""}updated {checked}</p>
<h1>{h1}</h1>
<p class="lede">{desc}</p>
<div class="gmeta">{kind}{mins}{cityp}<span>Dated and rechecked</span></div>
</div></section>
<div class="wrap lift">
{lift if lift else (yt(vid,title,start) if vid or not gallery else "")+(video_note or "")+gal}
<div class="gridg">
<article>
<div class="intro">{intro}</div>
<h2>Quick answers</h2>
<div class="faq">{faq_html}</div>
{f'<h2>{steps_title}</h2><ol class="steps">{steps_html}</ol>' if steps else ""}
{extra or ""}
<p class="note">Rules change. Everything here was checked on {checked} against the sources below. Before you fly, open the official page once more.</p>
<h2>Sources</h2><ul class="sources">{src_html}</ul>
</article>
<aside>{ch_html}{short_html}<div class="sidebox" {'hidden' if shorts else ''}><h3>Watch it short</h3><p>The same guide as a vertical video on <a href="{SOC['TikTok']}" rel="noopener">TikTok</a>, <a href="{SOC['Instagram']}" rel="noopener">Instagram</a> and <a href="{SOC['Pinterest']}" rel="noopener">Pinterest</a>.</p></div>
<div class="author"><img src="/img/natali-portrait-at-her-desk.jpg" alt=""><div><b>Written by Natali</b><p>A maker from Ireland who films her trips and writes down the parts nobody explains. <a href="/about/">About</a></p></div></div>
<div class="sidebox"><h3>Follow along</h3><div class="share"><a href="{SOC['YouTube']}?sub_confirmation=1" rel="noopener">YouTube</a><a href="{SOC['Instagram']}" rel="noopener">Instagram</a><a href="{SOC['TikTok']}" rel="noopener">TikTok</a><a href="{SOC['Pinterest']}" rel="noopener">Pinterest</a></div></div></aside>
</div>
{rel2}
</div>
</main>'''
    schema=[] if not steps else [{"@context":"https://schema.org","@type":"HowTo","name":h1,"description":desc,"url":url,"dateModified":checked,**({"datePublished":published} if published else {}),"image":og,
             "author":{"@type":"Person","name":"Natali","url":SITE+"/about/"},
             "step":[{"@type":"HowToStep","position":i+1,"name":s[0],**({"image":[SITE+f"/img/{k}.jpg" for k in s[2]]} if len(s)>2 and s[2] else {}),"text":html.unescape(re.sub(r'<[^>]+>','',re.sub(r'<span class="tag[^"]*">.*?</span>|<br>','',s[1]))),"url":f"{url}#step-{i+1}"} for i,s in enumerate(steps)]}]
    schema.append({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]})
    if not steps:
        schema.append({"@context":"https://schema.org","@type":"Article","headline":h1,"description":desc,"url":url,"dateModified":checked,**({"datePublished":published} if published else {}),"image":og,"author":{"@type":"Person","name":"Natali","url":SITE+"/about/"}})
    if vid and vschema:
        up=(upload or checked)
        if len(up)==10: up=up+"T17:00:00+01:00"
        vo={"@context":"https://schema.org","@type":"VideoObject","name":title,"description":desc,"thumbnailUrl":[og] if og else [f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg"],"uploadDate":up,"embedUrl":f"https://www.youtube.com/embed/{vid}","contentUrl":f"https://www.youtube.com/watch?v={vid}","author":{"@type":"Person","name":"Natali","url":SITE+"/about/"},"publisher":{"@type":"Person","name":"Natali","url":SITE+"/about/"}}
        if minutes: vo["duration"]=minutes
        schema.append(vo)
    if place:
        schema.append({"@context":"https://schema.org","@type":"TouristAttraction","name":place["name"],"address":{"@type":"PostalAddress","addressLocality":place.get("city","Shanghai"),"addressCountry":"CN"},"url":url,"isAccessibleForFree":place.get("free",False)})
    schema.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},{"@type":"ListItem","position":2,"name":"China guides","item":SITE+"/china/"},{"@type":"ListItem","position":3,"name":h1,"item":url}]})
    page(path,title,desc,body,schema,og,extra_head=head,dark=True,published=published,modified=checked)

exec(open('src/content.py').read())

# sitemap + robots
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">'+"".join(f'<url><loc>{SITE}{p}</loc><lastmod>{d}</lastmod>'+"".join(f'<image:image><image:loc>{u}</image:loc></image:image>' for u in PAGEIMGS.get(p,[]))+'</url>' for p,d in PAGES)+'</urlset>'
open('docs/sitemap.xml','w').write(sm)
open('docs/robots.txt','w').write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
open('docs/favicon.svg','w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#2F6F73"/><path d="M14 40c8-10 14-8 20-16 4-5 9-6 16-4" fill="none" stroke="#FBF7F0" stroke-width="6" stroke-linecap="round"/><circle cx="46" cy="22" r="6" fill="#E05A7A"/></svg>')
open('docs/.nojekyll','w').write('')
import shutil; shutil.copy('src/404.html','docs/404.html') if os.path.exists('src/404.html') else None
open('docs/_redirects','w').write(open('src/redirects.txt').read())
import glob as _g
_orph=[f[9:] for f in _g.glob('docs/img/**/*.*',recursive=True) if f[9:] not in USED]
if _orph: print("WARNING unused images (not on any page):",_orph)
print("built", len(PAGES), "pages")
