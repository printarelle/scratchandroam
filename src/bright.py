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

def nav_b(SOC, NAV_SHOP, FOOT_GROUPS=None, CARDS=None):
    by={c["slug"]:c for c in (CARDS or [])}
    chev='<svg class="chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>'
    cols=""
    MEGA_PICK={"Before you fly":["first-time-in-china","china-before-you-fly-checklist","china-visa-free-30-days","china-arrival-card-pc"],"Apps and on the ground":["china-travel-apps","alipay-metro-qr-code-china","taobao-for-foreigners","how-to-order-food-in-china-without-speaking-chinese"],"Shanghai":["the-bund-shanghai-at-night","nanjing-road-shanghai","huangpu-river-night-cruise"]}
    for h,l in (FOOT_GROUPS or []):
        sl=[x for x in MEGA_PICK.get(h,l) if x in by]
        if sl: cols+=f'<div class="mcol"><h3>{html.escape(h)}</h3>'+"".join(f'<a href="/guides/{x}/">{html.escape(by[x]["short"])}</a>' for x in sl)+'</div>'
    feat=('<div class="mfeat"><a class="mcard" href="/china/tools/"><span class="eyebrow">New</span><b>Money, units and size tools</b><span>Yuan converter, km and jin, and how to read a Taobao size sheet.</span></a>'
          '<a class="mcard" href="/guides/china-travel-faq/"><span class="eyebrow">Quick answers</span><b>Search every China question</b><span>Short answers with the date I checked them.</span></a>'
          f'<a class="mall" href="/china/">See all {len(by)} China guides →</a></div>')
    def dd(label,body,cls="",pid=""):
        return f'<div class="nd {cls}"><button type="button" class="nb" aria-expanded="false" aria-haspopup="true">{label}{chev}</button><div class="npanel">{body}</div></div>'
    china=dd("China guides",f'<div class="mgrid">{cols}{feat}</div>',"big")
    helpd=dd("Questions &amp; tools",'<a class="ni" href="/guides/china-travel-faq/"><b>Questions answered</b><span>Visa, arrival card, paying, eSIM, trains</span></a><a class="ni" href="/china/tools/"><b>Tools</b><span>Yuan, units, clothing and shoe sizes</span></a><a class="ni" href="/guides/china-travel-faq/#q-lost-phone-or-passport"><b>Lost phone or passport</b><span>What to do first</span></a>',"sm")
    trips=dd("My trips",'<a class="ni" href="/where-ive-been/"><b>Where I\'ve been</b><span>Every place I have filmed</span></a><a class="ni" href="/december-trip/"><b>December trip</b><span>Chengdu, Chongqing and Xi\'an</span></a><a class="ni" href="/travel-deals/"><b>Travel deals</b><span>Hotels, trains and tickets I use</span></a>',"sm")
    js=('<script>(function(){var ds=[].slice.call(document.querySelectorAll(".hb .nd"));function close(except){ds.forEach(function(d){if(d!==except){d.classList.remove("open");d.querySelector(".nb").setAttribute("aria-expanded","false")}})}'
        'ds.forEach(function(d){var b=d.querySelector(".nb");b.addEventListener("click",function(e){e.stopPropagation();var o=!d.classList.contains("open");close(d);d.classList.toggle("open",o);b.setAttribute("aria-expanded",o?"true":"false")})});'
        'document.addEventListener("click",function(e){if(!e.target.closest(".nd"))close()});document.addEventListener("keydown",function(e){if(e.key==="Escape"){var o=document.querySelector(".hb .nd.open .nb");close();if(o)o.focus()}})})();</script>')
    return f'''<header class="hb"><div class="wrap"><a class="logo" href="/" aria-label="Scratch and Roam with Natali, home"><span class="mark">Scratch <em>&amp;</em> Roam</span><span class="with">with Natali</span></a>
<nav id="menu"><a href="/">Home</a>{china}{helpd}{NAV_SHOP()}{trips}<a href="/about/">About</a><a class="msub" href="{SOC['YouTube']}?sub_confirmation=1" rel="me noopener">&#9654; Subscribe on YouTube</a></nav>
<div class="right"><button class="icbtn" id="sbtn" type="button" aria-label="Search guides" aria-haspopup="dialog">{IC["search"]}</button><a class="btn" href="{SOC['YouTube']}?sub_confirmation=1" rel="me noopener">Subscribe</a><button class="icbtn mbtn" id="menuBtn" aria-expanded="false" aria-controls="menu" aria-label="Menu">{IC["menu"]}</button></div></div></header>{js}'''

def footer_b(SOC, FOOT_GROUPS, CARDS):
    by={c["slug"]:c for c in CARDS}
    cols=""
    for h,l in FOOT_GROUPS:
        sl=[x for x in l if x in by]
        extra=('<a href="/guides/china-travel-faq/">Questions answered</a><a href="/china/tools/">Money and size tools</a>' if h=="Before you fly" else "")
        cols+=f'<div><h3>{html.escape(h)}</h3><nav>'+"".join(f'<a href="/guides/{x}/">{html.escape(by[x]["short"])}</a>' for x in sl)+extra+'</nav></div>'
    links="".join(f'<a href="{u}" rel="me noopener">{n}</a>' for n,u in SOC.items())
    return f'''<footer class="ft"><div class="wrap"><div class="grid"><div><a class="logo" href="/"><span class="mark">Scratch <em>&amp;</em> Roam</span><span class="with">with Natali</span></a><p class="tag">Real first-timer China. Real screenshots. Real prices, with the date I checked them.</p><h3 style="margin-top:22px">Follow along</h3><nav>{links}</nav></div>{cols}<div class="stamp">Scratch to reveal<span>Roam</span>to discover</div></div><div class="fine"><span>© 2026 Scratch &amp; Roam with Natali, Ireland. As an Amazon Associate I earn from qualifying purchases.</span><span><a href="/about/">About</a> · <a href="/travel-deals/">Travel deals</a> · <a href="/klook/">Klook</a> · <a href="/affiliate-disclosure/">Affiliate disclosure</a> · <a href="/feed.xml">RSS</a> · scratchandroam@gmail.com</span></div></div></footer>'''

NAVJS_B='<script>(function(){var sb=document.getElementById("shareBtn");if(sb){sb.addEventListener("click",function(e){e.preventDefault();var u=location.href.split("#")[0],t=document.title;if(navigator.share){navigator.share({title:t,url:u}).catch(function(){});return}var done=function(){var l=sb.querySelector("span");l.textContent="Link copied";setTimeout(function(){l.textContent="Share"},2000)};if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(u).then(done,function(){location.hash="share"})}else{location.hash="share"}})}var tm=document.getElementById("tabMenu");if(tm){tm.addEventListener("click",function(){var mb=document.getElementById("menuBtn");if(mb){mb.click();window.scrollTo({top:0,behavior:"smooth"})}})}var b=document.getElementById("menuBtn"),m=document.getElementById("menu");if(b){b.addEventListener("click",function(){var o=m.classList.toggle("open");b.setAttribute("aria-expanded",o?"true":"false");});}var L=[].slice.call(document.querySelectorAll(".toc a[href^=\\"#\\"]"));if(L.length&&"IntersectionObserver" in window){var map={};L.forEach(function(a){map[a.getAttribute("href").slice(1)]=a;});var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){L.forEach(function(a){a.classList.remove("on")});var a=map[e.target.id];if(a)a.classList.add("on");}});},{rootMargin:"-20% 0px -70% 0px"});Object.keys(map).forEach(function(id){var el=document.getElementById(id);if(el)io.observe(el);});L[0].classList.add("on");}})();(function(){var t=document.createElement("button");t.type="button";t.id="toTop";t.setAttribute("aria-label","Back to top");t.hidden=true;t.innerHTML="<svg viewBox=\\"0 0 24 24\\" aria-hidden=\\"true\\"><path d=\\"M6 14l6-6 6 6\\"/></svg>";document.body.appendChild(t);var on=false;function f(){var s=window.pageYOffset>700;if(s!==on){on=s;t.hidden=!s}}window.addEventListener("scroll",f,{passive:true});f();t.addEventListener("click",function(){var r=window.matchMedia&&window.matchMedia("(prefers-reduced-motion: reduce)").matches;window.scrollTo({top:0,behavior:r?"auto":"smooth"})})})();</script>'


# ===== tick-off steps, quick answers, topic shortcuts, phone tab bar =====
TICK_GUIDES={"first-time-in-china","china-before-you-fly-checklist","china-arrival-card-pc","china-arrival-card-alipay","china-travel-apps","china-dos-and-donts","china-visa-free-30-days","alipay-metro-qr-code-china","taobao-for-foreigners","taobao-11-11-singles-day-for-foreigners","food-delivery-in-china-for-foreigners-meituan","how-to-order-food-in-china-without-speaking-chinese","build-spice-tolerance-before-china"}
TICKJS=r"""(function(){var bar=document.getElementById("tickbar");if(!bar)return;var key="sr-tick:"+bar.getAttribute("data-key"),bs=[].slice.call(document.querySelectorAll(".steps .tick")),saved=[];try{saved=JSON.parse(localStorage.getItem(key)||"[]")}catch(e){}
function on(b){return b.getAttribute("aria-pressed")==="true"}
function count(){return bs.filter(on).length}
function paint(){var n=0;bs.forEach(function(b){var o=on(b);if(o)n++;b.parentNode.classList.toggle("ticked",o)});bar.classList.toggle("started",n>0);document.getElementById("tkcnt").textContent=n+" of "+bs.length+" done";document.getElementById("tkfill").style.width=Math.round(n/bs.length*100)+"%";document.getElementById("tkdone").hidden=n!==bs.length;try{localStorage.setItem(key,JSON.stringify(bs.map(on)))}catch(e){}}
bs.forEach(function(b,i){if(saved[i])b.setAttribute("aria-pressed","true");b.addEventListener("click",function(){b.setAttribute("aria-pressed",on(b)?"false":"true");paint()})});
var conf=document.getElementById("tkconf");
document.getElementById("tkreset").addEventListener("click",function(){var n=count();if(!n)return;document.getElementById("tkn").textContent=n;conf.hidden=false;document.getElementById("tkno").focus()});
document.getElementById("tkyes").addEventListener("click",function(){bs.forEach(function(b){b.setAttribute("aria-pressed","false")});conf.hidden=true;paint()});
document.getElementById("tkno").addEventListener("click",function(){conf.hidden=true});
document.getElementById("tkpdf").addEventListener("click",function(){window.print()});
var cb=document.getElementById("tkcopy");cb.addEventListener("click",function(){var left=bs.filter(function(b){return!on(b)}).map(function(b){var h=b.parentNode.querySelector("h3");return "- "+(h?h.textContent.trim():"")});var h1=document.querySelector("h1");var t=left.length?"Still to do ("+left.length+" of "+bs.length+"): "+(h1?h1.textContent.trim():"")+"\n"+left.join("\n")+"\n"+location.href.split("#")[0]:"All "+bs.length+" steps done.";var done=function(m){var o=cb.textContent;cb.textContent=m;setTimeout(function(){cb.textContent=o},2000)};
function fb(){var ta=document.createElement("textarea");ta.value=t;ta.style.position="fixed";ta.style.opacity="0";document.body.appendChild(ta);ta.select();var ok=false;try{ok=document.execCommand("copy")}catch(e){}document.body.removeChild(ta);done(ok?"Copied":"Copy failed")}
if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(function(){done("Copied")},fb)}else fb()});
paint()})();"""

