# Pages for scratchandroam.com. Facts only from Natali's own guides and the sources listed on each page.

# ---------------------------------------------------------------------------
# GUIDE REGISTRY. Every guide() must have an entry here, or the build stops.
# This one list feeds the home page tickets and rows, the /china/ sections, the
# Shopping menu link and the footer "Guides" column, so a new guide shows up
# everywhere without hand-editing five places.
#   sec: "before" (setup guides, top of /china/ and home tickets),
#        "shop" (Shopping section on /china/, "Shopping" menu link),
#        "place" (Shanghai answers rows).
#   Question cards (qs grids) stay at 5 plus "Coming next": choose which five in
#   QS_HOME and QS_CHINA below, and add the guide's card to QCARDS.
# ---------------------------------------------------------------------------
CARDS=[
 dict(slug="first-time-in-china",sec="before",img="first-time-in-china-13-things-before-you-fly",alt="Cover of the 13 things before China guide, with the 200 yuan fee card",num="GUIDE 13",meta=("VIDEO + CHECKLIST","6 MIN"),t="First time in China: 13 things to set up before you fly",p="Visa-free list, arrival card, Alipay and WeChat, cards, cash, trains, maps, packing.",short="First time in China: 13 things"),
 dict(slug="china-visa-free-30-days",sec="before",img="china-visa-free-30-days-departure-board-cover-4x5",alt="Cover of the China visa free 30 days guide: a departure board reading China, visa free, to 31 Dec, with the China flag",num="VISA-FREE",meta=("VIDEO + ANSWERS","30 DAYS"),t="China visa free 30 days: Irish, UK and EU passports",p="Who gets 30 days, until when, what to show at the border, and what you cannot extend.",short="China visa free 30 days"),
 dict(slug="china-dos-and-donts",sec="before",img="china-will-take-your-drone-15-dos-and-donts",alt="Cover of the China do's and don'ts guide: China will take your drone, 15 do's and don'ts",num="15 RULES",meta=("LIST","15 DO'S AND DON'TS"),t="China do's and don'ts: what not to bring, and what not to do",p="What customs and security take off you, the table manners that get stares, and what to pack or just buy there.",short="China do's and don'ts"),
 dict(slug="china-travel-apps",sec="before",img="china-travel-apps-12-apps-to-set-up-before-china",alt="Cover of the China travel apps guide, 12 apps to set up before China with a Nanjing Road night photo and the China flag",num="APPS LIST",meta=("LIST + VIDEO","12 APPS"),t="Apps to download before you go to China: the full list",p="Paying, maps, taxis, trains, what to set up at home, the hidden gems inside Alipay, and what to skip.",short="China travel apps"),
 dict(slug="top-25-china-apps",sec="before",img="top-25-china-apps-boarding-pass-cover",alt="Cover of the top 25 China apps guide: the words Top 25 China apps, an Access Denied stamp and three boarding passes for Alipay, Amap and Hellobike",num="TOP 25",meta=("RANKED LIST","25 APPS"),t="Top 25 China apps for tourists, ranked like a boarding pass",p="From critical to optional: what each app does, how to set it up, and what you lose without it.",short="Top 25 China apps"),
 dict(slug="china-arrival-card-pc",sec="before",img="china-arrival-card-on-a-pc-step-by-step",alt="Cover of the China arrival card guide for PC, number 14 with a passport and an entry stamp",num="GUIDE 14",meta=("VIDEO + STEPS","3 MIN"),t="China arrival card online, step by step on a computer",p="Upload your passport, let it fill the form, save the QR. Every screen shown.",short="Arrival card on a PC"),
 dict(slug="china-arrival-card-alipay",sec="before",img="china-arrival-card-in-alipay-step-by-step",alt="Cover of the China arrival card guide for Alipay on a phone",num="GUIDE 14",meta=("VIDEO + STEPS","3 MIN"),t="China arrival card in Alipay on your phone",p="The same card through the Alipay mini program, for people who do it on the way.",short="Arrival card in Alipay"),
 dict(slug="taobao-for-foreigners",sec="shop",img="how-to-order-on-taobao-step-by-step-guide-cover",alt="Cover of the how to order on Taobao guide, a phone showing the Taobao app",num="SHOPPING",meta=("STEP BY STEP","12 STEPS"),t="How to order on Taobao as a foreigner, step by step",p="Settings, euro prices, searching in English, sending a parcel to your hotel and paying with Alipay.",short="How to order on Taobao"),
 dict(slug="alipay-metro-qr-code-china",sec="before",img="alipay-metro-qr-code-china-cover-16x9",alt="Cover of the Alipay metro QR code guide: Metro QR in China with the chips Alipay, Metro and Bus and a China flag sticker",num="METRO QR",meta=("STEP BY STEP","8 STEPS"),t="Alipay metro QR code in China: how to add it, step by step",p="Pick the city, claim the free card, enter your payment password, and switch city when the code is wrong.",short="Alipay metro QR code"),
 dict(slug="the-bund-shanghai-at-night",sec="place",img="the-bund-shanghai-after-dark-cover-4x5",alt="The Bund in Shanghai at night",row_k="The Bund",row_q="How do I get to the Bund at night, and when do the lights go off?",short="The Bund at night"),
 dict(slug="nanjing-road-shanghai",sec="place",img="nanjing-road-shanghai-neon-shop-fronts-cover-4x5",alt="Nanjing Road neon shop fronts",row_k="Nanjing Road",row_q="When is the neon on, and where does the walking street start?",short="Nanjing Road"),
 dict(slug="huangpu-river-night-cruise",sec="place",img="huangpu-river-night-cruise-from-the-water-cover-4x5",alt="Shanghai skyline from the Huangpu river at night",row_k="River cruise",row_q="Which pier, which ticket, and is the night cruise worth it?",short="Huangpu River night cruise"),
 dict(slug="shanghai-circus-world-era-show",sec="place",img="shanghai-circus-world-full-show-cover",alt="Shanghai Circus World stage with aerial silks",row_k="ERA show",row_q="Where do I book ERA circus tickets and how do I get there?",short="Shanghai Circus World ERA show"),
]
CARD_SLUGS={c["slug"] for c in CARDS}
QCARDS={
 "pc":("Arrival card · PC","How do I fill the China arrival card online?","3 min video + steps","china-arrival-card-pc"),
 "alipay":("Arrival card · Phone","Can I do the arrival card in Alipay on the way?","3 min video + steps","china-arrival-card-alipay"),
 "visa":("Visa-free","Do I need a visa, and for how many days?","Answers by passport, dated","china-visa-free-30-days"),
 "apps":("Paying · Maps · Trains","Which apps do I need, and which can I skip?","12 apps + hidden gems","china-travel-apps"),
 "taobao":("Shopping · Taobao","How do I order on Taobao when it is all in Chinese?","12 steps, hotel delivery","taobao-for-foreigners"),
 "metro":("Metro · Bus · Alipay","How do I get the metro QR code in Alipay?","8 steps, any city","alipay-metro-qr-code-china"),
 "before":("Before you fly","What do I need to set up before I land?","13-point checklist, 6 min","first-time-in-china"),
}
QS_HOME=["pc","alipay","visa","apps","metro"]
QS_CHINA=["visa","pc","alipay","apps","metro"]
QS_NEXT='<a class="q next" href="https://www.youtube.com/@scratchandroam?sub_confirmation=1" rel="noopener"><span class="k">Coming next</span><b>Trains, metro cards and the Chengdu to Xi\'an route</b><span class="go">Subscribe to catch the December guides</span></a>'
def qs_html(keys):
    return "\n".join(f'      <a class="q" href="/guides/{QCARDS[k][3]}/"><span class="k">{QCARDS[k][0]}</span><b>{QCARDS[k][1]}</b><span class="go">{QCARDS[k][2]}</span></a>' for k in keys)+"\n      "+QS_NEXT
def cards_in(sec): return [c for c in CARDS if c["sec"]==sec]
def home_tickets():
    first=["china-arrival-card-pc","china-arrival-card-alipay","first-time-in-china","china-dos-and-donts","china-travel-apps"]
    by={c["slug"]:c for c in CARDS}
    rest=[c for c in CARDS if c["sec"] in ("before","shop") and c["slug"] not in first]
    return [by[s] for s in first]+rest
def tickets_html(cs):
    return "\n".join(f'    <a class="tk" href="/guides/{c["slug"]}/"><img src="/img/{c["img"]}.jpg" alt="{c["alt"]}" loading="lazy"><span class="num">{c["num"]}</span><div class="cb"><div class="meta"><span>{c["meta"][0]}</span><span>{c["meta"][1]}</span></div><h3>{c["t"]}</h3><p>{c["p"]}</p><span class="go">Read the guide</span></div></a>' for c in cs)
def rows_html():
    return "\n".join(f'    <a class="row" href="/guides/{c["slug"]}/"><img src="/img/{c["img"]}.jpg" alt="{c["alt"]}" loading="lazy"><span><span class="k">{c["row_k"]}</span><b>{c["row_q"]}</b><span class="go">Guide</span></span></a>' for c in cards_in("place"))


SCRATCH_JS = """<script>
(function(){var win=document.getElementById('cwin'),c=document.getElementById('foil'),btn=document.getElementById('reveal'),hint=document.getElementById('chint');if(!win||!c)return;
var ctx=c.getContext('2d'),down=false,cleared=false,px=0;
function size(){var r=win.getBoundingClientRect();c.width=Math.max(1,Math.round(r.width));c.height=Math.max(1,Math.round(r.height));paint();}
function paint(){if(cleared)return;var g=ctx.createLinearGradient(0,0,c.width,c.height);g.addColorStop(0,'#d6dadf');g.addColorStop(.45,'#aeb3ba');g.addColorStop(1,'#e2e5e8');ctx.globalCompositeOperation='source-over';ctx.fillStyle=g;ctx.fillRect(0,0,c.width,c.height);ctx.fillStyle='rgba(255,255,255,.35)';for(var i=0;i<120;i++){ctx.fillRect(Math.random()*c.width,Math.random()*c.height,2,2);}
ctx.fillStyle='#1E1B1F';ctx.textAlign='center';ctx.font='700 '+Math.round(Math.min(c.width*.085,34))+'px "Special Elite", monospace';ctx.fillText('SCRATCH HERE',c.width/2,c.height*.5);ctx.font=Math.round(Math.min(c.width*.045,16))+'px "Special Elite", monospace';ctx.fillText('drag across the silver',c.width/2,c.height*.5+30);
ctx.beginPath();ctx.arc(c.width*.72,c.height*.72,Math.max(16,c.width*.06),0,Math.PI*2);ctx.fillStyle='#E3A42B';ctx.fill();ctx.lineWidth=2;ctx.strokeStyle='#8a6414';ctx.stroke();}
function clear(){if(cleared)return;cleared=true;c.style.transition='opacity .7s';c.style.opacity='0';c.style.pointerEvents='none';win.classList.add('open');if(hint)hint.textContent='there it is';if(btn){btn.textContent='Shanghai, revealed';btn.disabled=true;}}
function pos(e){var r=c.getBoundingClientRect();var t=e.touches?e.touches[0]:e;return{x:t.clientX-r.left,y:t.clientY-r.top};}
function scratch(e){if(!down||cleared)return;var p=pos(e);ctx.globalCompositeOperation='destination-out';ctx.beginPath();ctx.arc(p.x,p.y,Math.max(22,c.width*.07),0,Math.PI*2);ctx.fill();px++;if(px>45)clear();e.preventDefault();}
c.addEventListener('mousedown',function(e){down=true;scratch(e);});c.addEventListener('touchstart',function(e){down=true;scratch(e);},{passive:false});
c.addEventListener('mousemove',scratch);c.addEventListener('touchmove',scratch,{passive:false});
window.addEventListener('mouseup',function(){down=false;});window.addEventListener('touchend',function(){down=false;});window.addEventListener('resize',size);
if(btn)btn.addEventListener('click',clear);
if(document.fonts&&document.fonts.ready){document.fonts.ready.then(size);}size();})();
</script>"""