QUICK={
 "taobao-11-11-singles-day-for-foreigners":("Quick answer",[
  ("When is the sale?","Deposits opened 15 October. The main sale began 20 October at 8 pm China time. The big day is Wednesday 11 November."),
  ("Can foreigners join?","Yes, for physical goods, paying through Alipay with your own bank card."),
  ("Do foreign cards work?","Linked cards work for normal orders. I could not confirm presale deposits, so pay a small in-stock order first."),
  ("Hotel delivery?","Yes if the hotel agrees. Not worth it for a stay of one to three days, because delivery can take up to three days."),
 ],("Taobao setup guide, step by step","/guides/taobao-for-foreigners/")),
}
def quick_b(slug):
    t,rows,(lt,lu)=QUICK[slug]
    return (f'<aside class="qbox" aria-label="{html.escape(t)}"><p class="ck">{html.escape(t)}</p><dl>'+"".join(f'<div><dt>{html.escape(a)}</dt><dd>{html.escape(b)}</dd></div>' for a,b in rows)+f'</dl><a class="btn" href="{lu}">{html.escape(lt)}</a></aside>')

HELP=[("Entry and visas","Visa-free rules","/guides/china-visa-free-30-days/"),
 ("Arrival card","Fill it in before you fly","/guides/china-arrival-card-pc/"),
 ("Paying in China","Alipay and WeChat","/guides/china-travel-apps/"),
 ("Travel apps","The 25 I used","/guides/top-25-china-apps/"),
 ("Trains and metro","Metro QR code","/guides/alipay-metro-qr-code-china/"),
 ("Shopping","Taobao, 11.11","/guides/taobao-for-foreigners/"),
 ("Food","Order without Chinese","/guides/how-to-order-food-in-china-without-speaking-chinese/"),
 ("Shanghai","Bund, Nanjing Road, shows","/#shanghai")]
def help_b():
    return ('<section class="help"><div class="wrap"><h2>What do you need help with?</h2><div class="hgrid">'
      +"".join(f'<a href="{u}"><b>{html.escape(a)}</b><span>{html.escape(b)}</span></a>' for a,b,u in HELP)+'</div><p class="hmore"><a class="more" href="/guides/china-travel-faq/">Browse every China question answered →</a></p></div></section>')

def tabbar_b(path):
    ic=lambda d:f'<svg viewBox="0 0 24 24" aria-hidden="true">{d}</svg>'
    BEFORE={"/guides/first-time-in-china/","/guides/china-before-you-fly-checklist/","/guides/china-visa-free-30-days/","/guides/china-arrival-card-pc/","/guides/china-arrival-card-alipay/","/guides/china-dos-and-donts/","/guides/build-spice-tolerance-before-china/"}
    APPS=lambda p:p.startswith("/guides/") and any(k in p for k in ("apps","metro","taobao","food","order"))
    cur="before" if path in BEFORE else ("apps" if APPS(path) else ("tools" if path=="/china/tools/" else ""))
    def a(k,href,label,d): return f'<a href="{href}"{" class=\"on\" aria-current=\"page\"" if cur==k else ""}>{ic(d)}{label}</a>'
    return ('<nav class="tabs" aria-label="Quick links">'
      +a("before","/guides/first-time-in-china/","Before you fly",'<path d="M4 12.5l4.5 4.5L20 6"/>')
      +a("apps","/guides/china-travel-apps/","Apps",'<rect x="7" y="2.5" width="10" height="19" rx="2.5"/><path d="M11 18.5h2"/>')
      +a("tools","/china/tools/","Tools",'<rect x="5" y="2.5" width="14" height="19" rx="2.5"/><path d="M8.5 7h7M8.5 12h2M13.5 12h2M8.5 16.5h2M13.5 16.5h2"/>')
      +f'<button type="button" id="tabMenu">{ic("<path d=\"M4 7h16M4 12h16M4 17h16\"/>")}Menu</button></nav>')

STOPS=[("Chengdu","6 to 9 Dec","We land on Sunday 6 December and settle into an apartment near Taikoo Li, which is our base for the whole trip.","Pandas, hotpot, the metro and Taikoo Li.",None),
 ("Chongqing","9 to 14 Dec","Hotel Indigo Chongqing Chaotianmen for five nights, with the drone show on Saturday 12 December.","Hotpot, the cableway, Liziba and the old town at night.",None),
 ("Xi'an","14 to 18 Dec","Han Tang House for four nights. The Muslim Quarter, the Bell and Drum Towers, the Great Mosque and the Terracotta Warriors.","The food streets and the city wall.",None),
 ("Chengdu again","18 to 29 Dec","Back to the apartment, with Christmas at the InterContinental Chengdu Global Center on 24 and 25 December.","Hotel review, the Global Center and a proper rest.",None)]
def december_b(SOC, CARDS):
    cards="".join(f'<article class="dstop"><span class="dd">{d}</span><h3>{html.escape(c)}</h3><p>{t}</p><small>{html.escape(w)}</small></article>' for c,d,t,w,_ in STOPS)
    by={c["slug"]:c for c in CARDS}
    guides=[("first-time-in-china","Before you fly"),("china-travel-apps","Apps to install"),("china-arrival-card-pc","Arrival card"),("alipay-metro-qr-code-china","Metro QR code"),("ihg-hotels-china-shanghai-hangzhou-review","IHG hotels in China")]
    gl="".join(f'<a href="/guides/{g}/"><b>{html.escape(l)}</b><span>{html.escape(by[g]["short"])}</span></a>' for g,l in guides if g in by)
    return f'''<main>
<section class="phero"><div class="wrap"><nav class="crumbs"><a href="/">Home</a><span>/</span><span>December trip</span></nav><p class="eyebrow">Trip 3 · December 2026</p><h1>China in December: Chengdu, Chongqing and Xi'an</h1><p class="lede">Our third China trip. Three cities, high-speed trains between them, and a Christmas in Chengdu. This page is the plan, and it fills in with videos and guides as I film them.</p></div></section>
<section class="sec"><div class="wrap"><div class="sechead left"><div><p class="eyebrow">The route</p><h2>Chengdu, Chongqing, Xi'an, back to Chengdu</h2><p>We fly from Ireland on 5 December and come home on 29 December. Chengdu is our base the whole time, and we take the side trips from there.</p></div></div><div class="dstops">{cards}</div><p class="dnote">Train tickets between the cities are not booked yet. When they are, the guide for that route goes up with the screenshots.</p></div></section>
<section class="sec mint"><div class="wrap"><div class="sechead left"><div><p class="eyebrow">Planned films</p><h2>What I will film and write up</h2></div></div><ul class="dlist"><li><b>Hotel reviews</b> for the stays above, including what the IHG status actually gave us.</li><li><b>Xi'an</b> and the Terracotta Warriors, step by step.</li><li><b>Chongqing after dark</b>, the drone show and the hotpot.</li><li><b>Trains and metro</b> between the three cities, with the tickets and the apps.</li></ul><p class="dnote">The plan can change. I only write a guide after I have done the thing.</p></div></section>
<section class="sec"><div class="wrap"><div class="sechead left"><div><h2>Read these first</h2><p>The guides that make any China trip easier, from the first two trips.</p></div></div><div class="hgrid dg">{gl}</div></div></section>
<section class="band"><div class="wrap"><div class="bcard"><h2>Follow the trip</h2><p>Videos land on YouTube first. Short clips go on TikTok and Instagram while we are there.</p><div class="acts"><a class="btn" href="{SOC['YouTube']}?sub_confirmation=1" rel="noopener">Subscribe on YouTube</a><a class="btn ghost" href="/china/">All China guides</a></div></div></div></section>
</main>'''

TIKTOKS={}   # slug -> [(tiktok video url, short caption)]. Add her real video links here and they show as tap-to-play on that guide.
def tiktok_b(slug):
    import re as _r
    items=TIKTOKS.get(slug) or []
    out=[]
    for u,cap in items:
        m=_r.search(r"/video/(\d+)",u)
        if not m: continue
        out.append(f'<figure class="ttv"><button type="button" class="ttplay" data-id="{m.group(1)}" aria-label="Play the TikTok: {html.escape(cap)}"><span class="ttbadge">TikTok</span><span class="ttcap">{html.escape(cap)}</span><span class="ttgo">&#9654; Tap to play</span></button><figcaption><a href="{u}" rel="noopener">Open on TikTok</a></figcaption></figure>')
    if not out: return ""
    return ('<h2 id="short">Watch it as a short</h2><div class="ttrow">'+"".join(out)+'</div><p class="ttnote">The video loads from TikTok only when you tap play. If TikTok is blocked where you are, use the link under it.</p>'
      '<script>(function(){[].slice.call(document.querySelectorAll(".ttplay")).forEach(function(b){b.addEventListener("click",function(){var f=document.createElement("iframe");f.src="https://www.tiktok.com/embed/v2/"+b.getAttribute("data-id");f.setAttribute("allowfullscreen","");f.setAttribute("allow","encrypted-media;fullscreen");f.title="TikTok video";f.loading="lazy";f.className="ttframe";b.parentNode.replaceChild(f,b)})})})();</script>')

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

# ===== Guide groups: each guide has one job, a "You are here" map and a next step =====
CLUSTERS=[
 ("plan","Plan your first China trip",[
   ("first-time-in-china","The full plan, in order","Start here: every step from entry rules to packing"),
   ("china-visa-free-30-days","Do you need a visa?","Visa-free entry and the 30-day rule"),
   ("china-arrival-card-pc","Arrival card on a computer","The form, step by step"),
   ("china-arrival-card-alipay","Arrival card on your phone","The same form inside Alipay"),
   ("china-before-you-fly-checklist","Safety and backups","Insurance, documents, emergency numbers, plan B"),
   ("china-dos-and-donts","Do's and don'ts","The small rules that save you trouble"),
 ]),
 ("apps","Apps and paying in China",[
   ("china-travel-apps","Set up the must-have apps","Start here: the 12 to set up at home, with the steps"),
   ("top-25-china-apps","All 25 apps, ranked","The full list from critical to optional, to choose extras"),
   ("alipay-metro-qr-code-china","The metro with Alipay","Ride with the QR code"),
   ("how-to-order-food-in-china-without-speaking-chinese","Order food","Menus, QR codes and delivery"),
   ("food-delivery-in-china-for-foreigners-meituan","Food delivery","Meituan in WeChat, to your hotel"),
   ("taobao-for-foreigners","Shop on Taobao","Order to your hotel"),
 ]),
 ("shanghai","Shanghai, what to book and see",[
   ("the-bund-shanghai-at-night","The Bund at night","Start here: when to go and where to stand"),
   ("nanjing-road-shanghai","Nanjing Road","The walk from the Bund"),
   ("huangpu-river-night-cruise","Huangpu River night cruise","Which pier, which cruise, how to book"),
   ("shanghai-circus-world-era-show","ERA show tickets","Where we booked and how to get there"),
 ]),
]
CLUSTER_OF={g[0]:c for c in CLUSTERS for g in c[2]}
def cluster_b(slug):
    key,title,items=CLUSTER_OF[slug]
    i=[g[0] for g in items].index(slug)
    lis="".join(f'<li{" class=\"here\"" if g[0]==slug else ""}>'+(f'<b>{html.escape(g[1])}</b><span>You are here</span>' if g[0]==slug else f'<a href="/guides/{g[0]}/"><b>{html.escape(g[1])}</b><span>{html.escape(g[2])}</span></a>')+'</li>' for g in items)
    nxt=items[i+1] if i+1<len(items) else items[0]
    return (f'<nav class="clus" aria-label="{html.escape(title)}"><p class="ck">Part of: {html.escape(title)}</p><ol>{lis}</ol>'
            f'<a class="cnext" href="/guides/{nxt[0]}/">Next: {html.escape(nxt[1])} →</a></nav>')

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
    hero_cap=(IMGREG.get(hero_img+".jpg",{}).get("cap") or "") if gallery else "Shanghai, our own photo"
    # body pieces
    toc=[]
    body=[]
    body.append(f'<div class="intro{" nodrop" if _t(intro)[:1].isdigit() else ""}">{intro}</div>')
    if slug in TICK_GUIDES and steps: body.append(f'<p class="startck"><a class="btn" href="#steps">Start the {len(steps)}-step checklist</a></p>')
    if slug in QUICK: body.append(quick_b(slug))
    if slug in CLUSTER_OF: body.append(cluster_b(slug))
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
        _pk=STEP_PICKS.get(slug,{}) if AFFILIATES_LIVE else {}
        body.append(f'<h2 id="steps">{html.escape(steps_title)}</h2>'); toc.append(("steps",steps_title))
        _tick = slug in TICK_GUIDES
        if _tick:
            body.append(f'<div class="tickbar" id="tickbar" data-key="{slug}"><div class="tk-top"><b>Tick-off checklist</b><span>Tap a step number to tick it off. Progress is saved in this browser on this device. No account needed.</span></div><div class="tk-prog"><span id="tkcnt">0 of {len(steps)} done</span></div><div class="tk-bar"><i id="tkfill"></i></div><div class="tk-acts"><button type="button" id="tkcopy">Copy what is left</button><button type="button" id="tkpdf">Save as PDF</button><button type="button" id="tkreset">Reset</button></div><div class="tk-confirm" id="tkconf" hidden role="alert"><span>Reset all <b id="tkn"></b> ticked steps?</span><button type="button" id="tkyes">Yes, reset</button><button type="button" id="tkno">Keep them</button></div></div>')
        _nb = (lambda i: f'<button type="button" class="n tick" aria-pressed="false" aria-label="Tick off step {i}">{i}</button>') if _tick else (lambda i: f'<div class="n">{i}</div>')
        body.append('<ol class="steps'+(' ticking' if _tick else '')+'">'+"".join(f'<li id="step-{i+1}">{_nb(i+1)}<div><h3>{html.escape(s[0])}</h3><p>{s[1]}</p>{figs(s[2] if len(s)>2 else None)}{_pk.get(i+1,"")}</div></li>' for i,s in enumerate(steps))+'</ol>')
        if _tick: body.append('<div class="tkdone" id="tkdone" hidden><b>All done.</b> Safe travels. <a href="/china/">More China guides →</a></div><script>'+TICKJS+'</script>')
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
    body.append(callout("tip",f'Rules change. Everything on this page was checked on {checked} against the sources below. Before you fly, open the official page once more.'))
    body.append('<h2 id="sources">Sources</h2>'); toc.append(("sources","Sources"))
    body.append('<ul class="sources">'+"".join(f'<li><a href="{u}" rel="noopener">{html.escape(n)}</a>{" (official)" if off else ""}</li>' for n,u,off in sources)+'</ul>')
    if TIKTOKS.get(slug): body.append(tiktok_b(slug)); toc.append(("short","Watch it as a short"))
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
    _sec=by[slug].get("sec")
    topic_pill={'place':'<a class="pill mint" href="/#shanghai">Shanghai</a>','before':'<a class="pill mint" href="/china/">Before you fly</a>','shop':'<a class="pill mint" href="/china/">China shopping</a>'}.get(_sec,'')
    if slug in TICK_GUIDES: topic_pill+='<span class="pill coral">Tick-off steps</span>'
    return f'''<main>
<section class="ghero"><div class="wrap">
<div class="hcard">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span><a href="/china/">Asia</a><span>/</span><a href="/china/">China</a><span>/</span><span>{crumb_last}</span></nav>
<div class="tags"><a class="pill mint" href="/china/">Guide</a><a class="pill mint" href="/china/">China</a>{topic_pill}<span class="pill mint">{kind}</span></div>
<div class="meta"><span class="pill coral">{IC["clock"]}{rd} min read</span><a class="pill blue" id="shareBtn" href="#share">{IC["share"]}<span>Share</span></a></div>
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
<div class="scard"><span class="eyebrow">Quick answers</span><p>Short, dated answers to the China questions first-timers ask.</p><a href="/guides/china-travel-faq/">Search the questions →</a><p style="margin-top:10px"><a href="/china/tools/">Yuan and clothing size tools →</a></p></div>
</aside>
</div>
{band_b(SOC)}
{social_b(SOC,"the-bund-pudong-skyline-and-shanghai-tower-at-night","nanjing-road-curved-corner-building-neon-lights")}
</main>'''

SCRATCH_HTML='<section class="sec" style="padding-top:0"><div class="wrap"><div class="scr">\n<div class="scr-copy"><p class="eyebrow">Scratch to reveal</p><h2>One tip from my own trips</h2><p>Scratch the card (or tap Reveal) for a lesson I learned the hard way in China. A new one each time you visit.</p><button type="button" class="btn ghost" id="scrBtn">Reveal</button></div>\n<div class="scr-card"><div class="scr-tip" id="scrTip" aria-live="polite"></div><canvas id="scrC" aria-hidden="true"></canvas></div>\n</div></div></section>\n<script>(function(){var T=[["Turn on your eSIM before you land.","At Christmas 2025 mine was ready and I forgot to switch it on. Have a backup plan too.","/guides/china-travel-apps/#step-8"],["If 12306 will not let you register, use Trip.com.","I could not get through 12306 in Alipay, so I booked all our trains on Trip.com for a small fee.","/guides/china-travel-apps/#step-5"],["Message the hotel before a Taobao parcel arrives.","Name, booking number, dates, and their address in Chinese. Tens of parcels, none lost.","/guides/taobao-for-foreigners/"],["Pack a plug adapter anyway.","Every Shanghai hotel we stayed in had UK sockets. I still carry one, just in case.","/guides/china-dos-and-donts/"],["Spend New Year on the Bund.","Our first trip, Christmas 2025. Honestly, the best decision we made.","/guides/the-bund-shanghai-at-night/"]];\nvar t=T[Math.floor(Math.random()*T.length)],tip=document.getElementById("scrTip"),c=document.getElementById("scrC"),b=document.getElementById("scrBtn");if(!c)return;\ntip.innerHTML=\'<b>\'+t[0]+\'</b><span>\'+t[1]+\'</span><a href="\'+t[2]+\'">Read the guide →</a>\';\nvar x=c.getContext("2d"),done=false,down=false;function size(){var r=c.parentNode.getBoundingClientRect(),d=window.devicePixelRatio||1;c.width=r.width*d;c.height=r.height*d;x.setTransform(d,0,0,d,0,0);var g=x.createLinearGradient(0,0,r.width,r.height);g.addColorStop(0,"#C9CDD3");g.addColorStop(.5,"#EEF0F2");g.addColorStop(1,"#B7BCC4");x.globalCompositeOperation="source-over";x.fillStyle=g;x.fillRect(0,0,r.width,r.height);x.fillStyle="#1B2A41";x.font="700 15px \'Plus Jakarta Sans\',sans-serif";x.textAlign="center";x.fillText("SCRATCH HERE",r.width/2,r.height/2+5);x.globalCompositeOperation="destination-out"}\nsize();window.addEventListener("resize",function(){if(!done)size()});\nfunction reveal(){done=true;c.style.transition="opacity .5s";c.style.opacity=0;setTimeout(function(){c.style.display="none"},500)}\nfunction pt(e){var r=c.getBoundingClientRect(),p=e.touches?e.touches[0]:e;return[p.clientX-r.left,p.clientY-r.top]}\nfunction scratch(e){if(!down||done)return;e.preventDefault();var p=pt(e);x.beginPath();x.arc(p[0],p[1],22,0,6.3);x.fill();}\nfunction check(){if(done)return;var d=x.getImageData(0,0,c.width,c.height).data,n=0;for(var i=3;i<d.length;i+=64)if(d[i]===0)n++;if(n/(d.length/64)>.45)reveal()}\nc.addEventListener("pointerdown",function(e){down=true;scratch(e)});c.addEventListener("pointermove",scratch);window.addEventListener("pointerup",function(){if(down){down=false;check()}});b.addEventListener("click",reveal)})();</script>\n'