HOME = '''<main>
<section class="hero2"><div class="wrap">
  <div class="top">
    <div>
      <p class="eyebrow" style="color:#C0DACE">Travel guides and videos from Ireland</p>
      <h1 style="margin-top:10px">Going to China for the first time? <span>Start here.</span></h1>
      <p class="lede">Step by step guides for the things nobody explains before you fly: the arrival card, Alipay, visa-free rules, trains and metros. Filmed on the trip, written down so you can follow along at the airport.</p>
      <div class="cta"><a class="btn pri" href="/china/">Start with the China guides</a><a class="btn light" href="https://www.youtube.com/@scratchandroam?sub_confirmation=1" rel="noopener">Subscribe on YouTube</a></div>
    </div>
    <a class="vid" href="/guides/first-time-in-china/"><img src="/img/first-time-in-china-13-things-before-you-fly.jpg" alt="Cover of the First time in China video, 13 things to set up before you fly" fetchpriority="high"><span class="tag">Newest video</span><span class="play" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></span><span class="cap">First time in China: 13 things to set up before you fly<small>6 MIN · VIDEO + CHECKLIST</small></span></a>
  </div>
  <div class="pick">
    <p class="hand">Pick the thing you need to sort out:</p>
    <div class="qs">
@@QS_HOME@@
    </div>
  </div>
</div></section>
<div class="strip" aria-hidden="true"><span>Scratch to reveal · Roam to discover · Shanghai · Chengdu · Chongqing · Xi'an · Arrival card · Alipay · Visa-free · Scratch to reveal · Roam to discover · Shanghai · Chengdu · Chongqing · Xi'an · Arrival card · Alipay · Visa-free · </span></div>

<section class="sec" id="december"><div class="wrap cardsec">
  <div class="cardwrap">
    <div class="scard">
      <div class="head"><span class="mk">Scratch <em>&amp;</em> Roam</span><span class="no">Card no. 001 · Shanghai</span></div>
      <div class="win" id="cwin"><img src="/img/the-bund-shanghai-after-dark-cover-3x4.jpg" alt="The Bund in Shanghai at night" loading="lazy"><canvas id="foil" aria-label="Scratch the silver foil to reveal Shanghai"></canvas><span class="done">Shanghai, scratched off</span></div>
      <div class="foot"><span class="hand">Scratch to reveal. Roam to discover.</span><button class="reveal" id="reveal" type="button">Reveal it for me</button></div>
    </div>
    <p class="hint" id="chint">drag your finger across the silver bit</p>
  </div>
  <div>
    <p class="eyebrow">Why it's called Scratch &amp; Roam</p>
    <h2 style="margin-top:6px">A city gets scratched off once we've been</h2>
    <p style="color:var(--ink2);margin-top:12px;max-width:54ch">Every video opens with a scratch card: a place stays hidden until you scratch it, then it is all there. Shanghai is done. Chengdu, Chongqing and Xi'an stay under the foil until December.</p>
    <div class="cities">
      <div class="city"><b>Chengdu</b><span class="k">December</span><span class="hand">pandas, hotpot</span></div>
      <div class="city"><b>Chongqing</b><span class="k">December</span><span class="hand">metro through a building</span></div>
      <div class="city"><b>Xi'an</b><span class="k">December</span><span class="hand">Terracotta Army</span></div>
    </div>
    <div class="stops"><span class="stop home">CORK</span><span class="dash">- -</span><span class="stop">LONDON</span><span class="dash">- -</span><span class="stop">CHENGDU</span><span class="dash">- -</span><span class="stop">CHONGQING</span><span class="dash">- -</span><span class="stop">XI'AN</span></div>
  </div>
</div></section>

<section class="sec alt" id="guides"><div class="wrap">
  <div class="sechead"><div><p class="eyebrow">Start here</p><h2>China first-timer guides</h2><p>Each guide is the video plus the full written steps, so you can read it without sound. Facts checked against official pages, with the date we checked them.</p></div><span class="pill" style="background:#fff">Rules change, so every guide is dated</span></div>
  <div class="tickets">
@@TK_HOME@@
  </div>
</div></section>

<section class="sec" id="shanghai"><div class="wrap">
  <div class="sechead"><div><p class="eyebrow">Shanghai, answered</p><h2>What we filmed, turned into the practical answers</h2></div><a class="btn" href="https://www.youtube.com/@scratchandroam" rel="noopener">All videos</a></div>
  <div class="rows">
@@ROWS@@
    <a class="row" href="https://www.youtube.com/@scratchandroam" rel="noopener"><img src="/img/shanghai-at-night-film-strip-cover-4x5.jpg" alt="Shanghai at night as one roll of film" loading="lazy"><span><span class="k">Photo set</span><b>Shanghai at night as one roll of film</b><span class="go">Photos</span></span></a>
    <a class="row" href="https://www.youtube.com/@scratchandroam" rel="noopener"><img src="/img/shanghai-circus-world-photo-dump-cover.jpg" alt="Shanghai Circus photo dump cover" loading="lazy"><span><span class="k">Photo set</span><b>Circus photo dump</b><span class="go">Photos</span></span></a>
  </div>
</div></section>

<section class="sec alt"><div class="wrap about">
  <div class="polaroid"><div class="img"><img src="/img/natali-portrait-at-her-desk.jpg" alt="Natali in her studio, smiling at the camera" loading="lazy"></div><div class="cap">Natali, somewhere with a camera</div></div>
  <div><p class="eyebrow">About</p><h2>A maker from Ireland who travels with a camera and a lot of curiosity</h2><p>I make things for a living and film the trips in between. These pages are the parts I wish someone had written down for me.</p><p style="margin-top:16px"><a href="/about/">More about Scratch &amp; Roam</a></p></div>
</div></section>
</main>
''' + SCRATCH_JS

HOME=HOME.replace('@@QS_HOME@@',qs_html(QS_HOME)).replace('@@TK_HOME@@',tickets_html(home_tickets())).replace('@@ROWS@@',rows_html())
page("/","Scratch & Roam: China first-timer guides and travel videos",
     "Travel guides and videos from Natali, a maker from Ireland. First-timer China guides: arrival card, Alipay, visa-free rules. Scratch to reveal. Roam to discover.",
     HOME,
     [{"@context":"https://schema.org","@type":"WebSite","name":"Scratch & Roam with Natali","url":SITE,"inLanguage":"en","publisher":{"@type":"Person","name":"Natali","url":SITE+"/about/","sameAs":json.loads(SAMEAS)}},
      {"@context":"https://schema.org","@type":"Person","name":"Natali","url":SITE+"/about/","jobTitle":"Travel creator and maker","homeLocation":{"@type":"Place","name":"Ireland"},"sameAs":json.loads(SAMEAS)}],
     og_image=SITE+"/og/shanghai-circus-world-photo-dump.jpg", dark=True)