def home_b(*, CARDS, SOC, n_guides):
    by={c["slug"]:c for c in CARDS}
    def gcard(c,small=False):
        return f'<a class="gc" href="/guides/{c["slug"]}/"><img src="/img/{c["img"]}.jpg" alt="{html.escape(c["alt"])}" loading="lazy"><div class="in"><span class="cat">{html.escape(c["meta"][0] if c.get("meta") else "Guide")}</span><h3>{html.escape(c.get("t") or c["short"])}</h3>{"" if small else f"<p>{html.escape(c.get(chr(112),chr(32)))}</p>"}<small>{html.escape(c["meta"][1] if c.get("meta") else "Shanghai")}</small></div></a>'
    start=[by[s] for s in ("china-arrival-card-pc","first-time-in-china","china-travel-apps")]
    before=[c for c in CARDS if c["sec"] in ("before","shop") and c not in start]
    places=[c for c in CARDS if c["sec"]=="place"]
    dests=f'''<a class="dest" href="/china/"><img src="/img/the-bund-pink-lit-pearl-tower-over-the-crowd.jpg" alt=""><div class="in"><h3>Shanghai</h3><small>{n_guides} guides</small><p>Two trips: Christmas 2025 and Easter 2026. The arrival card, Alipay, the metro QR, the Bund at night, the river cruise and the ERA show.</p></div></a>
<a class="dest soon" href="/december-trip/"><div class="noimg"><span>🇨🇳</span><small>Photos in December</small></div><div class="in"><h3>Chengdu, Chongqing, Xi'an</h3><small>December 2026, filming</small><p>Trains between the three, the metro cards, and the first pandas. Guides go up as I check each one.</p></div></a>
<a class="dest soon" href="{SOC['YouTube']}?sub_confirmation=1" rel="noopener"><div class="noimg"><span>🇯🇵</span><small>Photos coming</small></div><div class="in"><h3>Japan</h3><small>Been there, guides coming</small><p>I have been to Japan too. Those guides come after the China ones. Subscribe and they land in your feed.</p></div></a>'''
    return f'''<main>
<section class="hhero"><div class="wrap"><div><p class="eyebrow">Real first-timer China. Real screenshots.</p><h1>China travel guides, step by step, from someone who just did it</h1><p class="lede">I'm Natali, a maker from Ireland. I filmed my first trip to China and wrote down every form, app and queue that nobody explains, with the date I checked each one.</p><div class="acts"><a class="btn" href="/guides/china-arrival-card-pc/">Start with the arrival card</a><a class="btn ghost" href="/china/">{IC["pin"]} Browse China guides</a></div><a class="small" href="{SOC['YouTube']}?sub_confirmation=1" rel="noopener">{IC["mail"]} Watch the videos behind the guides</a></div>
<div class="collage"><figure><img src="/img/the-bund-gold-lit-historic-buildings-at-night.jpg" alt=""><figcaption>The Bund</figcaption></figure><figure><img src="/img/nanjing-road-curved-corner-building-neon-lights.jpg" alt=""><figcaption>Nanjing Road</figcaption></figure></div></div></section>
{help_b()}
{stats_b(n_guides,"A bit about my travels.")}
<section class="sec"><div class="wrap"><div class="sechead"><p class="eyebrow">Where I've been</p><h2>Where I've been. Where I can help.</h2><p>First-timer guides from the trips I've actually taken, with the screenshots from my own phone and the prices I actually paid.</p></div><div class="dests">{dests}</div></div></section>
{SCRATCH_HTML}
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
AFF_NOTE='<b class="adl">#Ad</b> This page has affiliate links. If you book through one I earn a small commission at no extra cost to you. I always say which ones we booked ourselves. <a href="/affiliate-disclosure/">Affiliate disclosure</a>.'
# Placeholder partner links. Replace "#TODO" with the real affiliate URLs / codes.
PARTNERS={
 "klook":dict(name="Klook",code=None,url="https://klook.tpm.li/jfysgwVe",qr="klook-scratch-and-roam-link-qr-code"),
}
KLOOK_CRUISE="https://klook.tpm.li/Gt6dONHf"
OFFERS={
 # Only links Natali gave. "pick"/badge only where she says she booked it. Prices only if she gives them.
 "shanghai-circus-world-era-show":[
  dict(k="Klook",price=None,title="ERA: Intersection of Time, Shanghai Circus World",
       text="This is where we booked our ERA tickets. You choose a zone and the date, and the ticket comes through Klook. The zones and how to pick one are explained in the steps below.",
       url="https://klook.tpm.li/YtyjQpDu",pick=True,badge="Where we booked",cta="See ERA tickets on Klook",
       qr="klook-era-shanghai-circus-world-tickets-qr-code",qralt="QR code for the Klook ERA ticket page"),
 ],
 "huangpu-river-night-cruise":[
  dict(k="Klook",price=None,title="Huangpu River Night Cruise Experience",
       text="The night cruise on Klook. Check which pier the ticket is for before you book, because a ticket only works at its own pier (step 1 below).",
       url=KLOOK_CRUISE,cta="See the night cruise on Klook",
       qr="klook-huangpu-river-night-cruise-qr-code",qralt="QR code for the Klook Huangpu River night cruise page"),
 ],
}
OFFER_HEAD={
 "shanghai-circus-world-era-show":("Where we booked our tickets",
   "We booked ERA through Klook, and this is the link I use. It is an affiliate link: if you book through it, I may earn a small commission at no extra cost to you. Ticket prices change by date and zone, so check today's price on the page."),
 "huangpu-river-night-cruise":("Where to book the cruise",
   "The cruise on Klook. It is an affiliate link: if you book through it, I may earn a small commission at no extra cost to you. Prices change by date and boat, so check today's price on the page."),
}
# guides that mention the cruise in passing and carry the same links inline (they show the affiliate note too)
AFF_INLINE={"the-bund-shanghai-at-night","nanjing-road-shanghai","huangpu-river-night-cruise","shanghai-circus-world-era-show"}
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
    h,t=OFFER_HEAD.get(slug,("Where to book","These are affiliate links: if you book through one, I may earn a small commission at no extra cost to you."))
    return f'<h2 id="book">{html.escape(h)}</h2><p>{html.escape(t)}</p><div class="offers">{cards}</div>'

def partner_b(key, SOC):
    p=PARTNERS[key]; n=html.escape(p["name"])
    qr=f'<figure class="pqr"><img src="/img/{p["qr"]}.jpg" alt="QR code that opens {n}" width="200" height="200"><figcaption>On a computer? Scan with your phone camera.</figcaption></figure>' if p.get("qr") else ''
    code=f'<span class="k">Use this code at checkout</span><div class="codebox" id="code"><span>{html.escape(p["code"])}</span><button type="button" data-copy="{html.escape(p["code"])}">Copy</button></div>' if p.get("code") else ''
    items=[(s_,o) for s_,lst in OFFERS.items() for o in lst if o["k"]==p["name"]]
    titles={"shanghai-circus-world-era-show":"Shanghai Circus World ERA show","huangpu-river-night-cruise":"Huangpu River night cruise"}
    cards="".join(f'<div class="offer{" pick" if o.get("pick") else ""}">{"<span class=\"badge\">"+html.escape(o.get("badge",""))+"</span>" if o.get("pick") else ""}<div class="otext"><span class="k">{html.escape(titles.get(s_,s_))}</span><b>{html.escape(o["title"])}</b><p>{html.escape(o["text"].replace(" in the steps below"," in my guide").replace(" (step 1 below)"," (my guide explains the piers)"))}</p><a class="btn" href="{o["url"]}" rel="sponsored noopener" target="_blank">{html.escape(o.get("cta","See it on "+n))}</a><span class="via"><a href="/guides/{s_}/">Read my guide first</a></span></div></div>' for s_,o in items)
    return f'''<main>
<section class="phero"><div class="wrap"><nav class="crumbs"><a href="/">Home</a><span>/</span><span>{n}</span></nav><p class="eyebrow"><span class="adl">#Ad</span> Travel deals</p><h1>{n}: my link, and what we booked</h1><p class="lede">We booked our ERA show tickets in Shanghai on {n}. This page has my {n} link, and the things on this site you can book there, each with the guide that explains it.</p></div></section>
<section class="pcode"><div class="wrap"><div class="plink"><div><h2>Open {n} with my link</h2><p>It opens the normal {n} site. If you book through it, I may earn a small commission at no extra cost to you.</p>{code}<div class="acts"><a class="btn" href="{p["url"]}" rel="sponsored noopener" target="_blank">Open {n}</a><a class="btn ghost" href="/china/">See the China guides</a></div><small>Affiliate link. <a href="/affiliate-disclosure/">How affiliate links work on this site</a>.</small></div>{qr}</div></div></section>
<section class="sec mint"><div class="wrap"><div class="sechead left"><div><h2>On {n}, from my guides</h2><p>Each card says whether we booked it ourselves. Read the guide first: it has the pier, the zone, the times and the things to check.</p></div></div><div class="offers">{cards}</div></div></section>
{band_b(SOC)}
</main>'''

def disclosure_b(SOC):
    return f'''<main>
<section class="phero"><div class="wrap"><nav class="crumbs"><a href="/">Home</a><span>/</span><span>Affiliate disclosure</span></nav><p class="eyebrow">Affiliate disclosure</p><h1>How affiliate links work on this site</h1><p class="lede">Some links on Scratch &amp; Roam are affiliate links. Here is what that means for you, in plain words.</p></div></section>
<section class="sec" style="padding-top:10px"><div class="wrap"><article class="art" style="max-width:720px">
<h2 style="margin-top:0">What an affiliate link is</h2><p>When you book through one of my affiliate links, the booking site pays me a small commission. It costs you nothing extra. It is one of the ways I keep the guides free to read.</p>
<h2>Which links are affiliate links</h2><p>Links to Klook, Viator, NordVPN, ExpressVPN, NordPass, Tiqets, Airalo, Yesim, Saily, Welcome Pickups, GetTransfer and Kiwi.com on this site are affiliate links.</p><p>On the Travel deals page, a card marked "I use this" is something I use myself, and "We booked here" means we booked through it. Every guide that has them says so at the top, next to the date it was checked, and again next to the links. Guides with no affiliate links say "Nothing here is sponsored".</p>
<h2>Amazon</h2><p>As an Amazon Associate I earn from qualifying purchases. Some guides link to Amazon for things the guide tells you to pack. In Ireland the links open Amazon.ie. Everywhere else they open Amazon.com, which sends you on to your own country's Amazon store if there is one.</p>\n<h2>Referral codes</h2><p>Some cards on the Travel deals page have a referral code instead of an affiliate link. With the Firsty code, for example, you get €3 off your first purchase over €4 and I get €3 credit in my app.</p>
<h2>What we booked ourselves</h2><p>When we booked something ourselves, the card says so, for example "Where we booked" on the ERA show tickets. When a card does not say that, it is an option I am sharing, not something we have tried.</p>
<h2>What it does not change</h2><p>No company pays me to write a guide or to say good things. The steps, the prices and the rules in each guide come from our own trips and from the sources listed at the bottom of each page, with the date I checked them.</p>
<h2>Tracking</h2><p>To count bookings that come from my links, pages on this site load a small script from Travelpayouts (the network that runs most of my partner links). They are used to match a booking to my link.</p>
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
        pic=f'<img src="/img/{img}.jpg" alt="">' if img else f'<div class="noimg"><span>{flag}</span><small>Photos coming</small></div>'
        return f'''<article class="cc{" soon" if soon else ""}"><div class="top">{pic}<span class="flag">{flag}</span><h2>{name}</h2><div class="pills"><span>{IC["plane"]}{trips}</span><span>{IC["pin"]}{days}</span></div></div><div class="body"><p>{desc}</p><a class="explore" href="{explore[1]}">{IC["book"]} {explore[0]} <span>→</span></a><div class="count"><b>{count[0]}</b>{count[1]}</div></div><div class="visits">{visit("cal","First visit",first)}{visit("plane","Last visit",last)}</div></article>'''
    cards=cc("the-bund-pink-lit-pearl-tower-over-the-crowd","🇨🇳","China","2 trips","Christmas + Easter","Our first trip was Christmas 2025 in Shanghai, with Disneyland, then New Year on the Bund. We went back for Easter 2026, fully prepared this time. Every guide on this site so far comes from those two trips.",("Explore China","/china/"),(str(n_guides),"guides"),"Dec 2025","Apr 2026")
    cards+=cc(None,"🇨🇳","Chengdu, Chongqing, Xi'an","Trip 3","Dec 2026","The next trip: three cities by high-speed train, the metro cards in each, the pandas, and the food. Guides go up as I check each one.",("Follow the trip",SOC["YouTube"]),("0","guides yet"),"Dec 2026","Coming",True)
    cards+=cc(None,"🇯🇵","Japan","Been there","Guides coming","I have been to Japan too, and I have the footage. The Japan guides come after the China ones. Subscribe and they land in your feed.",("Subscribe",SOC["YouTube"]+"?sub_confirmation=1"),("0","guides yet"),"Footage filmed","Guides soon",True)
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
<h2 id="affiliates">How the affiliate links work</h2><p>Some guides link to booking sites such as Klook and Viator. If you book through one of those links I may earn a small commission at no extra cost to you. Those links are marked, they never change what I recommend, and a guide with none of them says "nothing here is sponsored" at the top.</p>
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
<section class="sec" style="padding-top:40px"><div class="wrap"><div class="sechead left"><div><h2>Pick the thing you need to sort out</h2></div><a class="more" href="/guides/china-travel-faq/">Or search every question →</a></div><div class="gcards sm">{qs}</div></div></section>
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
 dict(cat="Tours and tickets",name="Viator",url="https://www.viator.com/?pid=P00328482&mcid=42383&medium=link&campaign=scratchandroam",
      text="Tours, day trips and activities around the world, from the Tripadvisor company. The link opens the Viator home page; search for your city."),
 dict(cat="eSIM and data",name="Firsty",url="https://www.firsty.app/",used=True,picktext="The eSIM I use",code="6TKZ-8RGM",codenote="Referral code: you get €3 off your first purchase over €4, and I get €3 credit.",
      text="The eSIM I use myself. I used Firsty in Japan and in Saudi Arabia with no problems, and I plan to use it in China too. Before China, check in the app how it handles Google and WhatsApp there."),
 dict(cat="eSIM and data",name="Airalo",url="https://airalo.tpm.li/2QR6sBuX",qr="airalo-travel-deal-link-qr-code",
      text="eSIM data plans for travel, bought and installed in an app. The link opens the Airalo app in the App Store."),
 dict(cat="eSIM and data",name="Yesim",url="https://yesim.tpm.li/AfoDqUbw",qr="yesim-travel-deal-link-qr-code",
      text="eSIM data plans for travel, for one country or a region."),
 dict(cat="eSIM and data",name="Saily",url="https://saily.tpm.li/r3wbWW2R",
      text="eSIM data plans for travel, from Nord Security, the company behind NordVPN."),
 dict(cat="VPN and security",name="NordVPN",url="https://go.nordvpn.net/aff_c?offer_id=15&aff_id=159585&url_id=902",used=True,picktext="The VPN I had on our first China trip",
      text="The VPN I had on our first China trip. It needed Wi-Fi to activate again after we landed, so install it, log in and test it at home, and keep a second VPN as a backup. Using a VPN in China sits in a legal grey area."),
 dict(cat="VPN and security",name="ExpressVPN",url="https://go.expressvpn.com/c/8054072/1462856/16063",
      text="A paid VPN app for phone and laptop. If you take a second VPN to China as a backup, install it, log in and test it at home before you fly. Using a VPN in China sits in a legal grey area."),
 dict(cat="VPN and security",name="NordPass",url="https://go.nordpass.io/aff_c?offer_id=488&aff_id=159585&url_id=9356",
      text="A password manager from the same company as NordVPN, for keeping your logins in one place when you travel."),
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
    picks=[d for d in DEALS if d.get("booked") or d.get("used")]
    pk="".join(f'<a class="pk" href="#d-{re.sub("[^a-z0-9]+","-",d["name"].lower())}"><b>{html.escape(d["name"])}</b><span>{html.escape(d.get("picktext") or ("We booked our ERA show tickets here" if d.get("booked") else "I use this"))}{" · code "+html.escape(d["code"]) if d.get("code") else ""}</span></a>' for d in picks)
    for d in sorted(DEALS,key=lambda d:0 if (d.get("booked") or d.get("used")) else 1):
        qr=f'<img class="dqr" src="/img/{d["qr"]}.jpg" alt="QR code for {html.escape(d["name"])}" width="110" height="110" loading="lazy">' if d.get("qr") else ''
        badge='<span class="dbadge booked">We booked here</span>' if d.get("booked") else ('<span class="dbadge booked">I use this</span>' if d.get("used") else '<span class="dbadge">Link only</span>')
        more=f'<a class="dmore" href="{d["more"][0]}">{html.escape(d["more"][1])} →</a>' if d.get("more") else ''
        cards+=f'''<article class="deal" id="d-{re.sub("[^a-z0-9]+","-",d["name"].lower())}" data-cat="{html.escape(d["cat"])}"><div class="dtop"><div><span class="dcat">{html.escape(d["cat"])}</span><h3>{html.escape(d["name"])}</h3>{badge}</div>{qr}</div><p>{html.escape(d["text"])}</p>{('<div class="dcode has"><span>Code</span><b>'+html.escape(d["code"])+'</b><button type="button" data-copy="'+html.escape(d["code"])+'">Copy</button></div><small class="dcn">'+html.escape(d.get("codenote",""))+'</small>') if d.get("code") else '<div class="dcode"><span>Code</span><b>No code needed</b></div>'}<div class="dact"><a class="btn" href="{d["url"]}" rel="{"noopener" if d.get("code") and "tpm.li" not in d["url"] else "sponsored noopener"}" target="_blank">Open {html.escape(d["name"])}</a>{more}</div></article>'''
    return f'''<main>
<section class="phero"><div class="wrap"><nav class="crumbs"><a href="/">Home</a><span>/</span><span>Travel deals</span></nav><p class="eyebrow"><span class="adl">#Ad</span> Travel deals</p><h1>My travel links, all in one place</h1><p class="lede">Tickets, eSIMs, airport transfers and flights. These are my partner links: if you book through one, I may earn a small commission at no extra cost to you. Each card says whether we booked there or I use it myself.</p></div></section>
<section class="sec" style="padding-top:8px"><div class="wrap">
<div class="dnote"><b>Before you click</b><p>Where I have a code, it is on the card with a Copy button. For China, read my <a href="/guides/china-travel-apps/">China travel apps guide</a> before you buy an eSIM: check that the plan routes data outside China, or Google and WhatsApp will not work. <a href="/affiliate-disclosure/">How affiliate links work on this site</a>.</p></div>
<h2 class="pkh">What I actually use</h2><div class="pks">{pk}</div>
<h2 class="pkh">Every link</h2><div class="chips" role="group" aria-label="Filter by category">{chips}</div>
<div class="deals" id="deals">{cards}</div>
</div></section>
{band_b(SOC)}
</main>
<script>(function(){{var b=document.querySelectorAll(".chips .chip"),c=document.querySelectorAll(".deal");b.forEach(function(x){{x.addEventListener("click",function(){{b.forEach(function(y){{y.classList.toggle("on",y===x)}});var f=x.getAttribute("data-f");c.forEach(function(d){{d.hidden=!(f==="all"||d.getAttribute("data-cat")===f)}})}})}})}})();</script>'''


# ===== Compact pick inside the step where the reader decides =====
def _pick_firsty(more="#links"):
    return ('<div class="spick"><span class="adl">#Ad</span><div><b>My pick: Firsty</b> <span class="dbadge booked">I use this</span>'
            '<p>The eSIM I used in Japan and Saudi Arabia. For China, check in the app how it handles Google and WhatsApp before you buy.</p>'
            '<div class="dcode has"><span>Code</span><b>6TKZ-8RGM</b><button type="button" data-copy="6TKZ-8RGM">Copy</button></div>'
            '<small class="dcn">You get €3 off your first purchase over €4, and I get €3 credit.</small>'
            f'<a class="btn" href="https://www.firsty.app/" rel="noopener" target="_blank">Open Firsty</a> <a class="smore" href="{more}">Other eSIMs →</a></div></div>')
def _pick_nordvpn():
    return ('<div class="spick"><span class="adl">#Ad</span><div><b>The VPN I had: NordVPN</b> <span class="dbadge booked">I use this</span>'
            '<p>On our first trip it needed Wi-Fi to activate again after we landed. Install it, log in and test it at home, and keep a second VPN as a backup.</p>'
            '<a class="btn" href="https://go.nordvpn.net/aff_c?offer_id=15&aff_id=159585&url_id=902" rel="sponsored noopener" target="_blank">Open NordVPN</a> <a class="smore" href="/travel-deals/">All my links →</a></div></div>')
STEP_PICKS={"china-travel-apps":{8:_pick_firsty(),9:_pick_nordvpn()},"china-before-you-fly-checklist":{4:_pick_firsty()}}