# China index
CHINA = '''<main>
<section class="chero"><div class="wrap">
<p class="eyebrow" style="color:#C0DACE"><a href="/" style="color:inherit">Home</a> · China</p>
<h1>China guides for first-timers: <span>entry, paying, trains.</span></h1>
<p class="lede">The practical part first, in the order you will need it: before you fly, at the border, then paying and getting around. Shanghai is filmed and written up; Chengdu, Chongqing and Xi'an land after December.</p>
<div class="pick">
  <p class="hand" style="color:#FFD27A;transform:none">Pick the thing you need to sort out:</p>
  <div class="qs">
@@QS_CHINA@@
  </div>
</div>
</div></section>

<section class="sec" id="before"><div class="wrap">
  <div class="sechead"><div><p class="eyebrow">Before you fly</p><h2>The setup guides</h2><p>Each one is the video plus the written steps, checked against the official page on the date shown.</p></div><span class="pill">Rules change, so every guide is dated</span></div>
  <div class="tickets">
@@TK_BEFORE@@
  </div>
</div></section>
<section class="sec alt" id="shopping"><div class="wrap">
  <div class="sechead"><div><p class="eyebrow">Once you are there</p><h2>Shopping, ordering and paying</h2><p>The things you do on your phone in China once the basics are set up, step by step, with the real screens.</p></div><span class="pill" style="background:#fff">Apps change, so every guide is dated</span></div>
  <div class="tickets">
@@TK_SHOP@@
  </div>
</div></section>


<section class="sec" id="shanghai"><div class="wrap">
  <div class="sechead"><div><p class="eyebrow">Shanghai, answered</p><h2>What we filmed, turned into the practical answers</h2><p>Four place guides from the trip, mostly at night: how to get there, when to go, what it costs.</p></div><a class="btn" href="https://www.youtube.com/@scratchandroam" rel="noopener">All videos</a></div>
  <div class="rows">
@@ROWS@@
  </div>
  <p class="intro" style="margin-top:26px;margin-bottom:0">The videos and photo sets behind these pages are on <a href="https://www.youtube.com/@scratchandroam" rel="noopener">YouTube</a>, <a href="https://www.instagram.com/scratchandroam/" rel="noopener">Instagram</a> and <a href="https://www.tiktok.com/@scratchandroam" rel="noopener">TikTok</a>. Shanghai Disneyland after dark is next.</p>
</div></section>

<section class="sec alt" id="december"><div class="wrap">
  <div class="sechead"><div><p class="eyebrow">Still under the foil</p><h2>December: Chengdu, Chongqing, Xi'an</h2><p>Pandas, hotpot, a metro that runs through a building, and the Terracotta Army. The guides from this trip land here first, then the videos.</p></div></div>
  <div class="cities" style="grid-template-columns:repeat(3,minmax(0,1fr));max-width:720px;margin-top:0">
    <div class="city"><b>Chengdu</b><span class="k">December</span><span class="hand">pandas, hotpot</span></div>
    <div class="city"><b>Chongqing</b><span class="k">December</span><span class="hand">metro through a building</span></div>
    <div class="city"><b>Xi'an</b><span class="k">December</span><span class="hand">Terracotta Army</span></div>
  </div>
  <div class="stops" style="margin-top:18px;font-size:12px"><span class="stop home">CORK</span><span class="dash">- -</span><span class="stop">LONDON</span><span class="dash">- -</span><span class="stop">CHENGDU</span><span class="dash">- -</span><span class="stop">CHONGQING</span><span class="dash">- -</span><span class="stop">XI'AN</span></div>
</div></section>
</main>'''
CHINA=CHINA.replace('@@QS_CHINA@@',qs_html(QS_CHINA)).replace('@@TK_BEFORE@@',tickets_html(cards_in('before'))).replace('@@TK_SHOP@@',tickets_html(cards_in('shop'))).replace('@@ROWS@@',rows_html())
page("/china/","China guides for first-timers: entry, payments, trains",
     "Practical China guides from Scratch & Roam: the arrival card, Alipay and WeChat setup, visa-free rules, trains and getting around, each with a video and written steps.",
     CHINA,[{"@context":"https://schema.org","@type":"CollectionPage","name":"China guides for first-timers","url":SITE+"/china/","mainEntity":{"@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"url":SITE+"/guides/"+c["slug"]+"/","name":c["short"]} for i,c in enumerate(CARDS)]}}],
     og_image=SITE+"/og/first-time-in-china-13-things.jpg", dark=True)

# About. Photos: swap any /img/ file for a personal one later (same aspect ratio keeps the layout).
ABOUT = '''<main>
<section class="ahero"><div class="wrap in">
  <div>
    <p class="eyebrow" style="color:#C0DACE"><a href="/" style="color:inherit">Home</a> · About</p>
    <h1>A maker from Ireland who travels <span>with a camera.</span></h1>
    <p class="lede">I am Natali. I make things for a living and film the trips in between: Shanghai so far, Chengdu, Chongqing and Xi'an in December, Japan after that. The guides on this site are the parts I wish someone had written down for me before my first trip.</p>
    <div class="cta"><a class="btn pri" href="/china/">Read the China guides</a><a class="btn light" href="https://www.youtube.com/@scratchandroam?sub_confirmation=1" rel="noopener">Subscribe on YouTube</a></div>
  </div>
  <div class="stack" aria-hidden="true">
    <div class="ph p1"><img src="/img/the-bund-shanghai-mix-of-architecture-styles-slide.jpg" alt=""><div class="cap">the Bund, late</div></div>
    <div class="ph p2"><img src="/img/shanghai-circus-world-act-2-hand-balance.jpg" alt=""><div class="cap">Shanghai Circus World</div></div>
    <div class="ph p3"><img src="/img/natali-portrait-at-her-desk.jpg" alt=""><div class="cap">me, in the studio</div></div>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="facts">
    <div class="fact"><b>Ireland</b><span>Home base, Co. Cork</span></div>
    <div class="fact"><b>1 city</b><span>Filmed and written up</span></div>
    <div class="fact"><b>3 cities</b><span>Under the foil for December</span></div>
    <div class="fact"><b>Dated</b><span>Every guide says when it was checked</span></div>
  </div>
</div></section>

<section class="sec alt"><div class="wrap story">
  <div class="pic"><img src="/img/nanjing-road-day-mood-night-mood-slide.jpg" alt="Nanjing Road in Shanghai at night" loading="lazy"><div class="sm"><img src="/img/huangpu-river-light-show-times-slide.jpg" alt="Pudong towers from the Huangpu river" loading="lazy"><img src="/img/the-bund-save-it-for-your-trip-slide.jpg" alt="Pudong skyline from the Bund" loading="lazy"></div></div>
  <div>
    <p class="eyebrow">The person</p>
    <h2>Making things by day, filming by night</h2>
    <p>I have a background in graphic design and I run a small studio in Ireland. Travel is the thing I do with the time in between, and the camera comes along because I want to remember the practical bits as much as the views: which exit, which pier, what it cost.</p>
    <p>My husband and family turn up in the videos sometimes, and so does the work on the days I am not travelling. Nothing here is sponsored. If a rule or a price is on a page, I checked it on the date written next to it.</p>
  </div>
</div></section>

<section class="sec"><div class="wrap story flip">
  <div class="pic"><div class="scard" style="max-width:380px;margin:0 auto"><div class="head"><span class="mk">Scratch <em>&amp;</em> Roam</span><span class="no">Card no. 001 · Shanghai</span></div><div class="win open" style="background:#1F1C28"><img src="/img/the-bund-shanghai-after-dark-cover-3x4.jpg" alt="The Bund in Shanghai at night" loading="lazy"><span class="done" style="opacity:1">Shanghai, scratched off</span></div><div class="foot"><span class="hand">Scratch to reveal. Roam to discover.</span></div></div></div>
  <div>
    <p class="eyebrow">The idea</p>
    <h2>Why a scratch card?</h2>
    <p>A place stays hidden until you scratch it, and then it is all there. Every video opens that way: the name of the place under silver foil, a coin, and then the real thing. On the site a city gets scratched off once we have actually been, so the foil over Chengdu, Chongqing and Xi'an comes off in December.</p>
    <p>It is also a reminder of how I like to travel: not knowing everything in advance, but having the practical parts sorted so the rest can be a surprise.</p>
  </div>
</div></section>

<section class="sec alt"><div class="wrap story">
  <div class="pic wide"><img src="/img/china-arrival-card-on-a-pc-step-by-step.jpg" alt="Cover of the China arrival card guide" loading="lazy"><div class="sm"><img src="/img/first-time-in-china-13-things-before-you-fly.jpg" alt="Cover of the first time in China checklist" loading="lazy"><img src="/img/china-arrival-card-in-alipay-step-by-step.jpg" alt="Cover of the Alipay arrival card guide" loading="lazy"></div></div>
  <div>
    <p class="eyebrow">The method</p>
    <h2>How a guide gets made</h2>
    <ol class="howl">
      <li><span class="n">1</span><div><b>Film the real screens and the real streets</b><span>The actual arrival card form, the actual metro exit. No stock footage.</span></div></li>
      <li><span class="n">2</span><div><b>Check every rule against the official page</b><span>Visa lists, fees, opening hours. Official sources are marked on each guide.</span></div></li>
      <li><span class="n">3</span><div><b>Write the steps so they work without sound</b><span>Each step heading is the thing you would type into a search box.</span></div></li>
      <li><span class="n">4</span><div><b>Date it, and recheck it</b><span>When a rule changes, the guide gets updated, not left to go stale.</span></div></li>
    </ol>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sechead"><div><p class="eyebrow">Follow along</p><h2>Same trips, different lengths</h2><p>Long videos on YouTube, short ones everywhere else, carousels on Instagram and Pinterest.</p></div></div>
  <div class="socs">
    <a class="soc" href="https://www.youtube.com/@scratchandroam" rel="me noopener"><b>YouTube</b><span>Full guides and long videos</span><span class="h">@scratchandroam</span></a>
    <a class="soc" href="https://www.instagram.com/scratchandroam/" rel="me noopener"><b>Instagram</b><span>Reels and facts carousels</span><span class="h">@scratchandroam</span></a>
    <a class="soc" href="https://www.tiktok.com/@scratchandroam" rel="me noopener"><b>TikTok</b><span>The short versions</span><span class="h">@scratchandroam</span></a>
    <a class="soc" href="https://www.pinterest.com/scratchandroam/" rel="me noopener"><b>Pinterest</b><span>Carousels and covers to save</span><span class="h">@scratchandroam</span></a>
    <a class="soc" href="https://www.facebook.com/scratchandroam" rel="me noopener"><b>Facebook</b><span>Everything, a day later</span><span class="h">@scratchandroam</span></a>
  </div>
</div></section>

<section class="sec" style="padding-top:0"><div class="wrap">
  <div class="hello"><div><p class="eyebrow" style="color:#CFC7D4">Say hello</p><h2>Questions about a trip, or a place you want covered?</h2><p>Email is best. I read everything, and the guides often start with a question someone sent.</p></div><div><p class="big">scratchandroam@gmail.com</p><p style="margin-top:8px">Handle everywhere: @scratchandroam</p></div></div>
</div></section>
</main>'''
page("/about/","About Scratch & Roam with Natali","Natali is a maker from Ireland who films her trips and writes first-timer travel guides. Scratch to reveal. Roam to discover.",ABOUT,
     [{"@context":"https://schema.org","@type":"AboutPage","name":"About Scratch & Roam with Natali","url":SITE+"/about/","mainEntity":{"@type":"Person","name":"Natali","sameAs":json.loads(SAMEAS)}}],
     og_image=SITE+"/og/shanghai-circus-world-photo-dump.jpg", dark=True)

NIA="https://s.nia.gov.cn/ArrivalCardFillingPC/"
COMMON_FAQ=[
 ("Do I have to show the QR code at the border?","In our own experience nobody asked us to show it, but it is better to have it. Save it as a PDF and send it to your email so it is on your phone either way."),
 ("Does the arrival card cost anything?","No. The official card on the National Immigration Administration site is free. If a site asks you to pay, it is not the official one."),
 ("Can I do it on my phone instead of a computer?","Yes. The same card is inside Alipay as a mini program. There is a separate guide and video for that version."),
 ("What do I need to have ready?","Your passport, your flight number, where you will stay in China and the reason for the trip. The passport page fills most of the form for you."),
]
PC_STEPS=[
 ("What is the China arrival card and is it free?","China's arrival card is filled in online before you land. The official page is on the National Immigration Administration site and it is free."),
 ("What do I need before I start?","Have your passport, your flight number, the address of where you are staying and your reason for travel next to you."),
 ("Where is the official arrival card website?",f'Go to the official page at <a href="{NIA}" rel="noopener">s.nia.gov.cn</a>. Use a computer with a camera or have a clear photo of your passport page ready to upload.'),
 ("Upload your passport page and check what it filled in","Upload the photo page of your passport. The site reads it and fills in your name, passport number, nationality and dates. Check every field against your passport; type only what it did not recognise."),
 ("Fill in the basic and personal information","Confirm the basic details, then add the personal ones: contact details and anything the passport page could not supply."),
 ("Fill in the travel information: flight, address, reason","Flight number, where you will stay, how long, and why you are travelling. Use the address exactly as your booking shows it."),
 ("Sign and confirm the card","Sign on the screen and confirm. Read the summary once more before you submit."),
 ("Save the QR code as a PDF and email","The site offers a QR code, a PDF download and an email copy. Take all of them. Keep the PDF on your phone in case there is no signal at the airport."),
]
guide("china-arrival-card-pc","China arrival card on a PC: step by step guide","China arrival card online on a PC, step by step",
      "Filling in the China arrival card online on a computer? Here is the whole form step by step, with the real form enlarged. Upload your passport and most of the details fill in for you.",
      "China arrival card online","33pgztdZT8Q",
      "<p>The arrival card is the one form every visitor fills in before landing in China. On a computer it takes a few minutes: the passport page does most of the typing, and at the end you save a QR code. This is the computer version; if you prefer your phone, use the <a href='/guides/china-arrival-card-alipay/'>Alipay guide</a>.</p>",
      PC_STEPS,COMMON_FAQ,
      [("National Immigration Administration: arrival card filling page",NIA,True)],
      SITE+"/og/china-arrival-card-on-a-pc.jpg",
      chapters=[("0:00","Intro: the arrival card on a PC"),("0:15","What the arrival card is"),("0:44","Get ready"),("1:04","Open the website"),("1:20","Passport page: the form fills itself"),("1:43","Basic information"),("2:04","Personal information"),("2:28","Travel information"),("2:51","Sign and confirm"),("3:01","Save your QR code"),("3:29","Your move")],
      related=[("/guides/china-arrival-card-alipay/","china-arrival-card-in-alipay-step-by-step","GUIDE 14","China arrival card in Alipay on your phone"),("/guides/first-time-in-china/","first-time-in-china-13-things-before-you-fly","GUIDE 13","First time in China: 13 things to set up before you fly")],
      minutes="PT3M41S",upload="2026-10-15")

AP_STEPS=[
 ("What is the China arrival card and is it free?","China's arrival card is filled in online before you land. The official version also lives inside Alipay as a mini program, and it is free."),
 ("What do I need before I start?","Have your passport, your flight number, the address of where you are staying and your reason for travel next to you. Install Alipay first if you have not yet."),
 ("Where is the arrival card inside Alipay?","Open Alipay and search for the arrival card mini program. Open it and agree to the terms."),
 ("Agree, then photograph your passport page","Take a photo of the photo page of your passport. The app reads it and fills in your name, passport number, nationality and dates. Check each one."),
 ("Check the basic information","Confirm the basic details the passport page supplied."),
 ("Add the personal information","Add your contact details and anything the passport could not supply."),
 ("Fill in the travel information: flight, address, reason","Flight number, where you will stay, how long, and why you are travelling. Use the address exactly as your booking shows it."),
 ("Sign and confirm the card","Sign on the screen and confirm. Read the summary once more before you submit."),
 ("Save the QR code as a PDF and email","Save the QR code, download the PDF and send it to your email, so it is on your phone even without signal."),
]
guide("china-arrival-card-alipay","China arrival card in Alipay: step by step guide","China arrival card in Alipay on your phone, step by step",
      "Filling in the China arrival card online with Alipay on your phone? Here is the whole form step by step. Upload your passport and most of the details fill in for you.",
      "China arrival card Alipay","YDdwz1ChMFE",
      "<p>If you already have Alipay set up for paying in China, the arrival card is inside it too. The passport page fills in most of the form, you check it, and you save the QR code at the end. Prefer a computer? Use the <a href='/guides/china-arrival-card-pc/'>PC guide</a>.</p>",
      AP_STEPS,COMMON_FAQ,
      [("National Immigration Administration: arrival card filling page",NIA,True)],
      SITE+"/og/china-arrival-card-in-alipay.jpg",
      chapters=[("0:00","Intro: the arrival card in Alipay"),("0:13","What the arrival card is"),("0:42","Get ready"),("1:03","Find the mini program in Alipay"),("1:21","Agree and passport page"),("1:42","Basic information"),("1:59","Personal information"),("2:15","Travel information"),("2:32","Sign and confirm"),("2:42","Save your QR code"),("3:10","Your move")],
      related=[("/guides/china-arrival-card-pc/","china-arrival-card-on-a-pc-step-by-step","GUIDE 14","China arrival card online on a computer"),("/guides/first-time-in-china/","first-time-in-china-13-things-before-you-fly","GUIDE 13","First time in China: 13 things to set up before you fly")],
      minutes="PT3M23S",upload="2026-10-15")

FT_STEPS=[
 ("Check the entry rules for your passport","On 15 October 2026, China listed visa-free entry for passport holders from 50 countries, most of it running to 31 December 2026, and the usual advice is a passport valid for 6 more months. Check your own country on the official list before you book, because the dates move."),
 ("Fill in the arrival card","It is free and online. Do it on a computer or inside Alipay; both guides are on this site."),
 ("Get the apps","Alipay and WeChat, before you fly. Both have an English setup for visitors."),
 ("Link your card","Add your bank card to Alipay and WeChat Pay at home, while you still have your normal phone number and signal."),
 ("Try a mini program","Trains, taxis and the arrival card all live inside Alipay as mini programs. Open one at home so the first time is not at a station."),
 ("Know the ¥200 line","Foreign cards in Alipay and WeChat Pay carry a 3 percent fee on single payments above ¥200. Below that there is no fee, so small payments are cheap."),
 ("Carry some cash and a backup card","Not much is needed, but a little cash and a second card cover the one shop that cannot take your phone."),
 ("Pick your flight","From Ireland the options are a non-stop from Dublin or a one-stop through a hub. Check your own airport; we have flown via London and via Helsinki, and this December via London."),
 ("Book smart","Book accommodation that confirms a real address, because the arrival card and any police registration both ask for it."),
 ("Book trains in time","High-speed train tickets go on sale about 15 days before travel. Book through the official 12306 app or a reseller and keep your passport number exactly as in the booking."),
 ("Station day","Stations are big and often share a name with a city. Check the exact station on your ticket, arrive early, and have your passport out for the gate."),
 ("Get maps that work","Amap and Apple Maps work well in China; Google Maps does not. Save offline notes with the Chinese names of your hotel and stations."),
 ("Pack light","Trains and metros mean stairs and gates. One bag you can lift makes every station day easier."),
]
guide("first-time-in-china","First time in China: 13 things to set up before you fly","First time in China: 13 things to set up before you fly",
      "Going to China for the first time? The 13 things we set up before flying: entry rules, the arrival card, Alipay and WeChat, cards, cash, flights, trains, maps and packing.",
      "first time in China","TuP9NS00Ugg",
      "<p>This is the checklist we wish we had before the first trip: not sights, just the setup. Everything on it was checked on 15 October 2026 against the sources at the bottom, and the video walks through the same 13 things.</p>",
      FT_STEPS,
      [("Do I need a visa for China?","It depends on your passport. In October 2026 China listed 50 countries with visa-free entry for short stays, most of it dated to 31 December 2026. Check the official list for your own country before booking."),
       ("Which app do I need, Alipay or WeChat?","Both work for paying. Set both up at home, link a card to each, and you will not be stuck when one of them does not like your card."),
       ("Does Google Maps work in China?","No. Use Amap or Apple Maps, and keep the Chinese names of your hotel and stations saved offline."),
       ("When should I book high-speed trains?","Tickets go on sale about 15 days before the travel date. Book as soon as they open for busy routes.")],
      [("Shanghai municipal government (English): visa-free entry policy","https://english.shanghai.gov.cn/en-Individuals-ImmigrationandVisas-Visa-freepolicies/20260709/469e8c5656534926a04b31a1084351f0.html",True),
       ("National Immigration Administration: arrival card filling page",NIA,True),
       ("China Railway 12306","https://www.12306.cn/en/",True)],
      SITE+"/og/first-time-in-china-13-things.jpg",minutes="PT5M45S",upload="2026-10-16",
      chapters=[("1","Entry rules"),("2","Arrival card"),("3","Get the apps"),("4","Pay setup"),("5","Mini-programs"),("6","The ¥200 fee"),("7","Cash"),("8","Flights"),("9","Booking"),("10","Trains"),("11","Station day"),("12","Maps"),("13","Pack light")],
      related=[("/guides/china-arrival-card-pc/","china-arrival-card-on-a-pc-step-by-step","GUIDE 14","China arrival card online on a computer"),("/guides/china-arrival-card-alipay/","china-arrival-card-in-alipay-step-by-step","GUIDE 14","China arrival card in Alipay on your phone")])

# ---------- China travel apps (every fact checked 16 Oct 2026 against the sources on the page) ----------
H='<span class="tag h">Set up at home</span>'
A='<span class="tag a">On arrival is fine</span>'
G='<span class="tag g">Hidden gem</span>'
APP_STEPS=[
 ("Alipay: the one app you cannot skip",
  H+"<br>Download the international Alipay (on the App Store it is called <b>Alipay - Simplify Your Life</b>), verify your passport first under Me, Settings, Account and Security, Identity Information, then link a Visa or Mastercard. Do it two or three days before you fly: the passport check is usually minutes, but guides report waits of up to 72 hours, and the codes go by text to your home number. Payments up to ¥200 are free; a payment over ¥200 carries a 3% fee, so split big bills or pay those by card where you can. The real reason it comes first: half the apps other lists tell you to download live inside it as mini-programs, so you can skip them (see the hidden gems below)."),
 ("WeChat and WeChat Pay: the backup with a 90-day fee break",
  H+G+"<br>Small shops, scan-to-order menus and a lot of ticket systems run on WeChat, so have it ready even if Alipay is your main wallet. Add your card under Me, Pay and Services, Wallet, Bank Cards; any number that can get a text works, no Chinese number needed. New accounts are sometimes asked for a friend verification, where an existing user scans a code for you, which is one more reason to start at home. The gem: Tencent announced on 27 May 2026 that first-time users who link an international card pay no transaction fee for 90 days from their first payment, on up to ¥1,000 a day. After that, WeChat's own help page says payments over ¥200 carry 3%."),
 ("AMap Global: maps in English, with a taxi app hiding inside",
  H+G+"<br>AMap (Gaode) is the map most people in China use, and the AMap Global app has had English since January 2025 and 14 more languages since July 2025. The part most lists miss: it has its own ride-hailing that books several taxi companies at once and shows pickup points and fare estimates in English. Its August 2026 announcement says you can sign in with a phone number from 65 countries and regions and pay through Alipay or WeChat Pay, so link Alipay at home. Search tip: paste the Chinese name of your hotel from the booking. On an iPhone, Apple Maps also works in China without a VPN and is a fine second map."),
 ("MetroMan China: the offline metro map nobody mentions",
  H+G+"<br>A small English app with offline metro maps for 53 Chinese cities, including Chengdu, Chongqing and Xi'an; free, with an optional paid upgrade, and its App Store listing was updated on 30 September 2026. It is the one I would open on a platform with no signal. You do not even need a ticket app for the metro in some cities: in Beijing, Shanghai and Chengdu you can tap a foreign Visa or Mastercard straight on the gate, and Alipay has a Transport code for each city you activate once."),
 ("Railway 12306: the official train app, and its two quiet features",
  H+G+"<br>The official China Railway app (on the App Store as <b>铁路12306</b>, with English inside). Register with your passport; you cannot buy until it is verified, and verification can take a while, so do it at home. Tickets normally open 15 days ahead, counting the travel day. Two features most visitors never find: the <b>waitlist</b> for sold-out trains, where you prepay and the system keeps trying until shortly before departure and refunds you if it fails, and a <b>60-day reservation</b> pilot running since 20 July 2026 on more than 200 Beijing to Shanghai trains, where you order 17 to 60 days ahead, the system fills orders 16 to 20 days before departure, and you pay by 23:00 that day. Also new: one free refund a day if you cancel within 30 minutes of buying and at least 4 hours before departure. Careful with lookalikes: <b>China Train Ticket for 12306官网</b> is a private app, not the official one."),
 ("Trip.com: the English backup for trains and hotels",
  H+"<br>The easiest place to book in English, with 24/7 English support and guest checkout for trains that does not need a verified passport. Its hotel search can filter for hotels that accept foreign guests, which matters because some hotels in China still cannot take foreigners. Trip.com's own pages disagree with each other about train booking fees in 2026, so compare the final price with 12306 before you pay."),
 ("NIA 12367: the government app that does your arrival card",
  H+G+"<br>The National Immigration Administration's app. Since 20 November 2025 you can fill in the China arrival card online before you land, in this app, in its Alipay or WeChat mini-program, or on the official website; Shanghai warns about lookalike scam sites, so use only official channels. It also handles police registration for stays outside hotels: hotels register you themselves, but if you stay in a flat or with friends you must register within 24 hours, and an online pilot started on 20 March 2026 in seven provinces including Sichuan and Chongqing. The Irish Department of Foreign Affairs notes that online registration needs a Chinese mobile number. Step by step: <a href='/guides/china-arrival-card-pc/'>arrival card on a PC</a> or <a href='/guides/china-arrival-card-alipay/'>in Alipay</a>."),
 ("A travel eSIM: how Google and WhatsApp keep working",
  H+"<br>eSIM sellers such as Airalo, Holafly, Nomad and Trip.com say their China plans route your data outside China, so Google, WhatsApp and Instagram work without a VPN; read the plan description to be sure. Install the eSIM at home on Wi-Fi: Airalo needs a connection to install, and Nomad says new plans cannot be bought once you are in mainland China. Two catches: an eSIM is data only, so keep your home SIM on for text codes from your bank, Alipay and WeChat, and hotel Wi-Fi does not route abroad, so blocked apps stop working the moment you switch to it."),
 ("A paid VPN, only as the backup for hotel Wi-Fi",
  H+"<br>You cannot get one after you land: Apple removed VPN apps from the China App Store in 2017 and provider websites are blocked. The 2026 twist most lists missed: LetsVPN, long the one people recommended, announced in April 2026 that it was ending its service for mainland China after weeks of blocking. Nobody publishes independent, dated tests from inside China, so pick a paid VPN with an obfuscation or stealth mode, install and test it at home, and treat it as a backup, not a plan. Using one sits in a legal grey area in China."),
 ("Apple Translate or Microsoft Translator, plus Pleco",
  H+G+"<br>Google Translate is blocked online in China; its offline Chinese pack works only if you download it before you go. Apple Translate is free, works fully offline once Chinese is downloaded and translates through the camera; on Android, Microsoft Translator works without a VPN and has offline packs too. The gem is <b>Pleco</b>, a free offline Chinese dictionary: when the translation of a menu line makes no sense, look up the characters one by one. Its camera recognition is a paid add-on (€9.99 on the Irish App Store). Alipay also has Scan, Translate built in for menus and signs."),
 ("RedNote (Xiaohongshu): where locals actually find places",
  H+G+"<br>Ask anyone in China where to eat and they open RedNote, not a review site. It is the best search engine for what is good right now: new cafés, viewpoints, which queue is worth it. It added AI translation in January 2025 and you can sign up with a foreign number, but the interface is still mostly Chinese, so search with the Chinese name of a place copied from AMap."),
 ("Dianping: reviews, plus a digital queue number",
  A+G+"<br>China's main restaurant review app. The App Store lists English, though in practice the English is partial and reviews are not translated. The feature worth installing it for is <b>排队 (queue)</b>: take a number for a busy restaurant from your phone and watch how many tables are ahead of you, instead of standing at the door for an hour."),
]
APP_EXTRA='''
<h2>Hidden gems inside Alipay (nothing to download)</h2>
<p>These are the apps other lists tell you to install. Open them from Alipay's search bar or Transport section instead, and they use the card you already linked.</p>
<ul class="gemlist">
<li><b>Taxi.</b> Transport, then Taxi, opens DiDi inside Alipay, with no separate account and fewer payment problems. The standalone DiDi app also has English and in-app translation if you prefer it.</li>
<li><b>Metro code.</b> Transport, then your city: activate each city's metro QR code once and scan through the gates.</li>
<li><b>Shared bikes.</b> Scan the QR code on a Hello Bike or Meituan bike with Alipay's scanner and the right mini-program opens. Meituan's own app needs a Chinese number; this way does not.</li>
<li><b>Power banks.</b> Scan a rental kiosk (Energy Monster and others). Expect a ¥99 hold on your card that is released when you return it.</li>
<li><b>Food delivery.</b> Ele.me was renamed Taobao Instant Commerce in December 2025 and runs as a mini-program in Alipay, which is the easiest delivery option for visitors.</li>
<li><b>Coffee.</b> Luckin's own app wants a Chinese number; the Luckin mini-program in Alipay does not.</li>
<li><b>Luggage storage.</b> Search 行李寄存 (luggage storage) to find left-luggage points near stations and sights.</li>
<li><b>China Bound.</b> China Daily's English travel platform, launched 1 January 2026, with translation, tickets, hotels and an AI itinerary helper. I have not tested it yet.</li>
<li><b>Shanghai Easy Go.</b> Shanghai's visitor service inside Alipay since July 2025: about 30 mini-programs for food, transport, tickets, luggage and tax refunds, with translation in 14 languages.</li>
<li><b>Travel Wallet.</b> Launched in April 2026 with Beijing's GO BEIJING service: you fund it by an international transfer and spend anywhere in mainland China with no card fee. It is open to people from 40 countries and regions, so check yours is on the list before relying on it.</li>
</ul>
<h2>Which apps must be set up at home?</h2>
<table class="tbl"><thead><tr><th>App</th><th>When</th><th>Why</th></tr></thead><tbody>
<tr><td>Alipay, WeChat</td><td class="home">At home</td><td>Passport checks, text codes to your home number, your bank's first-payment check</td></tr>
<tr><td>Railway 12306, Trip.com</td><td class="home">At home</td><td>Passport verification before you can buy trains</td></tr>
<tr><td>AMap Global, MetroMan</td><td class="home">At home</td><td>Google Play does not work in China; offline maps need downloading</td></tr>
<tr><td>Travel eSIM</td><td class="home">At home</td><td>Needs Wi-Fi to install; some plans cannot be bought in China</td></tr>
<tr><td>VPN</td><td class="home">At home</td><td>Not in China's App Store, provider sites blocked</td></tr>
<tr><td>NIA 12367</td><td class="home">At home</td><td>Arrival card before you land</td></tr>
<tr><td>Translation packs, Pleco, RedNote</td><td class="home">At home</td><td>Offline packs and sign-up are easier on open internet</td></tr>
<tr><td>Dianping, bikes, power banks, taxis</td><td class="arr">On arrival</td><td>Run through Alipay once it works</td></tr>
</tbody></table>
<h2>China travel apps you can skip</h2>
<ul class="skiplist">
<li><b>Google Maps.</b> Blocked without a VPN, and even with one the China map is offset, so your blue dot can sit hundreds of metres from where you are.</li>
<li><b>Uber.</b> It sold its China business to DiDi in 2016.</li>
<li><b>Airbnb for mainland China.</b> It removed its mainland listings in July 2022.</li>
<li><b>Baidu Maps.</b> Works, but AMap Global is the better English choice.</li>
<li><b>The standalone Meituan and Luckin apps.</b> Both expect a Chinese number; use their Alipay mini-programs.</li>
<li><b>Alipay Tour Card.</b> A prepaid card with a 5% top-up fee, and 2026 reports say it closed to new users. Do not plan around it.</li>
<li><b>Waygo.</b> Still in the App Store, but not updated since 2017.</li>
<li><b>LetsVPN and free VPNs.</b> LetsVPN left mainland China in April 2026; free VPNs are reported to fail.</li>
<li><b>Lookalike 12306 apps.</b> Only 铁路12306 from China Railway is official.</li>
</ul>'''
guide("china-travel-apps","China travel apps: 12 to set up before you go (2026)","Apps to download before you go to China: the full list",
      "The China travel apps to set up before you fly: paying, maps, taxis and trains, what must be done at home, the hidden gems inside Alipay, and what to skip.",
      "china travel apps","TuP9NS00Ugg",
      "<p>Most lists of China travel apps stop at Alipay, WeChat and a VPN. This one is the full setup: the 12 apps worth having on your phone before you land, which ones have to be set up at home, the hidden gems that sit inside apps you already have, and the ones you can skip.</p><p>Every fact here was checked on 16 October 2026 against the sources at the bottom, and a lot changed this year: a new 90-day fee break on WeChat Pay, a 60-day train reservation pilot, English taxis inside AMap, and the VPN everyone used to recommend pulling out of China.</p>",
      APP_STEPS,
      [("Which apps do I need for paying, maps, taxis and trains in China?","Alipay and WeChat for paying, AMap Global for maps (Apple Maps also works on an iPhone), the DiDi taxi inside Alipay or AMap's own ride-hailing for taxis, and Railway 12306 or Trip.com for trains. With those set up you can get through almost any day."),
       ("Which China travel apps must be set up at home?","Anything that needs a passport check, a text code or a download from a store that is blocked in China: Alipay, WeChat, 12306, Trip.com, AMap, your eSIM and any VPN. Passport checks can take up to a few days and Google Play and VPN sites do not work once you land."),
       ("Which apps can I skip?","Google Maps, Uber, Airbnb for mainland stays, the standalone Meituan and Luckin apps, Alipay's Tour Card, Waygo, LetsVPN and any 12306 lookalike."),
       ("Do I need a separate taxi app in China?","No. DiDi opens inside Alipay under Transport, and AMap Global books rides in English. Download the DiDi app only if you prefer a standalone app."),
       ("Do I need a VPN if I have a travel eSIM?","Usually not on mobile data, because travel eSIM plans for China route your data abroad. A VPN still helps on hotel Wi-Fi, which does not, and it has to be installed before you fly.")],
      [("WeChat Help Center: international cards on Weixin Pay","https://cs.help.wechat.com/hc/en-us/articles/11975770896271-How-to-Set-Up-International-Cards-for-Weixin-Pay",True),
       ("Tencent: Weixin Pay 90-day fee waiver, 27 May 2026","https://www.tencent.com/en-us/articles/2202338.html",True),
       ("Alipay on the App Store","https://apps.apple.com/app/alipay/id333206289",True),
       ("Trip.com: how to add a card to Alipay, June 2026","https://www.trip.com/guide/payments/how-to-add-card-to-alipay.html",False),
       ("China for Travelers: Alipay for foreigners, August 2026","https://chinafortravelers.com/guides/alipay-for-foreigners/",False),
       ("Beijing government: Travel Wallet and GO BEIJING, April 2026","https://english.beijing.gov.cn/specials/paymentservices/news/202604/t20260430_4624215.html",True),
       ("Shanghai government: AMap in 15 languages, July 2025","https://english.shanghai.gov.cn/en-Latest-WhatsNew/20250711/8f2fcf3c6b624a56a6b2c0d8152ea2f2.html",True),
       ("AMap: ride-hailing for international visitors, August 2026","https://en.prnasia.com/releases/global/amap-brings-ride-hailing-to-international-visitors-in-china-543611.shtml",True),
       ("MetroMan China on the App Store","https://apps.apple.com/app/id466351433",True),
       ("China for Travelers: paying with a foreign card at metro gates, August 2026","https://chinafortravelers.com/guides/china-metro-foreign-card/",False),
       ("DiDi China on the App Store","https://apps.apple.com/app/id554499054",True),
       ("Ministry of Culture and Tourism: getting around, March 2026","https://www.travelchina.org.cn/en/article/PVxGvzt38tts",True),
       ("Ministry of Culture and Tourism: train tickets with 12306, April 2026","https://www.travelchina.org.cn/en/article/LvQmnlhnsKzF",True),
       ("Beijing government: 12306 ticket reservation pilot, July 2026","https://english.beijing.gov.cn/travellinginbeijing/transportation/railway/202607/t20260720_4772390.html",True),
       ("China Railway 12306: FAQ","https://www.12306.cn/en/faq.html",True),
       ("Trip.com: sold-out trains and the waitlist, August 2026","https://my.trip.com/guide/transport/china-train-tickets-sold-out.html",False),
       ("Beijing government: online arrival card, November 2025","https://english.beijing.gov.cn/latest/news/202511/t20251105_4259688.html",True),
       ("National Immigration Administration: registration for stays outside hotels, March 2026","https://en.nia.gov.cn/n147418/n147463/c196956/content.html",True),
       ("Department of Foreign Affairs (Ireland): China travel advice","https://www.ireland.ie/en/dfa/overseas-travel/advice/china/",True),
       ("Airalo: is a VPN needed in China?","https://www.airalo.com/help/using-managing-esims/ZSEEHBT5HW6F/stay-connected-in-china-your-guide-to-unfiltered-internet-access-is-a-vpn-required/ZDZBNIKI4TFP",False),
       ("Nomad: do eSIMs work in China?","https://www.nomadesim.com/blog/do-esims-work-in-china",False),
       ("China Digital Times: LetsVPN ends mainland service, April 2026","https://chinadigitaltimes.net/chinese/726869.html",False),
       ("Comparitech: are VPNs legal in China? June 2026","https://www.comparitech.com/blog/vpn-privacy/are-vpns-legal-in-china",False),
       ("mychina.guide: does Google Translate work in China? September 2026","https://mychina.guide/blog/does-google-translate-work-in-china",False),
       ("Pleco on the Irish App Store","https://apps.apple.com/ie/app/pleco-chinese-dictionary/id341922306",True),
       ("TechNode: RedNote adds translation, January 2025","https://technode.com/2025/01/20/xiaohongshu-rolls-out-ai-powered-translation-feature-likely-using-gpt-4/",False),
       ("WanderInChina: Dianping and Meituan, February 2026","https://wanderinchina.com/survival-guide/useful-mobile-apps/dazhong-dianping-meituan/",False),
       ("Caixin: Alibaba retires the Ele.me brand, December 2025","https://www.caixinglobal.com/2025-12-05/alibaba-retires-eleme-brand-in-shift-to-instant-retail-102390218.html",False),
       ("China Daily: China Bound launches, January 2026","https://studychina.chinaservicesinfo.com/s/202601/01/WS6955ce18498e36855033978d/china-daily-launches-china-bound-an-english-language-smart-tourism-service-platform-for-international-traveler.html",True),
       ("Shanghai government: Easy Go on Alipay, July 2025","https://english.shanghai.gov.cn/en-ExpatServices-Videos-WhatsNew/20250702/104ac119548743968fe343bb14d14bdd.html",True),
       ("Trip.com: shared bikes in China, August 2026","https://au.trip.com/guide/transport/shared-bikes-in-china.html",False),
       ("China Survival Kit: renting a power bank, October 2026","https://chinasurvivalkit.com/blog/rent-power-bank-china-guide",False),
       ("Skift: Airbnb and China, March 2025","https://skift.com/2025/03/20/airbnb-stopped-listing-in-china-but-it-still-wants-chinese-travelers/",False),
       ("Waygo on the Irish App Store","https://apps.apple.com/ie/app/waygo-chinese-japanese-and-korean-translator/id496038103",True)],
      SITE+"/og/china-travel-apps.jpg",checked="2026-10-16",start=90,vschema=False,
      video_note='<p class="vnote">The video starts at 1:30, where my first-timer guide gets to the apps: Alipay and WeChat set up at home on my own phone, linking a card, mini-programs, trains, taxis and Amap. <a href="/guides/first-time-in-china/">Full 13-step guide</a>.</p>',
      steps_title="The 12 apps, in the order to set them up",
      chapters=[("1:30","Download Alipay and WeChat"),("1:50","Link your card"),("2:10","Alipay Travel Wallet"),("2:32","WeChat Pay"),("2:45","Mini-programs"),("4:42","Trains, taxis and Trip.com in Alipay"),("5:09","Maps: Amap and offline notes")],
      related=[("/guides/alipay-metro-qr-code-china/","alipay-metro-qr-code-china-cover-16x9","METRO QR","Alipay metro QR code in China: how to add it"),("/guides/first-time-in-china/","first-time-in-china-13-things-before-you-fly","GUIDE 13","First time in China: 13 things to set up before you fly"),("/guides/china-arrival-card-alipay/","china-arrival-card-in-alipay-step-by-step","GUIDE 14","China arrival card in Alipay on your phone"),("/guides/taobao-for-foreigners/","how-to-order-on-taobao-step-by-step-guide-cover","SHOPPING","How to order on Taobao as a foreigner, step by step"),("/guides/top-25-china-apps/","top-25-china-apps-boarding-pass-cover","TOP 25","Top 25 China apps for tourists, ranked like a boarding pass")],
      extra=APP_EXTRA)

# ---------- Shanghai place guides (facts from the sources listed on each page, checked 15 Oct 2026) ----------
SH=dict(city="Shanghai")
CHECK='<p>Prices and times here are from the sources at the bottom, checked on 15 October 2026. They move. Treat the numbers as a guide and check the official page or Trip.com on the day.</p>'

guide("the-bund-shanghai-at-night","The Bund Shanghai at night: how to get there and when to go","The Bund in Shanghai at night: how to get there, where to start, when the lights go off",
      "How to get to the Bund by metro (East Nanjing Road, exit 2 or 7), the best time for the lights, when they switch off, and a simple route along the river. Free, no ticket.",
      "the Bund Shanghai at night",None,
      "<p>The Bund is the river promenade with the old European banks on one side and the Pudong towers across the water. It is free, it is open all the time, and the only thing you can get wrong is the timing. We went at night and the gold-lit buildings are the whole point. Here is how to do it without wandering.</p>"+CHECK,
      [("Take the metro to East Nanjing Road and use exit 2 or 7","East Nanjing Road station is on Lines 2 and 10. From exit 2 you are on the pedestrian street; walk east, towards the river, about 10 to 15 minutes. Taxis cannot drop you on the promenade itself."),
       ("Arrive about an hour before sunset","You get the buildings in daylight, then sunset, then the lights. Coming from the north, Tiantong Road station on Lines 10 and 12 also works."),
       ("Start at the Peace Hotel and walk south","The green-roofed Peace Hotel is where Nanjing Road meets the Bund, so it is the natural start. Walk south along the raised promenade with the old banks on your right and Pudong on your left."),
       ("Know when the lights go off","The architectural lights on both banks usually switch off at 22:00. In winter they come on from about 18:00, in summer not until about 19:30. Do not arrive at 22:30 expecting the show."),
       ("Skip the sightseeing tunnel unless you have kids","The Bund Sightseeing Tunnel under the river is a short light-effects ride with no river view. Fun for children, not for the skyline."),
       ("Give it 90 minutes, or half a day with a cruise","The promenade and the main buildings take about 90 minutes. Add a river cruise from Jinling East Road pier (10 minutes south) and you have an evening.")],
      [("Is the Bund free?","Yes. The promenade has no ticket. Only the cruises, observation decks and the sightseeing tunnel cost money."),
       ("Which metro exit for the Bund?","East Nanjing Road station, Lines 2 and 10, exit 2 or exit 7, then walk east along Nanjing East Road to the river."),
       ("What time do the Bund lights turn off?","Usually 22:00 on both banks. They come on around 18:00 in winter and around 19:30 in summer."),
       ("Is the Bund better by day or by night?","Arrive about 45 to 60 minutes before sunset and you get both. Weekday mornings are the quiet option for photos.")],
      [("Wander in China: The Bund guide (updated 21 July 2026)","https://www.wanderinchina.com/destinations/shanghai/the-bund/",False)],
      SITE+"/og/the-bund-shanghai-at-night.jpg",
      related=[("/guides/nanjing-road-shanghai/","nanjing-road-shanghai-neon-shop-fronts-cover-4x5","SHANGHAI","Nanjing Road: how to walk it and when the neon is on"),("/guides/huangpu-river-night-cruise/","huangpu-river-night-cruise-from-the-water-cover-4x5","SHANGHAI","Huangpu River night cruise: which pier and which ticket")],
      gallery=[("the-bund-shanghai-after-dark-cover-4x5","The Bund after dark, gold lit bank buildings"),("the-bund-shanghai-52-historic-buildings-slide","Bund buildings lit at night"),("the-bund-shanghai-mix-of-architecture-styles-slide","The Bund promenade at night"),("pudong-oriental-pearl-tower-468-metres-slide","Bund facade detail at night"),("the-bund-save-it-for-your-trip-slide","Pudong skyline from the Bund")],
      place={"name":"The Bund","city":"Shanghai","free":True},steps_title="How to do the Bund in one evening",
      shorts={"Instagram":"https://www.instagram.com/scratchandroam/","TikTok":"https://www.tiktok.com/@scratchandroam","Pinterest":"https://www.pinterest.com/scratchandroam/"})

guide("nanjing-road-shanghai","Nanjing Road Shanghai: metro exit, neon times and the walk","Nanjing Road in Shanghai: how to walk it, which metro exit, when the neon comes on",
      "Nanjing Road pedestrian street: 1.6 km from People's Square to the Bund, metro exits at each end, neon on from 18:00 or 19:00 until 22:00, and the walk that ends at the river.",
      "Nanjing Road Shanghai",None,
      "<p>Nanjing Road is the long pedestrian shopping street that runs from People's Square to the Bund. It is loud, bright and busy, and the trick is to walk it in one direction at the right hour so it ends at the river with the lights on.</p>"+CHECK,
      [("Start at People's Square","People's Square station is on Lines 1, 2 and 8. Exit 19 brings you straight into the New World City basement; come up and you are at the west end of the street."),
       ("Walk east, about 1.6 km","The pedestrian section is car free. The old department stores (No. 1 Department Store, Wing On) and the neon signs are along the middle stretch."),
       ("Time it for the neon","Signs come on at 19:00 from June to September and at 18:00 from October to May, and go off at 22:00. Evening from about 17:00 to 22:00 is the time; weekday evenings are quieter than weekends."),
       ("Keep going past Henan Road to the Bund","The last 500 m east of Henan Road was pedestrianised in 2020 and leads straight to the Peace Hotel and the river. Do this bit at the end, not the start."),
       ("If you only want the east end","East Nanjing Road station, Lines 2 and 10, exit 2 puts you on the street; exit 3 is quieter if you have luggage."),
       ("Taxis and DiDi stop at the edge","Cars cannot enter. Drop-off points are the side streets such as West Tibet Road, Henan Middle Road or Jiujiang Road.")],
      [("How long is Nanjing Road pedestrian street?","About 1.6 km of pedestrian-only street, from People's Square to the Bund. Allow an hour to walk it with stops."),
       ("Which metro station for Nanjing Road?","People's Square (Lines 1, 2, 8) for the west end, East Nanjing Road (Lines 2, 10) for the east end near the Bund."),
       ("When do the Nanjing Road lights come on?","18:00 from October to May, 19:00 from June to September, off at 22:00."),
       ("Does Nanjing Road connect to the Bund?","Yes. Walk east past Henan Road and the street ends at the Peace Hotel on the Bund, about 500 m further.")],
      [("Wander in China: Nanjing East Road guide (updated 8 June 2026)","https://wanderinchina.com/destinations/shanghai/nanjing-east-road/",False)],
      SITE+"/og/nanjing-road-shanghai.jpg",
      related=[("/guides/the-bund-shanghai-at-night/","the-bund-shanghai-after-dark-cover-4x5","SHANGHAI","The Bund at night: how to get there and when to go"),("/guides/huangpu-river-night-cruise/","huangpu-river-night-cruise-from-the-water-cover-4x5","SHANGHAI","Huangpu River night cruise: which pier and which ticket")],
      gallery=[("nanjing-road-shanghai-neon-shop-fronts-cover-4x5","Nanjing Road neon shop fronts"),("nanjing-road-day-mood-night-mood-slide","Nanjing Road at night"),("nanjing-road-1-2-km-pedestrian-street-slide","Shops on Nanjing Road"),("nanjing-road-cute-stop-shanghai-in-chocolate-slide","Nanjing Road crowd and lights"),("nanjing-road-come-roam-with-me-slide","Nanjing Road by day")],
      place={"name":"Nanjing Road Pedestrian Street","city":"Shanghai","free":True},steps_title="How to walk Nanjing Road",
      shorts={"Instagram":"https://www.instagram.com/scratchandroam/","TikTok":"https://www.tiktok.com/@scratchandroam","Pinterest":"https://www.pinterest.com/scratchandroam/"})

guide("huangpu-river-night-cruise","Huangpu River night cruise Shanghai: pier, ticket, time","Huangpu River night cruise in Shanghai: which pier, which ticket, and which side to stand on",
      "Three piers, three cruise lengths, about 120 to 150 RMB for the standard night cruise. How to book as a foreigner, why your passport matters, and which side of the boat to stand on.",
      "Huangpu River night cruise",None,
      "<p>The night cruise is the one Shanghai thing that looks exactly like the photos. Both banks are lit, the boat is slow, and you are in the middle. The confusing part is the booking: three piers, tickets tied to one of them, and a voucher that is not a boarding pass. Here is the version that worked for us.</p>"+CHECK,
      [("Pick the pier before the ticket","Shiliupu pier (south end of the Bund) has the most routes. Jinling East Road pier (middle of the Bund) is best for a short ride and a 10 minute walk from East Nanjing Road station. Oriental Pearl pier is on the Pudong side. Your ticket only works at its own pier."),
       ("Choose the length","30 minutes express (about 80 to 100 RMB, mostly from Jinling East Road), 45 to 60 minutes classic (about 120 to 150 RMB, all piers, the usual choice), or 90 minutes plus, often a dinner cruise from Shiliupu (250 to 400 RMB and up)."),
       ("Go between 19:00 and 21:00","That is when both banks are fully lit. Some landmark lighting goes off after 21:00 or 22:00, so the last boats see less. The 17:00 to 19:00 sunset slot gives you daylight and then lights."),
       ("Book online, then swap the voucher at the pier","An online booking is a voucher, not a ticket. Exchange it at the pier window with your original passport; a photo of it is not accepted. Night cruise collection windows are roughly 17:00 to 20:00."),
       ("Arrive 30 to 60 minutes early","Pre-booking skips the ticket queue but not security, which can take 20 to 60 minutes on busy evenings."),
       ("Stand on the left going north","From Shiliupu heading north the Bund buildings are on the left; on the way back Pudong is on the left. Skip the cruise in rain or fog, the towers disappear.")],
      [("How much is the Huangpu River night cruise?","About 120 to 150 RMB for the standard 45 to 60 minute sightseeing cruise, 80 to 100 RMB for the 30 minute express, more for VIP decks and dinner cruises (figures from a Trip.com guide dated August 2026)."),
       ("Which pier is best for the Huangpu cruise?","Shiliupu for choice of routes, Jinling East Road for a short ride near the Bund, Oriental Pearl if you are staying in Pudong. Tickets are tied to one pier."),
       ("Do I need my passport for the river cruise?","Yes, the original. Online bookings are exchanged for tickets at the pier window against your passport."),
       ("What time is best for the Huangpu night cruise?","Between 19:00 and 21:00, when both banks are fully lit. Some lights go off from 21:00 to 22:00.")],
      [("Trip.com: Huangpu River cruise guide (10 August 2026)","https://www.trip.com/guide/attraction/huangpu-river-cruise.html",False)],
      SITE+"/og/huangpu-river-night-cruise.jpg",
      related=[("/guides/the-bund-shanghai-at-night/","the-bund-shanghai-after-dark-cover-4x5","SHANGHAI","The Bund at night: how to get there and when to go"),("/guides/shanghai-circus-world-era-show/","shanghai-circus-world-act-1-aerial-silks","SHANGHAI","Shanghai Circus World ERA show: tickets and how to get there")],
      gallery=[("huangpu-river-night-cruise-from-the-water-cover-4x5","Shanghai skyline from the Huangpu river at night"),("huangpu-river-light-show-times-slide","Pudong towers from the water"),("huangpu-river-same-river-new-angle-slide","Bund buildings from the cruise"),("huangpu-river-bund-side-and-pudong-side-slide","Lujiazui lit up from the river"),("huangpu-river-take-the-cruise-slide","The Oriental Pearl tower from the water")],
      place={"name":"Huangpu River Cruise","city":"Shanghai","free":False},steps_title="How to book and board",
      shorts={"Instagram":"https://www.instagram.com/scratchandroam/","TikTok":"https://www.tiktok.com/@scratchandroam","Pinterest":"https://www.pinterest.com/scratchandroam/"})

guide("shanghai-circus-world-era-show","Shanghai Circus World ERA show: tickets and how to get there","Shanghai Circus World ERA show: how to book tickets, where to sit, how to get there",
      "ERA at Shanghai Circus World: metro Line 1 to Shanghai Circus World station exit 3, shows at 19:30 Tuesday to Sunday, ticket zones from about 280 to 880 RMB, and where foreigners can book.",
      "Shanghai Circus World ERA tickets",None,
      "<p>We saw the acrobatics show at Shanghai Circus World on a weeknight and filmed five of the acts (the long video is on YouTube). The show is excellent. The part people search for is the boring part: where to buy the ticket, which zone, and how to get to a venue that is not in the centre. So that is this page.</p>"+CHECK,
      [("Get there on Line 1","Shanghai Circus World has its own metro station on Line 1 (上海马戏城). Take exit 3 and the venue is about 3 minutes on foot. Evening traffic makes taxis slower than the metro."),
       ("Check the show times for your date","Evening show at 19:30, Tuesday to Sunday, with Monday usually dark. Saturday and Sunday add a 14:00 matinee. Weekday shows are the shorter 60 minute version; the full 100 minute version is most often on Sundays."),
       ("Book online before you go","Official site: shcircusworld.com. Trip.com sells zone tickets with QR entry, listing Zone A around 580 RMB and Zones B and C around 380 RMB, with the seat assigned inside the zone. The box office opens around 09:30 but weekends sell out."),
       ("Pick a zone, not a seat","Zones differ by distance and angle, not quality. Rows 3 to 7 of Zone A are a good balance for floor acts and overhead acts. VIP (around 880 RMB) is closest for the floor acts."),
       ("Arrive by 19:00","Scanning starts about 30 minutes before the show, and latecomers are held at the door until the first act ends."),
       ("Photos only in the breaks","Rules on flash and video vary; photos during applause are generally fine, long video recording is not.")],
      [("How do I get to Shanghai Circus World?","Metro Line 1 to Shanghai Circus World station, exit 3, then a 3 minute walk. Address: 2266 Gonghexin Road, Jing'an District."),
       ("How much are ERA tickets?","Roughly 280 to 880 RMB depending on zone (VIP 880, A 580, B 380, side and upper sections 280 to 480), per a 2026 guide. Check the official site or Trip.com for the date."),
       ("Where can foreigners book ERA tickets?","The official site shcircusworld.com, Trip.com (QR code entry), or the venue box office from about 09:30."),
       ("What time is the ERA show?","19:30 Tuesday to Sunday, plus 14:00 on Saturday and Sunday. Monday is usually a rest day.")],
      [("Nomado: ERA acrobatics show guide (2026)","https://www.nomadotravel.app/en/attractions/era-acrobatics-show",False),("Shanghai Circus World official site","https://www.shcircusworld.com/",True)],
      SITE+"/og/shanghai-circus-world-era-show.jpg",
      related=[("/guides/huangpu-river-night-cruise/","huangpu-river-night-cruise-from-the-water-cover-4x5","SHANGHAI","Huangpu River night cruise: which pier and which ticket"),("/guides/the-bund-shanghai-at-night/","the-bund-shanghai-after-dark-cover-4x5","SHANGHAI","The Bund at night: how to get there and when to go")],
      gallery=[("shanghai-circus-world-act-1-aerial-silks","Aerial silks act at Shanghai Circus World"),("shanghai-circus-world-act-2-hand-balance","Hand balance act"),("shanghai-circus-world-act-3-laser-lights","Laser light act"),("shanghai-circus-world-act-4-aerial-hoop","Act four at Shanghai Circus World"),("shanghai-circus-world-act-5-the-sphere","Act five at Shanghai Circus World")],
      place={"name":"Shanghai Circus World","city":"Shanghai","free":False},steps_title="How to book and get there",
      shorts={"YouTube":"https://www.youtube.com/@scratchandroam","Instagram":"https://www.instagram.com/scratchandroam/","TikTok":"https://www.tiktok.com/@scratchandroam"})

# ---- China do's and don'ts (SR-0021, 16 Oct 2026): Contraband board matching the reel and carousel ----
DD_ROUNDS=[
 ("customs","#FF2E2E","#fff","Round 01 / 04","Customs will <em>take it</em>","What you can't bring into China",[
  ("01","Fruit, meat, dairy","CONFISCATED","Sealed, cooked, the airplane apple. All of it. Bin.",
   "China's quarantine list bans <b>fresh fruit and vegetables, meat and meat products (raw or cooked), eggs, fresh milk, cheese, butter and cream</b>. Sealed packaging makes no difference. Eat the plane snack on the plane or drop it in the bins before customs. Packaged sweets, crisps and biscuits are generally fine.",
   "China consulate list; Sanya Airport customs (official); Trip.com 2026",False,"X-ray of an apple"),
  ("02","Sensitive media","CONFISCATED","Political books, prints, files. Customs decides what counts.",
   "China Customs bans printed matter, films, photos, discs and computer storage media that it considers <b>harmful to China's politics, economy, culture or morals</b>. The wording is broad and the officer decides, so leave anything political at home.",
   "China Customs (GACC) prohibited list, via Gulf News",False,"X-ray of a stack of books"),
  ("03","A drone, in Beijing","CONFISCATED","Banned from entering the city. Soon you can't even own one there.",
   "Bringing a drone into Beijing from outside the city is already prohibited, tourists included, and from <b>15 November 2026</b> owning or storing a drone inside the city limits is banned too. Drones can be confiscated and fines issued. Elsewhere in China you can still fly outdoors, but the drone needs real-name registration.",
   "AP via The Star, 13 September 2026",False,"X-ray of a drone"),
 ]),
 ("security","#FF8A00","#0A0A0C","Round 02 / 04","Security will <em>take it</em>","At airport security in China",[
  ("04","Power bank with no 3C mark","CONFISCATED","Flying inside China? It stays at security.",
   "Since <b>28 June 2025</b>, power banks without a clearly printed 3C (CCC) mark are banned on domestic flights in mainland China and are taken at security. Most power banks bought in Ireland or the UK do not have it. On trains and in the city it is no problem; it only matters at the airport. If you fly between cities, buy a 3C power bank in China.",
   "CAAC rule, via Techlicious 2026 and China Discovery",False,"X-ray of a battery"),
  ("05","Lighters and matches","BINNED","Not in your pocket. Not in your suitcase.",
   "Chinese authorities do not allow matches or lighters in the cabin or in checked bags, and you will be asked to throw them away at the security checkpoint. Buy a cheap one after you land if you need it.",
   "JAL, Beijing Capital Airport page; Trip.com 2026",False,"X-ray of a flame"),
  ("06","Cold meds like Sudafed","SECOND LOOK","Pseudoephedrine is controlled. Read the label first.",
   "Pseudoephedrine, the decongestant in Sudafed and many cold and flu tablets, is <b>strictly controlled in China</b>. Check the ingredients of every cold medicine before you pack it, keep medicines in the original box, and carry the prescription and a doctor's letter for anything prescribed.",
   "Travel China With Me; Trvlogue, August 2026",False,"X-ray of a capsule"),
  ("07","Cash over ¥20,000","DECLARE IT","Or US$5,000. Declare it, or explain it.",
   "Carrying more than <b>¥20,000 in Chinese cash, or foreign cash worth more than US$5,000</b>? It is not banned, but you must declare it in the red channel when you arrive.",
   "Shanghai government customs guide (official)",False,"X-ray of a banknote bundle"),
 ]),
 ("etiquette","#B26BFF","#0A0A0C","Round 03 / 04","Don't <em>do this</em>","Table manners and habits that get stares",[
  ("08","Chopsticks upright in rice","RUDE","In your rice they look like funeral incense. Lay them down.",
   "Standing chopsticks upright in a bowl of rice looks like the <b>incense burned for the dead</b>, Beijing's official tourism site explains. Lay them across the bowl or on the chopstick rest instead.",
   "Visit Beijing (official tourism site)",False,"X-ray of a rice bowl with chopsticks standing in it"),
  ("09","Tapping your bowl","RUDE","Old saying: tap your bowl, beg for life. Stop drumming.",
   "The old saying goes <b>tap your bowl and you'll be a beggar for life</b>, because beggars once tapped their bowls for attention. Tapping the bowl or the table with your chopsticks is simply seen as rude.",
   "Visit Beijing (official tourism site); China Highlights",False,"X-ray of chopsticks"),
  ("10","Hands off heads","DON'T","In Tibetan areas the head is sacred. Everywhere else, it's just weird.",
   "This one is less strict than people say. It is not a strong taboo across most of mainland China. The clear rule is in <b>Tibetan areas</b>, where the head is considered sacred, so do not touch a Tibetan person on the head. Everywhere else, touching a stranger's head is just personal space.",
   "China Highlights etiquette guide; Chinese Forums",False,"X-ray of a person getting a head massage"),
  ("11","Drinking tap water","BOIL IT","Locals don't. They boil it, or make tea.",
   "Even in Beijing, where the tap water is among the cleanest in the country, it is <b>not considered safe to drink straight from the tap</b>. Locals boil it or drink tea. Use the kettle or bottled water.",
   "Natali; Visit Beijing (official tourism site)",True,"X-ray of a tap and a glass"),
 ]),
 ("instead","#2BD67B","#0A0A0C","Round 04 / 04","Do this <em>instead</em>","What to pack, and what to just buy there",[
  ("12","Bring a plug adapter","PACK IT","Irish and UK plugs fit zero sockets.",
   "Mainland China runs on <b>220V with Type A and Type I sockets</b>. Irish and UK three-pin plugs (Type G) fit none of them, and most European, Indian, South African and US three-pin plugs do not fit either. Australian plugs do. Phone and laptop chargers usually handle 220V; check single-voltage hair tools.",
   "Chinavigators; Travel of China; Trip.com",False,"X-ray of a plug"),
  ("13","Deodorant, SPF, tampons","PACK IT","The ones you trust are hard to find. Bring your own.",
   "Strong antiperspirant is hard to find outside big cities, a lot of sunscreen sold in China adds <b>skin whitener</b>, and pads are far more common than tampons (Watsons in big cities stocks a few, often one brand). Bring the ones you trust.",
   "The Culture Trip; Travel China Cheaper; Sara Jaaksola",False,"X-ray of a lotion bottle"),
  ("14","Tissues? Buy them there","BUY THERE","Toilets rarely have paper, but every corner shop sells pocket packs.",
   "Most public toilets have no paper and often no soap, but don't fill your suitcase with rolls: <b>pocket tissue packs are sold everywhere</b> for very little. Keep two packs and a small hand sanitiser in your day bag. In older buildings the paper goes in the bin, not the toilet.",
   "Natali; Chinavigators; Travel China Cheaper",True,"X-ray of a toilet roll"),
  ("15","Not expired","STILL GOOD","That date is the day it was made. Add the shelf life.",
   "Chinese packaging usually prints the <b>production date (生产日期)</b> and a <b>shelf life (保质期)</b>, for example 12 months. The date you see is when it was made, so add the shelf life to get the expiry. The new national label standard GB 7718-2025 makes the expiry date compulsory from 16 March 2027.",
   "Natali; SAMR 2024 via CIRS; GB 7718-2025 via REACH24H",True,"X-ray of a tin can"),
 ]),
]
import json as _json
DD_ICON=_json.load(open("src/dd_icons.json"))
DD_SLIDES=["china-dos-and-donts-carousel-1-china-will-take-your-drone","china-dos-and-donts-carousel-2-customs-will-take-it","china-dos-and-donts-carousel-3-security-will-take-it","china-dos-and-donts-carousel-4-dont-do-this","china-dos-and-donts-carousel-5-do-this-instead"]
def _dd_board():
    jump="".join(f'<a href="#{rid}" style="--c:{c}">{html.escape(t.replace("<em>","").replace("</em>",""))}</a>' for rid,c,ink,k,t,sub,items in DD_ROUNDS)
    out=f'<section class="dd" aria-label="China do\'s and don\'ts"><div class="dd-top"><span>SCAN / ARRIVALS</span><span class="rec">● 15 ITEMS FLAGGED</span></div><div class="dd-jump">{jump}</div>'
    for rid,c,ink,k,t,sub,items in DD_ROUNDS:
        out+=f'<div class="dd-round" id="{rid}" style="--c:{c};--ink:{ink}"><p class="dd-k">{k}</p><h2>{t}</h2><p class="dd-sub">{sub}</p>'
        for n,name,v,sar,body,src,tip,alt in items:
            t_=' <span class="dd-tip">NATALI\'S TIP</span>' if tip else ''
            out+=f'<div class="dd-item" id="dd-{n}"><img src="/img/dd/china-customs-xray-icon-{DD_ICON[n]}.png" alt="{html.escape(alt)}" width="96" height="96" loading="lazy"><div><span class="dd-v">{v}</span>{t_}<h3><i>#{n}</i>{html.escape(name)}</h3><p class="dd-s">{html.escape(sar)}</p><p>{body}</p><p class="dd-src">SRC: {html.escape(src)}</p></div></div>'
        out+='</div>'
    slides="".join(f'<img src="/img/{DD_SLIDES[i-1]}.jpg" alt="China do\'s and don\'ts carousel, slide {i} of 5" loading="lazy">' for i in range(1,6))
    out+=f'<div class="dd-end"><b>Save this. <em>Or learn it the hard way.</em></b><p>Send it to the friend who packs a drone. The same list as a carousel, to screenshot or save:</p><div class="dd-slides">{slides}</div></div></section>'
    return out

guide("china-dos-and-donts","China do's and don'ts: 15 rules before you fly (2026)","China do's and don'ts: what not to bring, and what not to do",
      "China do's and don'ts for first-timers: what customs and airport security take off you, the table manners that get stares, and what to pack or just buy there.",
      "china do's and don'ts",None,
      "<p>Most China packing lists tell you to download a VPN and call it a day. These China do's and don'ts are the other stuff: what customs and airport security will actually take off you, the table habits that get you stares, and what to pack versus what to just buy when you land.</p><p>It is the written version of the Scratch &amp; Roam short, in the same order. Three of the tips are mine from the trip, marked as Natali's tip; everything else was checked on 16 October 2026 against the sources at the bottom.</p>",
      [],
      [("What can't you bring into China?","Fresh fruit and vegetables, meat and meat products, eggs, fresh milk, cheese, butter and cream, seeds and soil, and media that China Customs considers politically harmful. Drones cannot be brought into Beijing."),
       ("Can I bring a power bank to China?","Yes, into the country. But on domestic flights inside China it needs a clearly printed 3C mark, or security takes it."),
       ("Can you drink tap water in China?","No. Even in Beijing it is not considered safe straight from the tap. Boil it, drink tea, or buy bottled water."),
       ("Is it rude to stick chopsticks in rice in China?","Yes. Chopsticks standing upright in rice look like incense burned for the dead. Lay them across the bowl or on the rest."),
       ("Do I need a plug adapter for China from Ireland or the UK?","Yes. Irish and UK three-pin plugs fit no socket in mainland China, which uses Type A and Type I at 220V.")],
      [("Chinese Consulate General in Sydney: objects prohibited from being carried into China","https://sydney.china-consulate.gov.cn/eng/zlgdt/previous2024b_/202208/t20220825_10752452.htm",True),
       ("Sanya Phoenix International Airport: international customs clearance","https://en.sanyaairport.com/engjtg.jhtml",True),
       ("Trip.com: restricted and prohibited items for China entry, 2026","https://uk.trip.com/guide/info/china-prohibited-restricted-items.html",False),
       ("Gulf News: China customs prohibited items, citing customs.gov.cn","https://gulfnews.com/living-in-uae/ask-us/uae-travelling-to-china-what-customs-regulations-do-i-need-to-know-of-1.1689605810796",False),
       ("The Star (AP): Beijing bans drone possession in the city, 13 September 2026","https://www.thestar.com.my/aseanplus/aseanplus-news/2026/09/13/beijing-bans-drone-possession-in-the-city-after-earlier-moves-to-tighten-rules",False),
       ("Techlicious: flying within China, your power bank needs a 3C label","https://www.techlicious.com/tip/flying-within-china-your-power-bank-needs-a-3c-label/",False),
       ("China Discovery: China power bank rules 2026","https://www.chinadiscovery.com/articles/china-power-bank-rules-3c-certification-guide.html",False),
       ("JAL: Beijing Capital International Airport information","https://jal.co.jp/en/inter/airport/pek/info",False),
       ("Trip.com: can I bring a lighter on a plane in China?","https://au.trip.com/guide/info/can-i-bring-a-lighter-on-a-plane.html",False),
       ("Travel China With Me: traveling to China with medicine","https://travelchinawith.me/china-facts/traveling-to-china-with-medicine/",False),
       ("Trvlogue: China medicine regulations 2026","https://www.trvlogue.com/en/china-medicine-regulations-2026",False),
       ("Shanghai government: customs clearance guide for inbound passengers","https://english.shanghai.gov.cn/en-CustomsRegulations/20231212/9a3c7f512d464e0798be3fc76c8dd6f2.html",True),
       ("Visit Beijing: chopsticks etiquette","https://english.visitbeijing.com.cn/article/47ONGlfHcES",True),
       ("Visit Beijing: tap water","https://english.visitbeijing.com.cn/article/47ON183WTWN",True),
       ("China Highlights: do's and don'ts in China","https://www.chinahighlights.com/travelguide/guidebook/etiquette.htm",False),
       ("Chinese Forums: touching a child's head","https://www.chinese-forums.com/forums/topic/7557-culture-question-touching-a-childs-head/",False),
       ("Chinavigators: do you need a power adapter for China?","https://www.chinavigators.com/power-adapter-china/",False),
       ("Travel of China: travel adaptors for China","https://www.travelofchina.com/travel-adaptors-for-china/",False),
       ("Trip.com: China plug guide","https://in.trip.com/guide/info/china-plug.html",False),
       ("The Culture Trip: things to bring when you move to China","https://theculturetrip.com/articles/12-things-to-bring-when-you-move-to-china",False),
       ("Travel China Cheaper: China packing checklist","https://www.travelchinacheaper.com/China-travel-packing-checklist",False),
       ("Sara Jaaksola: what you should really bring to China","https://sarajaaksola.com/what-should-you-really-bring-to-china",False),
       ("Chinavigators: the China toilet guide","https://www.chinavigators.com/china-toilet-guide/",False),
       ("CIRS: SAMR on production date and shelf life labelling, March 2024","https://www.cirs-group.com/en/food/china-samr-issues-announcement-on-encouraging-food-enterprises-to-improve-the-labeling-of-production-dates-and-shelf-lives-of-pre-packaged-foods",False),
       ("REACH24H: China 2025 food labelling regulation (GB 7718-2025)","https://en.reach24h.com/news/insights/food/china-2025-food-labeling-regulations-key-changes",False)],
      SITE+"/og/china-dos-and-donts.jpg",
      related=[("/guides/first-time-in-china/","first-time-in-china-13-things-before-you-fly","13-point checklist","First time in China: 13 things to set up before you fly"),
               ("/guides/china-travel-apps/","china-travel-apps-12-apps-to-set-up-before-china","12 apps","Apps to download before you go to China"),
               ("/guides/china-arrival-card-pc/","china-arrival-card-on-a-pc-step-by-step","Arrival card","China arrival card online, step by step")],
      checked="2026-10-16",
      lift='<div class="dd-hero"><img data-hero src="/img/china-will-take-your-drone-15-dos-and-donts.jpg" alt="China will take your drone: 15 do\'s and don\'ts, an airport X-ray monitor with a confiscated drone" width="1280" height="720"></div>',
      extra=_dd_board())

# ---------- Taobao ordering guide (SR-0023) ----------
TB_STEPS=[
 ("Open Settings and check your language, country and currency",
  "Tap <b>My Taobao</b> (bottom right), then the small gear for <b>Settings</b>. You will see country, language and currency. <b>First-hand:</b> on my own account, bought from Ireland, Chinese was the only language on offer, and Ireland was not on the list. Taobao's English interface appears to depend on the region of your account, and the third-party guides I found only name Singapore, Malaysia, Hong Kong and Macau. I could not find an official Taobao page that lists the regions, so check your own Settings instead of trusting any list, including mine."),
 ("Switch the currency to euro",
  "Even with the app in Chinese, the currency can be changed. After I switched to euro, every price showed a rough euro amount underneath the yuan price. It is an estimate, not what your bank will charge, but it is enough to see at a glance whether something is cheap."),
 ("Search in English, and translate what you cannot read",
  "Type what you want in English, for example <b>phone case</b>, and results come up. <b>Taobao's search box took English when I tried it.</b> When a button or a product page makes no sense, use your phone's built-in translation instead of copying text into another app. On an iPhone (XS, XR or newer, on iOS 15 or later) Live Text lets you tap the text in the camera view and translate it. On Android, Circle to Search has a Translate option on supported phones. Both are official features, set up in the phone's own settings, not in Taobao."),
 ("Add your delivery address before you buy anything",
  "Tap <b>delivery address</b>, then <b>add new address</b>. Do this first. If you skip it, Taobao will stop you at checkout and ask for it anyway (more on that in step 10). Always write your name in English, even if the rest of the address is in Chinese."),
 ("Sending to a hotel: message them first",
  "Email them, or message on WeChat if they use it. Give your name, your booking number and your dates. Ask whether it is okay to receive a parcel before you arrive. Ask for their exact address and the reception phone number, in Chinese, so you can copy it into Taobao character for character. Do not order until they say yes."),
 ("Write the note in Chinese, and ask for it to be left at reception",
  "Let an AI assistant (Gemini, Claude or ChatGPT) write the address note in Chinese. The point of the note: leave the parcel at reception or in the parcel locker, and <b>do not call the guest</b>. For example: <b>包裹请放前台或快递柜，请勿致电客人</b>. That is an AI translation. Show it to the hotel in your first message so they can tell you if the wording is wrong."),
 ("Add your own phone number, with the country code",
  "The phone field is not there for calls. Couriers and hotel staff often see only the last four digits, and that is how they match a parcel to a guest. Add your own number with your country code. In my experience this is what keeps parcels from being lost: I have ordered tens of packages this way and not one was lost. That is my own record, not a guarantee."),
 ("Check the delivery time before you order",
  "<b>Do not order to a hotel if you are staying only one to three days.</b> Delivery can take up to three days, and the parcel may arrive after you have checked out. The delivery estimate is shown on the product page and at checkout; read it before you pay."),
 ("Pick your item, then add it to the cart or buy now",
  "On the product page choose the options, such as your phone model and then the colour. Then tap <b>add to cart</b>, or <b>buy now</b> if you are sure. Not sure yet? Tap the star to save it to your <b>favourites</b>."),
 ("Go to the cart and check out",
  "In the cart, tick what you want and tap <b>checkout</b>. If you have not added an address yet, a pop-up will ask for one first. Once the address is in, submit the order."),
 ("Pay with Alipay",
  "Pay through Alipay with your own bank card. Set Alipay up at home before you fly; the steps are in my <a href=\"/guides/china-travel-apps/\">China travel apps guide</a>. Trip.com and China for Travelers both report a 3% fee on Alipay card payments over ¥200, but their wording differs on whether exactly ¥200 is included, so check the fee shown in your own Alipay before paying. I did not find Taobao-specific Alipay rules for foreign cards on an official page."),
 ("Find the order under My orders",
  "Once paid, everything lives under <b>My orders</b> in the My Taobao tab: to pay, to ship, to receive, and refunds. This is where you follow delivery and where you tap to confirm receipt when the parcel arrives."),
]
TB_FIGS={0:["taobao-app-my-taobao-tab-and-settings-gear-english-labels","taobao-settings-country-language-currency-english-label","taobao-language-country-currency-page-english-labels"],
 1:["taobao-currency-list-pick-euro-english-label","taobao-euro-estimate-under-every-price-english-label"],
 2:["taobao-search-bar-english-label","taobao-search-type-in-english-labels"],
 3:["taobao-settings-delivery-address-english-label","taobao-add-new-address-button-english-label"],
 5:["taobao-address-form-full-address-and-door-number-english-label"],
 6:["taobao-address-form-recipient-name-and-phone-english-labels"],
 8:["taobao-product-options-phone-model-colour-add-to-cart-english-labels","taobao-product-page-favourite-star-english-label"],
 9:["taobao-cart-tick-items-and-checkout-english-labels","taobao-checkout-popup-set-delivery-address-first-english-label"],
 11:["taobao-my-orders-to-pay-to-ship-to-receive-refunds-english-labels"]}
TB_STEPS=[(a,b,TB_FIGS.get(i,[])) for i,(a,b) in enumerate(TB_STEPS)]

VF_STEPS=[
 ("Check your passport is on the list","The list covers ordinary passports from Ireland, the UK (added from 17 February 2026) and most EU countries. In the 27 EU countries, 25 are on it: Czechia and Lithuania are not."),
 ("Check the end date, not only the 30 days","The policy runs until 24:00 on 31 December 2026, Beijing time. A trip that starts in December has to fit before that moment. 2027 has not been announced, so do not book a 2027 trip on the assumption that it continues."),
 ("Check your passport validity","The UK government says your passport must expire at least 6 months after the day you arrive and have 2 blank pages. I use 6 months as the safe rule for Irish and EU passports too, but I did not find the same line on an Irish government page, so check yours."),
 ("Fill in the free arrival card before you fly","China has a free online arrival card, run on official channels only. Paid copycat sites exist. See my arrival card guides for the step by step."),
 ("Carry proof of your trip","The embassy FAQ recommends carrying documents such as an invitation letter, air tickets and accommodation bookings that match why you are visiting. It does not say they are always asked for. A ticket and a hotel booking on your phone is the sensible minimum."),
 ("Plan the 30 days as a hard limit","You cannot extend visa-free time. If you must stay longer for good reason you apply for a stay permit from the local exit-entry police, which is not a normal holiday option. For a longer trip, get the right visa before you fly."),
]

guide("china-visa-free-30-days","China Visa Free 30 Days: Irish, UK and EU Passports","China visa free 30 days: Irish, UK and EU passports",
      "Who gets 30 days visa free in China right now, until when, what to show at the border, and whether you can extend or leave and come back. Checked 17 October 2026.",
      "china visa free 30 days","",
      "<p>If you hold an Irish, UK or EU passport, you can currently enter China without a visa for up to 30 days. The catch is the date: the policy runs until 24:00 on 31 December 2026, Beijing time, and nothing has been announced for 2027. This page answers the four things people ask, with the source for each, checked on 17 October 2026.</p><p>It is a guide, not legal advice. The embassy and your own government's travel page are the final word, so open them once more before you fly.</p>",
      VF_STEPS,
      [("Who gets 30 days visa free in China right now?","Ordinary passport holders from Ireland, the UK (from 17 February 2026) and the EU countries on the list can enter for up to 30 days, for tourism, business, family or friend visits, or transit. In the EU, Czechia and Lithuania are not on it."),
       ("Until when is China visa free?","Until 24:00 Beijing time on 31 December 2026. 2027 has not been announced. Earlier extensions were announced in late 2024 and early November 2025, but that is history, not a promise."),
       ("What do I show at the border?","A passport valid for at least 6 months with 2 blank pages, plus your free arrival card. The embassy recommends carrying an air ticket, accommodation booking or invitation letter that matches your purpose."),
       ("Can I extend visa free time in China?","No. If you must stay longer for good reason you can apply for a stay permit from the local exit-entry police. For a planned longer trip, apply for the right visa before you fly."),
       ("Can I leave China and come back for another 30 days?","The embassy says you can enter visa free multiple times and that there is currently no cap on the number of entries or total days. Entries must still match a visit purpose such as tourism, so this is not a way to live there. Rules can change.")],
      [("Embassy of China in Ireland: FAQ on visa-free entry","https://ie.china-embassy.gov.cn/eng/qzfw/202412/t20241219_11506444.htm",True),
       ("Embassy of China in Ireland: notice on extending the unilateral visa-free policy (4 Nov 2025)","https://ie.china-embassy.gov.cn/eng/qzfw/202511/t20251104_11746287.htm",True),
       ("Chinese Visa Application Service Centre London: notice on the extension, 4 Dec 2025","https://bio.visaforchina.cn/LON3_EN/tongzhigonggao/315858144490295296.html",True),
       ("UK government: China entry requirements","https://www.gov.uk/foreign-travel-advice/china/entry-requirements",True)],
      SITE+"/og/china-visa-free-30-days.jpg",checked="2026-10-17",published="2026-10-17",vschema=False,
      lift='<div class="dd-hero"><img data-hero src="/img/china-visa-free-30-days-departure-board-cover-16x9.jpg" alt=""></div>',
      steps_title="What to check before you fly",
      extra='<h2>The carousel</h2><div class="shots"><figure><a href="/img/china-visa-free-30-days-who-can-board-slide.jpg"><img src="/img/china-visa-free-30-days-who-can-board-slide.jpg" alt=""></a><figcaption>Who can board</figcaption></figure><figure><a href="/img/china-visa-free-30-days-time-left-slide.jpg"><img src="/img/china-visa-free-30-days-time-left-slide.jpg" alt=""></a><figcaption>Time left</figcaption></figure><figure><a href="/img/china-visa-free-30-days-at-the-desk-slide.jpg"><img src="/img/china-visa-free-30-days-at-the-desk-slide.jpg" alt=""></a><figcaption>At the desk</figcaption></figure><figure><a href="/img/china-visa-free-30-days-changes-slide.jpg"><img src="/img/china-visa-free-30-days-changes-slide.jpg" alt=""></a><figcaption>What you cannot change</figcaption></figure><figure><a href="/img/china-visa-free-30-days-last-call-slide.jpg"><img src="/img/china-visa-free-30-days-last-call-slide.jpg" alt=""></a><figcaption>Last call</figcaption></figure></div><p class="note">How I count the 30 days in the video: landing day is day 0 and day 30 is the last day. The embassy wording is from the date of entry to the 30th calendar day until 24:00, so if your exit is close to the limit, leave a day early.</p>',
      shorts={"Instagram":"https://www.instagram.com/scratchandroam/","TikTok":"https://www.tiktok.com/@scratchandroam","Pinterest":"https://www.pinterest.com/scratchandroam/"},
      related=[("/guides/first-time-in-china/","first-time-in-china-13-things-before-you-fly","GUIDE 13","First time in China: 13 things to set up before you fly"),("/guides/china-arrival-card-alipay/","china-arrival-card-in-alipay-step-by-step","GUIDE 14","China arrival card in Alipay on your phone"),("/guides/china-travel-apps/","china-travel-apps-12-apps-to-set-up-before-china","GUIDE","Apps to download before you go to China")])

guide("taobao-for-foreigners","How to order on Taobao as a foreigner: step by step guide","How to order on Taobao as a foreigner, step by step",
      "How to order on Taobao without speaking Chinese: language and currency settings, searching in English, hotel delivery, the Chinese note, and paying with Alipay.",
      "how to order on taobao","",
      "<p>Taobao has almost everything, and the whole app is in Chinese. This guide walks through one real order on my own phone, from Ireland: what I could and could not change in Settings, how to search without Chinese, how to send a parcel to a hotel without losing it, and where to find your order afterwards.</p><p>Where something comes from my own account I say so. Where it comes from someone else's guide I say that too, and a few things I could not confirm are marked as such.</p>",
      TB_STEPS,
      [("Can I use Taobao in English?","It depends on your account's region. On my account, bought from Ireland, the only language was Chinese. Third-party guides say English is available for some regions such as Singapore, Malaysia, Hong Kong and Macau, but I found no official list, so open Settings in your own app and look."),
       ("How do I search on Taobao if I do not read Chinese?","Type your search in English. It worked for me with phone case. For anything you cannot read, use your phone's own translation: Live Text on an iPhone, or Circle to Search on Android."),
       ("Can I send a Taobao parcel to my hotel?","Yes, but ask the hotel first. Message them with your name, booking number and dates, ask if they accept parcels before you arrive, and ask for their address and reception phone in Chinese. Add a Chinese note asking them to leave it at reception and not to call the guest."),
       ("How long does Taobao delivery take?","It varies. Delivery to a hotel can take up to three days, so do not order for a stay of one to three days. Read the delivery estimate before you pay."),
       ("How do I pay on Taobao with a foreign card?","Through Alipay, with your own bank card linked in the Alipay app. Set it up before you travel. Third-party sources report a 3% fee on payments over ¥200.")],
      [("Phone settings: Live Text on iPhone (Apple Support)","https://support.apple.com/en-ie/HT212630",True),
       ("Circle to Search: translate (Google Search Help)","https://support.google.com/websearch/answer/14508957?hl=en",True),
       ("Alipay on the App Store","https://apps.apple.com/app/alipay/id333206289",True),
       ("Trip.com: how to change Taobao to English","https://www.trip.com/guide/info/how-to-change-taobao-to-english.html",False),
       ("Tianwen: Taobao in English","https://tianwenwangluo.com/en/taobao-in-english/",False),
       ("Trip.com: how to add a card to Alipay","https://www.trip.com/guide/payments/how-to-add-card-to-alipay.html",False),
       ("China for Travelers: Alipay for foreigners","https://chinafortravelers.com/guides/alipay-for-foreigners/",False)],
      SITE+"/og/taobao-for-foreigners.jpg",checked="2026-10-17",published="2026-10-17",vschema=False,
      lift='<div class="dd-hero"><img data-hero src="/img/how-to-order-on-taobao-step-by-step-guide-cover.jpg" alt=""></div>',
      steps_title="The 12 steps, in order",
      related=[("/guides/china-travel-apps/","china-travel-apps-12-apps-to-set-up-before-china","GUIDE","Apps to download before you go to China"),("/guides/first-time-in-china/","first-time-in-china-13-things-before-you-fly","GUIDE 13","First time in China: 13 things to set up before you fly"),("/guides/china-arrival-card-alipay/","china-arrival-card-in-alipay-step-by-step","GUIDE 14","China arrival card in Alipay on your phone")])


# ---------- Top 25 China apps, Boarding Pass style (SR-0027) ----------
exec(open('src/bp_apps.py').read())
_BP_FRAMES=[("alipay-pass-critical-gate-01","Pass 1: Alipay, critical"),("amap-pass-critical-gate-05","Pass 5: Amap, critical"),("taobao-pass-handy-gate-16","Pass 16: Taobao, handy"),("boarding-complete-checklist-of-25-apps","Boarding complete")]
def _bp_extra():
    shots="".join(f'<figure><img src="/img/top-25-china-apps-short-frame-{k}.jpg" alt="" width="540" height="960"><figcaption>{c}</figcaption></figure>' for k,c in _BP_FRAMES)
    return bp_board()+f'<h2>The same list as a Short</h2><p>I made this list as a vertical video in the same boarding pass style, one pass per app, counting down in order of importance. It is going up on YouTube Shorts, TikTok and Instagram. A few frames:</p><div class="bp-shots">{shots}</div>'
guide("top-25-china-apps","Top 25 China apps for tourists, ranked (2026)","Top 25 apps to have in China, ranked like a boarding pass",
      "The 25 apps worth having for a trip to China, ranked from critical to optional: what each does, how to set it up, what you lose without it. Checked October 2026.",
      "top 25 china apps",None,
      "<p>These are the top 25 China apps for a first trip, ranked in order of importance. Each one gets a boarding pass: what it is for, how to set it up, why it ranks where it does, and what happens if you land without it. The first five are critical, the last five are optional, and two of those come with a warning.</p><p>It is the written version of my Scratch &amp; Roam Short, in the same order. The pass rows are my words from the video; the fine print on each pass was checked on 18 October 2026 against the sources at the bottom. Where I could not confirm something, the pass says so. For the full setup of the first dozen apps, use my <a href=\"/guides/china-travel-apps/\">China travel apps guide</a>.</p>",
      [],
      [("What are the most important apps to have in China?","Alipay and WeChat for paying and messaging, a travel eSIM or VPN for Google and WhatsApp, and Amap for maps. These are the first four to five passes on this list, and all of them need to be set up at home."),
       ("Which China apps do I need to set up before I fly?","Alipay, WeChat, an eSIM or VPN, 12306, Trip.com and your translator packs. They need a passport check, a text code, or a download from a store that does not work in China, so do them at home."),
       ("Which apps on the list can I skip?","Waygo (not updated since 2017) and Kuli Kuli (a paywall) are the two with warnings. DeepL is optional and I could not confirm it works without a VPN in China. Ele.me is now called Taobao Flash Sale."),
       ("Do I need a VPN in China if I have an eSIM?","Usually not on mobile data, because travel eSIM plans for China say they route data outside China. A VPN still helps on hotel Wi-Fi, and it has to be installed and tested before you fly."),
       ("Which translator app is best for China?","Download the Chinese pack in Google Translate or Microsoft Translator at home, add Baidu Translate for signs and menus, and keep Pleco for single characters. Pick two and test them before you fly.")],
      BP_SOURCES,
      SITE+"/og/top-25-china-apps.jpg",
      related=[("/guides/china-travel-apps/","china-travel-apps-12-apps-to-set-up-before-china","12 apps","Apps to download before you go to China: the full list"),
               ("/guides/first-time-in-china/","first-time-in-china-13-things-before-you-fly","GUIDE 13","First time in China: 13 things to set up before you fly"),
               ("/guides/taobao-for-foreigners/","how-to-order-on-taobao-step-by-step-guide-cover","SHOPPING","How to order on Taobao as a foreigner, step by step")],
      checked="2026-10-18",published="2026-10-18",
      jsonld=[{"@context":"https://schema.org","@type":"ItemList","name":"Top 25 China apps, ranked","itemListOrder":"https://schema.org/ItemListOrderAscending","numberOfItems":25,"itemListElement":[{"@type":"ListItem","position":a[0],"name":a[1],"url":SITE+"/guides/top-25-china-apps/#app-"+str(a[0])} for a in BP]}],
      lift='<div class="bp-hero"><img data-hero src="/img/top-25-china-apps-boarding-pass-cover.jpg" alt="" width="1280" height="720"></div>',
      extra=_bp_extra())


# ---------- Alipay metro QR code (SR-0026) ----------
AM_FIGS={0:["alipay-home-screen-with-transport-icon-and-quick-tutorial-caption"],
 1:["alipay-select-city-list-with-chengdu-highlighted-for-metro-qr"],
 2:["alipay-transport-tab-tap-bus-and-metro-icon-for-xian"],
 3:["alipay-obtain-metro-card-agree-and-obtain-card-button-xian"],
 4:["alipay-payment-password-notice-for-claiming-metro-qr-card"],
 5:["alipay-metro-card-collected-successfully-use-now-button"],
 7:["alipay-wrong-qr-code-switch-city-top-left-notice"]}
AM_STEPS=[
 ("Set up Alipay at home first",
  "The metro QR code lives inside your Alipay account, so the account has to work first: identity check, a linked bank card and your payment password. The steps are in my <a href=\"/guides/china-travel-apps/\">China travel apps guide</a>. One third-party guide says the account needs a linked foreign card and identity verification before the transit feature works. I did not find an official Alipay page that lists the requirements for visitors, so follow what your own app asks for."),
 ("Open Alipay and tap Transport",
  "On the Alipay home screen, <b>Transport</b> is in the top row, next to Scan, Pay/Receive and Pocket. This is not the same thing as the payment code you show in a shop. A third-party guide warns that the shop payment QR does not open a metro gate, so it has to be the Transport code."),
 ("Pick the city you are going to",
  "My Alipay was set to Cork. I am going to Chengdu in a month and a half, so I opened the city list and tapped <b>Chengdu</b>. Each city has its own code: another guide says activating Beijing's does not cover Shanghai. Pick the city you are about to ride in, and repeat for each city you visit."),
 ("Tap Bus & Metro",
  "Back on the Transport tab, the Metro card was not showing yet, only Taxi and a map. After the city was set, the <b>BusMetro</b> icon appeared in the top row. Tap it. Parts of the page are in Chinese, so the floating <b>Translate</b> button is useful. If the translation seems stuck, be patient, it can take a moment."),
 ("Tap Agree and obtain card",
  "The next screen is called Obtain card to take Metro, and it names the metro provider for that city. The screen says <b>Free card</b>. The agreement is in Chinese. Read it with Translate before you tap the blue <b>Agree and obtain card</b> button. The official Alipay+ documentation says the fare is taken after your ride, from the payment method you have linked, on a ride first, pay later basis."),
 ("Enter your Alipay payment password",
  "Alipay asks for the payment password you set up for paying. This is the password screen that goes black when you record the screen, which is why my video shows a notice instead. Type it on your own phone, in private."),
 ("Card collected: tap Use now to open the QR code",
  "When it works you get <b>Card collected successfully</b> and a <b>Use now</b> button, and Use now takes you to your QR code. The same Bus & Metro card idea applies to buses and to any city you add; I also added another city the same way, and there is an option on the screen to activate all available transports. At the gate, hold the code over the reader. Two third-party guides say to turn the screen brightness up and hold it steady for a second or two. At a bus reader, scan before you go in."),
 ("If the QR code is for the wrong city, switch the city",
  "If the code does not match the city you are standing in, the gate will not open. Tap the <b>city name at the top left</b> of the Alipay home screen and choose the right one. A guide updated on 14 October 2026 calls a wrong city selection a common reason codes fail. If a gate still refuses you, step aside and buy a single-journey ticket at the machine, and keep a little cash for buses."),
]
AM_STEPS=[(a,b,AM_FIGS.get(i,[])) for i,(a,b) in enumerate(AM_STEPS)]
guide("alipay-metro-qr-code-china","Alipay metro QR code in China: how to add it","Alipay metro QR code in China: how to add it, step by step",
      "How to add the Alipay metro and bus QR code for China: pick the city, claim the free card, enter your payment password, and fix the wrong-city code.",
      "alipay metro qr code china",None,
      "<p>The Alipay metro QR code is the code you hold over the gate to ride the metro or bus in a Chinese city. This guide shows how I added it on my own phone, from Ireland: where Transport is, how to pick the city, how to claim the free card, and what to do when the QR code is for the wrong city.</p><p>The screenshots are frames from my own screen recording. The facts about how it is charged come from the official Alipay+ documentation and are marked official. Things I could not confirm are marked as such. Checked on 18 October 2026.</p>",
      AM_STEPS,
      [("How do I add the metro QR code in Alipay?","Open Alipay, tap Transport, pick your city, tap Bus & Metro, tap Agree and obtain card, then enter your Alipay payment password. When you see Card collected successfully, tap Use now to open the QR code."),
       ("Do I need a different QR code for each city?","Yes. One third-party guide says each city needs its own ride code and that activating Beijing's does not cover Shanghai. Pick the city, claim its card, and repeat when you move on."),
       ("Is the Alipay metro card free, and how do I pay?","The card screen I used said Free card. The official Alipay+ documentation describes a ride first, pay later model: the fare is deducted after you exit a station or leave a vehicle, from the payment method linked to your wallet. Fares themselves differ by city, so I give no price."),
       ("Why does the gate not open with my QR code?","The usual causes are the wrong city selected, or using the shop payment code instead of the Transport code. Switch the city at the top left of the Alipay home screen. If it still fails, buy a single-journey ticket at the machine. The Alipay+ documentation says the ticket machines in every mainland metro station accept Alipay."),
       ("Can I set it up before I fly?","It worked on my phone in Ireland for a city I have not reached yet. One third-party guide says some users abroad see an empty Transport tab and may need to activate on arrival, so test it at home and have a plan for when you land.")],
      [("Alipay+ Docs: Cross-border public transport, product introduction","https://docs.alipayplus.com/alipayplus/alipayplus/public_transport/product_introduction",True),
       ("Alipay+ Docs: Transport Code FAQs","https://docs.alipayplus.com/alipayplus/alipayplus/public_transport/transport_code_faqs",True),
       ("Chinavigators: How to use Alipay transit codes for China metros (updated 18 March 2026)","https://www.chinavigators.com/alipay-transit-code/",False),
       ("UnlockChina: How to pay for the metro in China as a foreigner (19 July 2026)","https://www.unlockchina.co/china-metro-payment/",False),
       ("LocalKey Travel: China metro for foreigners (updated 14 October 2026)","https://www.localkeytravel.com/china-guide/china-metro-for-foreigners",False)],
      SITE+"/og/alipay-metro-qr-code-china.jpg",checked="2026-10-18",published="2026-10-18",vschema=False,
      lift='<div class="dd-hero"><img data-hero src="/img/alipay-metro-qr-code-china-cover-16x9.jpg" alt="" width="1280" height="720"></div>',
      steps_title="The 8 steps, in order",
      shotnote="Frames from my own screen recording of Alipay. Tap a picture to open it larger.",
      related=[("/guides/china-travel-apps/","china-travel-apps-12-apps-to-set-up-before-china","GUIDE","Apps to download before you go to China"),("/guides/first-time-in-china/","first-time-in-china-13-things-before-you-fly","GUIDE 13","First time in China: 13 things to set up before you fly"),("/guides/top-25-china-apps/","top-25-china-apps-boarding-pass-cover","TOP 25","Top 25 China apps for tourists, ranked like a boarding pass")])