# ===== "Links for this guide" boxes (partner links that fit the guide's topic) =====
GUIDE_DEALS={
 "china-travel-apps":(["Firsty","Airalo","Yesim","Saily","NordVPN","ExpressVPN"],"eSIMs for step 8, and two VPNs for step 9: the one I had, and a second one as a backup. Whichever you pick, read the plan description first: for China you want one that routes data outside China, so Google and WhatsApp keep working."),
 "top-25-china-apps":(["Firsty","Airalo","Yesim","Saily","NordVPN"],"eSIMs for pass number 4, and the VPN I had. For China, read the plan description first: you want one that routes data outside China."),
 "first-time-in-china":(["Firsty","Airalo","Kiwi.com","Welcome Pickups","GetTransfer"],"An eSIM for the internet on landing, flights, and a transfer from the airport so the first hour is easy."),
 "china-before-you-fly-checklist":(["Firsty","Airalo","NordVPN","ExpressVPN","Welcome Pickups","GetTransfer"],"An eSIM and two VPNs for step 4, and an airport transfer for step 10, so your first day stays simple."),
 "food-delivery-in-china-for-foreigners-meituan":(["Firsty","Airalo"],"You need mobile data to order, chat with the rider and pay, so sort your eSIM before you fly."),
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
    return (f'<h2 id="links">Links for this guide</h2><p>{html.escape(note)} These are my partner links: if you book through one, I may earn a small commission at no extra cost to you. '
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


# ===== China travel questions answered (help centre, step 2) =====
# Data: src/china-answers.json (one record per question). Short answers, last-checked date and source on each;
# longer steps live in the guides. Records with status "needs official check" show a visible note.
import json as _json, datetime as _dt
FAQ_GROUPS=["Before I fly","Money","Phone and internet","Getting around","In the city","Problems"]
FAQ_EXTRA_LINKS={"spice-tolerance":("/guides/build-spice-tolerance-before-china/","Build spice tolerance before China")}
def faq_data():
    return _json.load(open('src/china-answers.json',encoding='utf-8'))["records"]
def _fmt_date(s):
    d=_dt.date.fromisoformat(s); return f"{d.day} {d.strftime('%b %Y')}"
def faq_checked():
    return max(r["chk"] for r in faq_data())
def faq_b(SOC):
    recs=faq_data(); by={r["id"]:r for r in recs}
    chips='<button type="button" class="chip on" data-f="all">All</button>'+"".join(f'<button type="button" class="chip" data-f="{html.escape(g)}">{html.escape(g)}</button>' for g in FAQ_GROUPS if any(r["group"]==g for r in recs))
    secs=""
    for g in FAQ_GROUPS:
        rs=[r for r in recs if r["group"]==g]
        if not rs: continue
        items=""
        for r in rs:
            key=html.escape(" ".join([r["q"]]+r["alts"]+[_t(r["a"])]).lower(),quote=True)
            links=[]
            if r.get("slug"): links.append(f'<a class="fqg" href="/guides/{r["slug"]}/">Read the full guide →</a>')
            if r.get("yt"): links.append(f'<a class="fqv" href="https://www.youtube.com/watch?v={r["yt"]}" rel="noopener">Watch the video</a>')
            rel=[]
            for x in r.get("rel",[]):
                if x in by: rel.append(f'<a href="#q-{x}">{html.escape(by[x]["q"])}</a>')
                elif x in FAQ_EXTRA_LINKS: rel.append(f'<a href="{FAQ_EXTRA_LINKS[x][0]}">{html.escape(FAQ_EXTRA_LINKS[x][1])}</a>')
            warn='<p class="fqwarn"><b>Check before you rely on it.</b> Rules change. Look at the official page for your passport and your travel date.</p>' if r["st"].startswith("needs official check") else ''
            items+=f'''<details class="fq" id="q-{r["id"]}" data-g="{html.escape(g)}" data-k="{key}"><summary>{html.escape(r["q"])}</summary><div class="fqb"><p>{html.escape(r["a"])}</p>{warn}<div class="fqact">{"".join(links)}</div>{('<p class="fqrel"><b>Related:</b> '+" · ".join(rel)+'</p>') if rel else ''}{('<p class="fqlinks"><b>Official pages:</b> '+" · ".join(f'<a href="{html.escape(u)}" rel="noopener" target="_blank">{html.escape(l)}</a>' for l,u in r["links"])+'</p>') if r.get("links") else ''}<p class="fqmeta">Checked {_fmt_date(r["chk"])}. Source: {html.escape(r["src"])}.</p></div></details>'''
        secs+=f'<section class="fqsec" data-g="{html.escape(g)}"><h2>{html.escape(g)}</h2>{items}</section>'
    return f'''<main>
<section class="phero"><div class="wrap"><nav class="crumbs"><a href="/">Home</a><span>/</span><a href="/china/">China</a><span>/</span><span>Questions answered</span></nav><p class="eyebrow">China Travel Companion</p><h1>China travel questions answered</h1><p class="lede">Short answers to what first-timers ask before and during a China trip. Each one says when I last checked it and where it comes from, and links to the full guide when I have one.</p></div></section>
<section class="sec" style="padding-top:8px"><div class="wrap">
<div class="dnote"><b>Read this first</b><p>Rules, prices and apps change. Every answer carries its checked date, and anything about visas needs a look at the official page for your own passport. I add questions as I film and test more of China.</p></div>
<div class="fqsearch"><label for="fqq">What do you need help with?</label><input id="fqq" type="search" placeholder="Try: arrival card, eSIM, metro, VPN" autocomplete="off"></div>
<div class="chips" role="group" aria-label="Filter by stage">{chips}</div>
<p class="fqcount" id="fqcount" aria-live="polite"></p>
<div id="fqlist">{secs}</div>
<p class="tmeta">Also useful: the <a href="/china/tools/">yuan converter and Chinese clothing size finder</a>.</p>
<p class="fqnone" id="fqnone" hidden>No answer matches that yet. Try fewer words, or check the <a href="/china/">China guides</a>.</p>
</div></section>
{band_b(SOC)}
</main>
<script>(function(){{var q=document.getElementById("fqq"),chips=[].slice.call(document.querySelectorAll(".chips .chip")),items=[].slice.call(document.querySelectorAll(".fq")),secs=[].slice.call(document.querySelectorAll(".fqsec")),cnt=document.getElementById("fqcount"),none=document.getElementById("fqnone"),g="all";function run(){{var t=q.value.toLowerCase().trim().split(/\\s+/).filter(Boolean),n=0;items.forEach(function(d){{var ok=(g==="all"||d.getAttribute("data-g")===g),k=d.getAttribute("data-k");t.forEach(function(w){{if(k.indexOf(w)<0)ok=false}});d.hidden=!ok;if(ok)n++}});secs.forEach(function(s){{s.hidden=!s.querySelector(".fq:not([hidden])")}});none.hidden=n>0;cnt.textContent=(t.length||g!=="all")?n+(n===1?" answer":" answers"):""}}q.addEventListener("input",run);chips.forEach(function(c){{c.addEventListener("click",function(){{chips.forEach(function(y){{y.classList.toggle("on",y===c)}});g=c.getAttribute("data-f");run()}})}});if(location.hash){{var e=document.getElementById(location.hash.slice(1));if(e&&e.tagName==="DETAILS")e.open=true}}window.addEventListener("hashchange",function(){{var e=document.getElementById(location.hash.slice(1));if(e&&e.tagName==="DETAILS")e.open=true}})}})();</script>'''
def faq_schema(SITE):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":r["q"],"acceptedAnswer":{"@type":"Answer","text":r["a"]}} for r in faq_data()]}

# ===== China tools: money, units, clothing sizes =====
TOOLS_RATE_FALLBACK={"base":"EUR","cny":7.4343,"date":"27 October 2026"}
_TOOLS_HTML='''<main>
<section class="phero"><div class="wrap"><nav class="crumbs"><a href="/">Home</a><span>/</span><a href="/china/">China</a><span>/</span><span>Tools</span></nav><p class="eyebrow">China Travel Companion</p><h1>China money, units and clothing size tools</h1><p class="lede">Three small tools for shopping and paying in China. They run in your browser, so they also work once the page has loaded and your signal drops.</p></div></section>
<section class="sec" style="padding-top:8px"><div class="wrap">
<div class="dnote"><b>Read this first</b><p>Rates change daily and your bank adds its own fee. Use these numbers to judge a price, not to budget to the cent. For sizes, the seller's own size chart always wins.</p></div>
<div class="tool" id="money"><h2>Yuan (RMB) and your currency</h2>
<div class="trow"><label>Amount<input id="mAmt" type="number" inputmode="decimal" value="100" min="0"></label>
<label>From<select id="mFrom"><option value="CNY">Chinese yuan (CNY)</option><option value="EUR">Euro (EUR)</option><option value="USD">US dollar (USD)</option><option value="GBP">Pound (GBP)</option></select></label>
<label>To<select id="mTo"><option value="EUR">Euro (EUR)</option><option value="USD">US dollar (USD)</option><option value="GBP">Pound (GBP)</option><option value="CNY">Chinese yuan (CNY)</option></select></label></div>
<p class="tres" id="mOut" aria-live="polite"></p><p class="tmeta" id="mMeta"></p>
<div class="ttab" id="mTab"></div>
<p class="tmeta">Live rate: <a href="https://frankfurter.dev" rel="noopener" target="_blank">Frankfurter</a>, which publishes European Central Bank reference rates. If it cannot load, the page uses the last ECB euro rate I saved ({FBDATE}) and only converts euro and yuan.</p></div>
<div class="tool" id="units"><h2>Units and temperature</h2>
<div class="trow"><label>Kilometres<input class="u" data-k="km" type="number" inputmode="decimal" placeholder="km"></label><label>Miles<input class="u" data-k="mi" type="number" inputmode="decimal" placeholder="miles"></label></div>
<div class="trow"><label>Celsius<input class="u" data-k="c" type="number" inputmode="decimal" placeholder="°C"></label><label>Fahrenheit<input class="u" data-k="f" type="number" inputmode="decimal" placeholder="°F"></label></div>
<div class="trow"><label>Kilograms<input class="u" data-k="kg" type="number" inputmode="decimal" placeholder="kg"></label><label>Pounds<input class="u" data-k="lb" type="number" inputmode="decimal" placeholder="lb"></label></div>
<div class="trow"><label>Centimetres<input class="u" data-k="cm" type="number" inputmode="decimal" placeholder="cm"></label><label>Inches<input class="u" data-k="in" type="number" inputmode="decimal" placeholder="inches"></label></div>
<div class="trow"><label>Jin (斤)<input class="u" data-k="jin" type="number" inputmode="decimal" placeholder="jin"></label><label>Kilograms (from jin)<input class="u" data-k="kgj" type="number" inputmode="decimal" placeholder="kg"></label></div>
<p class="tmeta">China uses metric. Type in either box and the other fills in. Chinese shops often sell by the <i>jin</i> (斤): 1 jin is 500 g.</p></div>
<div class="tool" id="sizes"><h2>Clothing size finder</h2>
<p>Chinese clothing labels follow the national standard GB/T 1335 and look like <b>170/88A</b>: <b>170</b> is the height in cm the garment is cut for, <b>88</b> is the chest or bust in cm, and the letter is the fit. <b>A</b> is regular, <b>Y</b> is slimmer and <b>B</b> is fuller.</p>
<div class="trow"><label>Height (cm)<input id="sH" type="number" inputmode="decimal" placeholder="168"></label><label>Chest or bust (cm)<input id="sC" type="number" inputmode="decimal" placeholder="90"></label><label>Fit<select id="sF"><option value="A">A, regular</option><option value="Y">Y, slimmer</option><option value="B">B, fuller</option></select></label></div>
<p class="tres" id="sOut" aria-live="polite">Fill in height and chest to see your label.</p>
<h3>Reading a real Taobao size sheet</h3>
<p>Many Taobao shirts and jackets do not use 170/88A at all. This one, a men's-style shirt sized by collar number, shows what you will see after tapping 尺码信息 (size info) on a listing. Sizes 39 to 46 are collar numbers, and the seller recommends 42.</p>
<div class="twrap"><table class="szt"><thead><tr><th>Size</th><th>Height cm</th><th>Weight kg</th><th>Shoulder cm</th><th>Chest cm</th></tr></thead><tbody>
<tr><td>39</td><td>158-173</td><td>50-55</td><td>42.1</td><td>96</td></tr>
<tr><td>40</td><td>158-178</td><td>55-62.5</td><td>43.3</td><td>100</td></tr>
<tr><td>41</td><td>158-188</td><td>62.5-70</td><td>44.5</td><td>104</td></tr>
<tr><td><b>42</b></td><td>163-188</td><td>70-77.5</td><td>45.7</td><td>108</td></tr>
<tr><td>43</td><td>163-188</td><td>77.5-85</td><td>46.9</td><td>112</td></tr>
<tr><td>44</td><td>163-188</td><td>85-92.5</td><td>48.1</td><td>116</td></tr>
<tr><td>45</td><td>168-188</td><td>92.5-100</td><td>49.3</td><td>120</td></tr>
<tr><td>46</td><td>173-188</td><td>100-110</td><td>50.5</td><td>124</td></tr>
</tbody></table></div>
<p><b>Words to find on the sheet</b></p>
<div class="twrap"><table class="szt"><thead><tr><th>Chinese</th><th>Pinyin</th><th>Means</th></tr></thead><tbody>
<tr><td>尺码信息</td><td>chǐmǎ xìnxī</td><td>Size information</td></tr>
<tr><td>身高体重对照表</td><td>shēngāo tǐzhòng duìzhào biǎo</td><td>Height and weight chart: find your height row and weight column, the cell is your size</td></tr>
<tr><td>尺寸表</td><td>chǐcùn biǎo</td><td>Measurement table for each size</td></tr>
<tr><td>身高 / 体重</td><td>shēngāo / tǐzhòng</td><td>Height / weight</td></tr>
<tr><td>肩宽 / 胸围</td><td>jiānkuān / xiōngwéi</td><td>Shoulder width / chest</td></tr>
<tr><td>买家尺码参考</td><td>mǎijiā chǐmǎ cānkǎo</td><td>What real buyers of this height and weight bought</td></tr>
<tr><td>100%买家认为尺码标准</td><td></td><td>100% of buyers say the size is true to the label. The orange number is the recommended size</td></tr>
<tr><td>DZ</td><td></td><td>Most likely 定制 (made to measure). Ask the seller before ordering</td></tr>
</tbody></table></div>
<p class="tmeta">How I would use it: start with the weight grid, then check the buyer reference rows for your own height and weight, then read the size note at the bottom. The sheet itself says different ways of measuring can differ by 2 to 4 cm. I have not confirmed whether the chest number is the body or the garment, so ask the seller (客服) if it matters. Sheet seen on Taobao on 29 October 2026.</p>
<h3>Example: a bra size chart</h3>
<p>Bra sheets give two things: the underbust (下围) and the difference between bust and underbust (胸围和下围差). The band is the underbust rounded to a 5, and the cup comes from the difference. This sheet, for a wired and wire-free set, lists the brand's own sizes next to the China size.</p>
<div class="twrap"><table class="szt"><thead><tr><th>Underbust cm</th><th>Band, brand</th><th>Band, China</th></tr></thead><tbody>
<tr><td>63-67</td><td>30</td><td>65</td></tr><tr><td>68-72</td><td>32</td><td>70</td></tr><tr><td>73-77</td><td>34</td><td>75</td></tr><tr><td>78-82</td><td>36</td><td>80</td></tr><tr><td>83-87</td><td>38</td><td>85</td></tr></tbody></table></div>
<div class="twrap"><table class="szt"><thead><tr><th>Bust minus underbust cm</th><th>Cup, brand</th><th>Cup, China</th></tr></thead><tbody>
<tr><td>6.1-8</td><td>AA</td><td>AA</td></tr><tr><td>8.1-10.5</td><td>A</td><td>A</td></tr><tr><td>10.6-13</td><td>B</td><td>B</td></tr><tr><td>13.1-16</td><td>C</td><td>C</td></tr><tr><td>16.1-19</td><td>D</td><td>D</td></tr><tr><td>19.1-22</td><td>DD</td><td>E</td></tr><tr><td>22.1-25</td><td>DDD</td><td>F</td></tr></tbody></table></div>
<p class="tmeta">So 32DD and 70E are the same bra, and a 75B is a 34B. Underbust and bust are measured in cm. The listing also pairs briefs with bra sizes: 32 is XS, 34 is S, 36 is M and 38 is L. Not every cup letter exists in every band on this sheet, so if your size is missing, ask the seller.</p>
<p><b>Words on a bra listing</b></p>
<div class="twrap"><table class="szt"><thead><tr><th>Chinese</th><th>Pinyin</th><th>Means</th></tr></thead><tbody>
<tr><td>文胸 / 内衣</td><td>wénxiōng / nèiyī</td><td>Bra / underwear</td></tr>
<tr><td>下围</td><td>xiàwéi</td><td>Underbust</td></tr>
<tr><td>胸围</td><td>xiōngwéi</td><td>Bust or chest</td></tr>
<tr><td>罩杯</td><td>zhàobēi</td><td>Cup</td></tr>
<tr><td>有钢圈 / 无钢圈</td><td>yǒu gāngquān / wú gāngquān</td><td>Wired / wire-free</td></tr>
<tr><td>聚拢程度: 常规, 微聚拢, 聚拢, 超聚拢</td><td>jùlǒng chéngdù</td><td>How much lift: regular, slight, push-up, extra push-up</td></tr>
<tr><td>罩杯厚度: 薄模杯, 厚模杯</td><td>zhàobēi hòudù</td><td>Cup padding: thin moulded, thick moulded</td></tr>
<tr><td>内裤 / 套装</td><td>nèikù / tàozhuāng</td><td>Briefs / set</td></tr>
<tr><td>锦纶, 氨纶, 聚酯纤维, 棉, 莫代尔</td><td></td><td>Nylon, spandex, polyester, cotton, modal</td></tr>
</tbody></table></div>
<h3>Example: a dress with S to XL</h3>
<p>Here the sizes are letters, and the cm columns are what matter: 裙长 dress length, 胸围 chest, 肩宽 shoulder, 腰围 waist, 袖长 sleeve length. This seller also shows the model: 171 cm, 50 kg, wearing M (三围, the three measurements, are bust, waist and hip: 81, 63.5 and 94).</p>
<div class="twrap"><table class="szt"><thead><tr><th>Size</th><th>Length</th><th>Chest</th><th>Shoulder</th><th>Waist</th><th>Sleeve</th></tr></thead><tbody>
<tr><td>S</td><td>134</td><td>72-96</td><td>33</td><td>54-76</td><td>61</td></tr><tr><td>M</td><td>135</td><td>76-100</td><td>34</td><td>58-80</td><td>62</td></tr><tr><td>L</td><td>136</td><td>80-104</td><td>35</td><td>62-84</td><td>63</td></tr><tr><td>XL</td><td>137</td><td>84-108</td><td>36</td><td>66-88</td><td>64</td></tr></tbody></table></div>
<p class="tmeta">The chest and waist are ranges, which usually means a stretchy fabric, but the sheet does not say so. The seller notes hand measuring can be 1 to 2 cm off (手工测量可能存在1-2cm误差).</p>
<h3>Watch the weight unit: jin, not kilos</h3>
<p>A second dress sheet has a height and weight grid. Its weight row is labelled 体重 (斤), which is <b>jin</b>. One jin is half a kilo, so 100 jin is 50 kg. If you read 100 as kilos you will order far too big. The measurement table above it on the same sheet looks like kilos (45 for the 155 cm size), so check the unit on every grid.</p>
<div class="twrap"><table class="szt"><thead><tr><th>Height cm</th><th>85-90 jin (42.5-45 kg)</th><th>100-105 jin (50-52.5 kg)</th><th>115-120 jin (57.5-60 kg)</th></tr></thead><tbody>
<tr><td>150-155</td><td>S</td><td>M</td><td>L</td></tr><tr><td>160-165</td><td>S</td><td>S</td><td>L</td></tr><tr><td>170-175</td><td>blank</td><td>M</td><td>M</td></tr></tbody></table></div>
<p class="tmeta">Blank cells mean the seller does not make a size for that height and weight. The note under the grid says to choose by how you like clothes to fit (MM根据穿衣习惯选择尺码, where MM is slang for a young woman). Sheets seen on Taobao on 29 October 2026. I have not ordered any of these items.</p>
<h3>Example: shoe sizes</h3>
<p>Chinese shoe sizes are easier than clothes. The <b>标准码</b> (standard size) is the same number as an EU size, so a 38 is a 38. The <b>国际码</b> (international code) is the foot length in millimetres, so 240 means 24.0 cm. Always compare your own foot length in cm with the seller's 脚长 column.</p>
<p><b>标准女鞋尺寸表, standard women's shoes</b></p>
<div class="twrap"><table class="szt"><thead><tr><th>国际码 (mm)</th><th>标准码 (EU)</th><th>脚长 foot length cm</th><th>脚宽 foot width cm</th></tr></thead><tbody><tr><td>215</td><td>33</td><td>21.0-21.4</td><td>7.5-7.9</td></tr><tr><td>220</td><td>34</td><td>21.5-22.0</td><td>8.0-8.4</td></tr><tr><td>225</td><td>35</td><td>22.1-22.5</td><td>8.5</td></tr><tr><td>230</td><td>36</td><td>22.6-23.0</td><td>8.6-9.0</td></tr><tr><td>235</td><td>37</td><td>23.1-23.5</td><td>9.1</td></tr><tr><td>240</td><td>38</td><td>23.6-24.0</td><td>9.2-9.5</td></tr><tr><td>245</td><td>39</td><td>24.1-24.5</td><td>9.6-10.0</td></tr><tr><td>250</td><td>40</td><td>24.6-25.0</td><td>10.1-10.5</td></tr></tbody></table></div>
<p><b>标准男鞋尺寸表, standard men's shoes</b></p>
<div class="twrap"><table class="szt"><thead><tr><th>国际码 (mm)</th><th>标准码 (EU)</th><th>脚长 foot length cm</th><th>脚宽 foot width cm</th></tr></thead><tbody><tr><td>240</td><td>38</td><td>23.5-24</td><td>9.2-9.5</td></tr><tr><td>245</td><td>39</td><td>24-24.5</td><td>9.6-10</td></tr><tr><td>250</td><td>40</td><td>24.5-25</td><td>10.1-10.5</td></tr><tr><td>255</td><td>41</td><td>25-25.5</td><td>10.6-11</td></tr><tr><td>260</td><td>42</td><td>25.5-26</td><td>11.1-11.5</td></tr><tr><td>265</td><td>43</td><td>26-26.5</td><td>11.6-12</td></tr><tr><td>270</td><td>44</td><td>26.5-27</td><td>12.1-12.5</td></tr></tbody></table></div>
<p>A running-shoe listing from a different brand gave US, EU and cm side by side:</p>
<div class="twrap"><table class="szt"><thead><tr><th>Men US</th><th>Men EU</th><th>Men cm</th></tr></thead><tbody><tr><td>6</td><td>38.5</td><td>24</td></tr><tr><td>6.5</td><td>39</td><td>24.5</td></tr><tr><td>7</td><td>40</td><td>25</td></tr><tr><td>7.5</td><td>40.5</td><td>25.5</td></tr><tr><td>8</td><td>41</td><td>26</td></tr><tr><td>8.5</td><td>42</td><td>26.5</td></tr><tr><td>9</td><td>42.5</td><td>27</td></tr><tr><td>9.5</td><td>43</td><td>27.5</td></tr><tr><td>10</td><td>44</td><td>28</td></tr><tr><td>10.5</td><td>44.5</td><td>28.5</td></tr><tr><td>11</td><td>45</td><td>29</td></tr><tr><td>11.5</td><td>45.5</td><td>29.5</td></tr><tr><td>12</td><td>46</td><td>30</td></tr></tbody></table></div>
<div class="twrap"><table class="szt"><thead><tr><th>Women US</th><th>Women EU</th><th>Women cm</th></tr></thead><tbody><tr><td>5</td><td>35.5</td><td>22</td></tr><tr><td>5.5</td><td>36</td><td>22.5</td></tr><tr><td>6</td><td>36.5</td><td>23</td></tr><tr><td>6.5</td><td>37.5</td><td>23.5</td></tr><tr><td>7</td><td>38</td><td>24</td></tr><tr><td>7.5</td><td>38.5</td><td>24.5</td></tr><tr><td>8</td><td>39</td><td>25</td></tr><tr><td>8.5</td><td>40</td><td>25.5</td></tr><tr><td>9</td><td>40.5</td><td>26</td></tr></tbody></table></div>
<p class="tmeta">The two sheets do not agree. On the first, men's EU 42 is a foot length of 25.5-26 cm. On the second, men's EU 42 is 26.5 cm. I think the first measures your foot and the second measures the shoe, but neither sheet says so. That is why the cm number matters more than the size name: measure your foot standing on paper from heel to longest toe, then use the seller's own sheet. Between two sizes, go up one. That same running-shoe seller says the shoes run true to size, and advises sizing up if your feet are wide (脚宽大建议选择大一码).</p>
<p><b>Words on a shoe listing</b></p>
<div class="twrap"><table class="szt"><thead><tr><th>Chinese</th><th>Pinyin</th><th>Means</th></tr></thead><tbody>
<tr><td>尺码对照表 / 尺码参考</td><td>chǐmǎ duìzhào biǎo</td><td>Size comparison chart</td></tr>
<tr><td>男鞋 / 女鞋</td><td>nánxié / nǚxié</td><td>Men's shoes / women's shoes</td></tr>
<tr><td>脚长 / 脚宽</td><td>jiǎo cháng / jiǎo kuān</td><td>Foot length / foot width</td></tr>
<tr><td>美国码 / 欧码</td><td>Měiguó mǎ / Ōu mǎ</td><td>US size / EU size</td></tr>
<tr><td>尺码建议</td><td>chǐmǎ jiànyì</td><td>Sizing advice</td></tr>
<tr><td>不支持七天无理由退换</td><td>bù zhīchí qī tiān wú lǐyóu tuìhuàn</td><td>No 7-day return without a reason</td></tr>
</tbody></table></div>
<p class="tmeta"><b>Check returns before you buy shoes.</b> The running-shoe listing warns that shoes which are worn, washed or have the tag removed, in a way that affects resale, are not covered by the 7-day no-reason return, unless there is a quality problem. Try them on indoors on a clean floor, and ask the seller (客服) if you are unsure. Sheets seen on Taobao on 29 October 2026. The text on the second sheet is partly cut off at the edge, so I have only translated what I could read.</p>
<h3>Women's tops, roughly</h3>
<div class="twrap"><table class="szt"><thead><tr><th>China label</th><th>Letter</th><th>Bust cm</th><th>EU</th><th>UK</th><th>US</th></tr></thead><tbody>
<tr><td>155/80A</td><td>XS</td><td>80-83</td><td>32-34</td><td>4-6</td><td>0-2</td></tr>
<tr><td>160/84A</td><td>S</td><td>84-87</td><td>36-38</td><td>8-10</td><td>4-6</td></tr>
<tr><td>165/88A</td><td>M</td><td>88-91</td><td>40-42</td><td>12-14</td><td>8-10</td></tr>
<tr><td>168/92A</td><td>L</td><td>92-96</td><td>42-44</td><td>16-18</td><td>12-14</td></tr>
<tr><td>170/96A</td><td>XL</td><td>96-100</td><td>44-46</td><td>20</td><td>16</td></tr>
<tr><td>172/100A</td><td>XXL</td><td>100-104</td><td>46-48</td><td>22</td><td>18</td></tr>
</tbody></table></div>
<h3>Men's jackets and tops, roughly</h3>
<div class="twrap"><table class="szt"><thead><tr><th>China label</th><th>Letter</th><th>Chest cm</th><th>Height cm</th><th>EU</th></tr></thead><tbody>
<tr><td>165/84A</td><td>S</td><td>84-87</td><td>163-167</td><td>44</td></tr>
<tr><td>170/88A</td><td>M</td><td>88-91</td><td>168-172</td><td>46</td></tr>
<tr><td>175/92A</td><td>L</td><td>92-95</td><td>173-177</td><td>48</td></tr>
<tr><td>180/96A</td><td>XL</td><td>96-99</td><td>178-182</td><td>50</td></tr>
<tr><td>185/100A</td><td>XXL</td><td>100-103</td><td>183-187</td><td>52</td></tr>
<tr><td>190/104A</td><td>3XL</td><td>104-107</td><td>188-192</td><td>54</td></tr>
</tbody></table></div>
<p class="tmeta">Source: the label structure and the size tables come from <a href="https://www.travelofchina.com/size-chart-for-china-clothes/" rel="noopener" target="_blank">Travel of China's size chart guide</a>, which cites GB/T 1335. Checked 29 October 2026. I have not tested these against garments myself. Trust the centimetre columns over the letter and country sizes, and measure your own chest. Taobao sellers usually post their own chart, and many brands cut smaller than the standard, so between two sizes I would go up. Trousers are not covered yet.</p></div>
</div></section>
{BAND}
</main>
<script>(function(){
var FB={FBJSON};var R=null,live=false;
var money=["CNY","EUR","USD","GBP"];
function fmt(n,c){try{return new Intl.NumberFormat("en-IE",{style:"currency",currency:c,maximumFractionDigits:2}).format(n)}catch(e){return n.toFixed(2)+" "+c}}
function rate(a,b){if(a===b)return 1;if(!R||!R[a]||!R[b])return null;return R[b]/R[a]}
function setFallback(){R={EUR:1,CNY:FB.cny};live=false}
function money_run(){var amt=parseFloat(document.getElementById("mAmt").value),a=document.getElementById("mFrom").value,b=document.getElementById("mTo").value,out=document.getElementById("mOut"),tab=document.getElementById("mTab");
var r=rate(a,b);if(isNaN(amt)||amt<0){out.textContent="Type an amount.";tab.innerHTML="";return}
if(r===null){out.textContent="Offline: I can only convert euro and yuan right now.";tab.innerHTML="";return}
out.textContent=fmt(amt,a)+" is about "+fmt(amt*r,b);
var rows="";[10,50,100,200,500,1000].forEach(function(x){rows+="<tr><td>"+fmt(x,a)+"</td><td>"+fmt(x*r,b)+"</td></tr>"});
tab.innerHTML='<table class="szt"><thead><tr><th>'+a+'</th><th>'+b+'</th></tr></thead><tbody>'+rows+'</tbody></table>'}
function meta(d){document.getElementById("mMeta").textContent=live?("Live ECB-based rate for "+d+". Your bank or card will add a fee, so expect a little less."):("Saved ECB rate from "+FB.date+" (euro and yuan only). Rates change, so check your bank.")}
setFallback();meta();money_run();
try{fetch("https://api.frankfurter.dev/v1/latest?base=CNY&symbols=EUR,USD,GBP").then(function(r){if(!r.ok)throw 0;return r.json()}).then(function(j){if(!j||!j.rates||!j.rates.EUR||!j.rates.USD||!j.rates.GBP)throw 0;R={CNY:1,EUR:j.rates.EUR,USD:j.rates.USD,GBP:j.rates.GBP};live=true;meta(j.date);money_run()}).catch(function(){})}catch(e){}
["mAmt","mFrom","mTo"].forEach(function(i){document.getElementById(i).addEventListener("input",money_run)});
var U={km:["mi",function(v){return v*0.621371},function(v){return v/0.621371}],c:["f",function(v){return v*9/5+32},function(v){return (v-32)*5/9}],kg:["lb",function(v){return v*2.204623},function(v){return v/2.204623}],jin:["kgj",function(v){return v/2},function(v){return v*2}],cm:["in",function(v){return v/2.54},function(v){return v*2.54}]};
var inp={};[].forEach.call(document.querySelectorAll(".u"),function(e){inp[e.getAttribute("data-k")]=e});
Object.keys(U).forEach(function(k){var o=U[k][0];inp[k].addEventListener("input",function(){var v=parseFloat(inp[k].value);inp[o].value=isNaN(v)?"":Math.round(U[k][1](v)*100)/100});inp[o].addEventListener("input",function(){var v=parseFloat(inp[o].value);inp[k].value=isNaN(v)?"":Math.round(U[k][2](v)*100)/100})});
function size_run(){var h=parseFloat(document.getElementById("sH").value),c=parseFloat(document.getElementById("sC").value),f=document.getElementById("sF").value,o=document.getElementById("sOut");
if(isNaN(h)||isNaN(c)){o.textContent="Fill in height and chest to see your label.";return}
if(h<120||h>210||c<60||c>140){o.textContent="Check the numbers: height and chest are both in centimetres.";return}
var H=Math.round(h/5)*5,C=Math.round(c/4)*4;o.innerHTML="Your label is about <b>"+H+"/"+C+f+"</b>. Heights step in 5 cm and chests in 4 cm. If you sit between two sizes, go up one.<br>If the shop only lists letters, use the tables below and match on centimetres."}
["sH","sC","sF"].forEach(function(i){document.getElementById(i).addEventListener("input",size_run)});
})();</script>'''
def tools_b(SOC):
    return (_TOOLS_HTML.replace('{FBJSON}',_json.dumps(TOOLS_RATE_FALLBACK)).replace('{FBDATE}',TOOLS_RATE_FALLBACK["date"]).replace('{BAND}',band_b(SOC)))
