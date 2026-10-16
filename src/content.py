# Pages for scratchandroam.com. Facts only from Natali's own guides and the sources listed on each page.

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
    <a class="vid" href="/guides/first-time-in-china/"><img src="/img/first-time-16x9.jpg" alt="Cover of the First time in China video, 13 things to set up before you fly" fetchpriority="high"><span class="tag">Newest video</span><span class="play" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></span><span class="cap">First time in China: 13 things to set up before you fly<small>6 MIN · VIDEO + CHECKLIST</small></span></a>
  </div>
  <div class="pick">
    <p class="hand">Pick the thing you need to sort out:</p>
    <div class="qs">
      <a class="q" href="/guides/china-arrival-card-pc/"><span class="k">Arrival card · PC</span><b>How do I fill the China arrival card online?</b><span class="go">3 min video + steps</span></a>
      <a class="q" href="/guides/china-arrival-card-alipay/"><span class="k">Arrival card · Phone</span><b>Can I do the arrival card in Alipay on the way?</b><span class="go">3 min video + steps</span></a>
      <a class="q" href="/guides/first-time-in-china/"><span class="k">Visa-free</span><b>Do I need a visa, and for how many days?</b><span class="go">In the checklist guide</span></a>
      <a class="q" href="/guides/china-travel-apps/"><span class="k">Paying · Maps · Trains</span><b>Which apps do I need, and which can I skip?</b><span class="go">12 apps + hidden gems</span></a>
      <a class="q" href="/guides/first-time-in-china/"><span class="k">Before you fly</span><b>What do I need to set up before I land?</b><span class="go">13-point checklist, 6 min</span></a>
      <a class="q next" href="https://www.youtube.com/@scratchandroam?sub_confirmation=1" rel="noopener"><span class="k">Coming next</span><b>Trains, metro cards and the Chengdu to Xi'an route</b><span class="go">Subscribe to catch the December guides</span></a>
    </div>
  </div>
</div></section>
<div class="strip" aria-hidden="true"><span>Scratch to reveal · Roam to discover · Shanghai · Chengdu · Chongqing · Xi'an · Arrival card · Alipay · Visa-free · Scratch to reveal · Roam to discover · Shanghai · Chengdu · Chongqing · Xi'an · Arrival card · Alipay · Visa-free · </span></div>

<section class="sec" id="december"><div class="wrap cardsec">
  <div class="cardwrap">
    <div class="scard">
      <div class="head"><span class="mk">Scratch <em>&amp;</em> Roam</span><span class="no">Card no. 001 · Shanghai</span></div>
      <div class="win" id="cwin"><img src="/img/bund-3x4.jpg" alt="The Bund in Shanghai at night" loading="lazy"><canvas id="foil" aria-label="Scratch the silver foil to reveal Shanghai"></canvas><span class="done">Shanghai, scratched off</span></div>
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
    <a class="tk" href="/guides/china-arrival-card-pc/"><img src="/img/arrival-pc-16x9.jpg" alt="Cover of the China arrival card guide for PC, number 14 with a passport and an entry stamp" loading="lazy"><span class="num">GUIDE 14</span><div class="cb"><div class="meta"><span>VIDEO + STEPS</span><span>3 MIN</span></div><h3>China arrival card online, step by step on a computer</h3><p>Upload your passport, let it fill the form, save the QR. Every screen shown.</p><span class="go">Read the guide</span></div></a>
    <a class="tk" href="/guides/china-arrival-card-alipay/"><img src="/img/arrival-alipay-16x9.jpg" alt="Cover of the China arrival card guide for Alipay on a phone" loading="lazy"><span class="num">GUIDE 14</span><div class="cb"><div class="meta"><span>VIDEO + STEPS</span><span>3 MIN</span></div><h3>China arrival card in Alipay on your phone</h3><p>The same card through the Alipay mini program, for people who do it on the way.</p><span class="go">Read the guide</span></div></a>
    <a class="tk" href="/guides/first-time-in-china/"><img src="/img/first-time-16x9.jpg" alt="Cover of the 13 things before China guide, with the 200 yuan fee card" loading="lazy"><span class="num">GUIDE 13</span><div class="cb"><div class="meta"><span>VIDEO + CHECKLIST</span><span>6 MIN</span></div><h3>First time in China: 13 things to set up before you fly</h3><p>Visa-free list, arrival card, Alipay and WeChat, cards, cash, trains, maps, packing.</p><span class="go">Read the guide</span></div></a>
    <a class="tk" href="/guides/china-travel-apps/"><img src="/img/apps-16x9.jpg" alt="Cover of the China travel apps guide, 12 apps to set up before China with a Nanjing Road night photo and the China flag" loading="lazy"><span class="num">APPS LIST</span><div class="cb"><div class="meta"><span>LIST + VIDEO</span><span>12 APPS</span></div><h3>Apps to download before you go to China: the full list</h3><p>Paying, maps, taxis, trains, what to set up at home, the hidden gems inside Alipay, and what to skip.</p><span class="go">Read the guide</span></div></a>
  </div>
</div></section>

<section class="sec" id="shanghai"><div class="wrap">
  <div class="sechead"><div><p class="eyebrow">Shanghai, answered</p><h2>What we filmed, turned into the practical answers</h2></div><a class="btn" href="https://www.youtube.com/@scratchandroam" rel="noopener">All videos</a></div>
  <div class="rows">
    <a class="row" href="/guides/the-bund-shanghai-at-night/"><img src="/img/bund-4x5.jpg" alt="The Bund in Shanghai at night" loading="lazy"><span><span class="k">The Bund</span><b>How do I get to the Bund at night, and when do the lights go off?</b><span class="go">Guide</span></span></a>
    <a class="row" href="/guides/nanjing-road-shanghai/"><img src="/img/nanjing-4x5.jpg" alt="Nanjing Road neon shop fronts" loading="lazy"><span><span class="k">Nanjing Road</span><b>When is the neon on, and where does the walking street start?</b><span class="go">Guide</span></span></a>
    <a class="row" href="/guides/huangpu-river-night-cruise/"><img src="/img/river-4x5.jpg" alt="Shanghai skyline from the Huangpu river at night" loading="lazy"><span><span class="k">River cruise</span><b>Which pier, which ticket, and is the night cruise worth it?</b><span class="go">Guide</span></span></a>
    <a class="row" href="/guides/shanghai-circus-world-era-show/"><img src="/img/circus-16x9.jpg" alt="Shanghai Circus World stage with aerial silks" loading="lazy"><span><span class="k">ERA show</span><b>Where do I book ERA circus tickets and how do I get there?</b><span class="go">Guide</span></span></a>
    <a class="row" href="https://www.youtube.com/@scratchandroam" rel="noopener"><img src="/img/film-4x5.jpg" alt="Shanghai at night as one roll of film" loading="lazy"><span><span class="k">Photo set</span><b>Shanghai at night as one roll of film</b><span class="go">Photos</span></span></a>
    <a class="row" href="https://www.youtube.com/@scratchandroam" rel="noopener"><img src="/img/circus-photo-16x9.jpg" alt="Shanghai Circus photo dump cover" loading="lazy"><span><span class="k">Photo set</span><b>Circus photo dump</b><span class="go">Photos</span></span></a>
  </div>
</div></section>

<section class="sec alt"><div class="wrap about">
  <div class="polaroid"><div class="img"><img src="/img/natali.jpg" alt="Natali in her studio, smiling at the camera" loading="lazy"></div><div class="cap">Natali, somewhere with a camera</div></div>
  <div><p class="eyebrow">About</p><h2>A maker from Ireland who travels with a camera and a lot of curiosity</h2><p>I make things for a living and film the trips in between. These pages are the parts I wish someone had written down for me.</p><p style="margin-top:16px"><a href="/about/">More about Scratch &amp; Roam</a></p></div>
</div></section>
</main>
''' + SCRATCH_JS

page("/","Scratch & Roam with Natali: China first-timer guides and travel videos",
     "Travel guides and videos from Natali, a maker from Ireland. First-timer China guides: arrival card, Alipay, visa-free rules. Scratch to reveal. Roam to discover.",
     HOME,
     [{"@context":"https://schema.org","@type":"WebSite","name":"Scratch & Roam with Natali","url":SITE,"inLanguage":"en","publisher":{"@type":"Person","name":"Natali","url":SITE+"/about/","sameAs":json.loads(SAMEAS)}},
      {"@context":"https://schema.org","@type":"Person","name":"Natali","url":SITE+"/about/","jobTitle":"Travel creator and maker","homeLocation":{"@type":"Place","name":"Ireland"},"sameAs":json.loads(SAMEAS)}],
     og_image=SITE+"/og/circus-photo.jpg", dark=True)

# China index
CHINA = '''<main>
<section class="chero"><div class="wrap">
<p class="eyebrow" style="color:#C0DACE"><a href="/" style="color:inherit">Home</a> · China</p>
<h1>China guides for first-timers: <span>entry, paying, trains.</span></h1>
<p class="lede">The practical part first, in the order you will need it: before you fly, at the border, then paying and getting around. Shanghai is filmed and written up; Chengdu, Chongqing and Xi'an land after December.</p>
<div class="pick">
  <p class="hand" style="color:#FFD27A;transform:none">Pick the thing you need to sort out:</p>
  <div class="qs">
    <a class="q" href="/guides/first-time-in-china/"><span class="k">Before you fly</span><b>What do I need to set up before I land?</b><span class="go">13-point checklist, 6 min</span></a>
    <a class="q" href="/guides/first-time-in-china/"><span class="k">Visa-free</span><b>Do I need a visa, and for how many days?</b><span class="go">In the checklist guide</span></a>
    <a class="q" href="/guides/china-arrival-card-pc/"><span class="k">Arrival card · PC</span><b>How do I fill the China arrival card online?</b><span class="go">3 min video + steps</span></a>
    <a class="q" href="/guides/china-arrival-card-alipay/"><span class="k">Arrival card · Phone</span><b>Can I do the arrival card in Alipay on the way?</b><span class="go">3 min video + steps</span></a>
      <a class="q" href="/guides/china-travel-apps/"><span class="k">Paying · Maps · Trains</span><b>Which apps do I need, and which can I skip?</b><span class="go">12 apps + hidden gems</span></a>
    <a class="q next" href="https://www.youtube.com/@scratchandroam?sub_confirmation=1" rel="noopener"><span class="k">Coming next</span><b>Trains, metro cards and the Chengdu to Xi'an route</b><span class="go">Subscribe to catch the December guides</span></a>
  </div>
</div>
</div></section>

<section class="sec" id="before"><div class="wrap">
  <div class="sechead"><div><p class="eyebrow">Before you fly</p><h2>The setup guides</h2><p>Each one is the video plus the written steps, checked against the official page on the date shown.</p></div><span class="pill">Rules change, so every guide is dated</span></div>
  <div class="tickets">
    <a class="tk" href="/guides/first-time-in-china/"><img src="/img/first-time-16x9.jpg" alt="13 things before China guide cover" loading="lazy"><span class="num">GUIDE 13</span><div class="cb"><div class="meta"><span>VIDEO + CHECKLIST</span><span>6 MIN</span></div><h3>First time in China: 13 things to set up before you fly</h3><p>Visa-free list, arrival card, Alipay and WeChat, cards, cash, trains, maps, packing.</p><span class="go">Read the guide</span></div></a>
    <a class="tk" href="/guides/china-travel-apps/"><img src="/img/apps-16x9.jpg" alt="Cover of the China travel apps guide, 12 apps to set up before China with a Nanjing Road night photo and the China flag" loading="lazy"><span class="num">APPS LIST</span><div class="cb"><div class="meta"><span>LIST + VIDEO</span><span>12 APPS</span></div><h3>Apps to download before you go to China: the full list</h3><p>Paying, maps, taxis, trains, what to set up at home, the hidden gems inside Alipay, and what to skip.</p><span class="go">Read the guide</span></div></a>
    <a class="tk" href="/guides/china-arrival-card-pc/"><img src="/img/arrival-pc-16x9.jpg" alt="China arrival card on a PC guide cover" loading="lazy"><span class="num">GUIDE 14</span><div class="cb"><div class="meta"><span>VIDEO + STEPS</span><span>3 MIN</span></div><h3>China arrival card online on a computer</h3><p>Upload your passport, let it fill the form, save the QR. Every screen shown.</p><span class="go">Read the guide</span></div></a>
    <a class="tk" href="/guides/china-arrival-card-alipay/"><img src="/img/arrival-alipay-16x9.jpg" alt="China arrival card in Alipay guide cover" loading="lazy"><span class="num">GUIDE 14</span><div class="cb"><div class="meta"><span>VIDEO + STEPS</span><span>3 MIN</span></div><h3>China arrival card in Alipay on your phone</h3><p>The same card through the Alipay mini program, for people who do it on the way.</p><span class="go">Read the guide</span></div></a>
  </div>
</div></section>

<section class="sec alt" id="shanghai"><div class="wrap">
  <div class="sechead"><div><p class="eyebrow">Shanghai, answered</p><h2>What we filmed, turned into the practical answers</h2><p>Four place guides from the trip, mostly at night: how to get there, when to go, what it costs.</p></div><a class="btn" href="https://www.youtube.com/@scratchandroam" rel="noopener">All videos</a></div>
  <div class="rows">
    <a class="row" href="/guides/the-bund-shanghai-at-night/"><img src="/img/bund-4x5.jpg" alt="The Bund in Shanghai at night" loading="lazy"><span><span class="k">The Bund</span><b>How do I get to the Bund at night, and when do the lights go off?</b><span class="go">Guide</span></span></a>
    <a class="row" href="/guides/nanjing-road-shanghai/"><img src="/img/nanjing-4x5.jpg" alt="Nanjing Road neon shop fronts" loading="lazy"><span><span class="k">Nanjing Road</span><b>When is the neon on, and where does the walking street start?</b><span class="go">Guide</span></span></a>
    <a class="row" href="/guides/huangpu-river-night-cruise/"><img src="/img/river-4x5.jpg" alt="Shanghai skyline from the Huangpu river at night" loading="lazy"><span><span class="k">River cruise</span><b>Which pier, which ticket, and is the night cruise worth it?</b><span class="go">Guide</span></span></a>
    <a class="row" href="/guides/shanghai-circus-world-era-show/"><img src="/img/circus-16x9.jpg" alt="Shanghai Circus World stage with aerial silks" loading="lazy"><span><span class="k">ERA show</span><b>Where do I book ERA circus tickets and how do I get there?</b><span class="go">Guide</span></span></a>
  </div>
  <p class="intro" style="margin-top:26px;margin-bottom:0">The videos and photo sets behind these pages are on <a href="https://www.youtube.com/@scratchandroam" rel="noopener">YouTube</a>, <a href="https://www.instagram.com/scratchandroam/" rel="noopener">Instagram</a> and <a href="https://www.tiktok.com/@scratchandroam" rel="noopener">TikTok</a>. Shanghai Disneyland after dark is next.</p>
</div></section>

<section class="sec" id="december"><div class="wrap">
  <div class="sechead"><div><p class="eyebrow">Still under the foil</p><h2>December: Chengdu, Chongqing, Xi'an</h2><p>Pandas, hotpot, a metro that runs through a building, and the Terracotta Army. The guides from this trip land here first, then the videos.</p></div></div>
  <div class="cities" style="grid-template-columns:repeat(3,minmax(0,1fr));max-width:720px;margin-top:0">
    <div class="city"><b>Chengdu</b><span class="k">December</span><span class="hand">pandas, hotpot</span></div>
    <div class="city"><b>Chongqing</b><span class="k">December</span><span class="hand">metro through a building</span></div>
    <div class="city"><b>Xi'an</b><span class="k">December</span><span class="hand">Terracotta Army</span></div>
  </div>
  <div class="stops" style="margin-top:18px;font-size:12px"><span class="stop home">CORK</span><span class="dash">- -</span><span class="stop">LONDON</span><span class="dash">- -</span><span class="stop">CHENGDU</span><span class="dash">- -</span><span class="stop">CHONGQING</span><span class="dash">- -</span><span class="stop">XI'AN</span></div>
</div></section>
</main>'''
page("/china/","China guides for first-timers: entry, payments, trains",
     "Practical China guides from Scratch & Roam: the arrival card, Alipay and WeChat setup, visa-free rules, trains and getting around, each with a video and written steps.",
     CHINA,[{"@context":"https://schema.org","@type":"CollectionPage","name":"China guides for first-timers","url":SITE+"/china/"}],
     og_image=SITE+"/og/first-time.jpg", dark=True)

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
    <div class="ph p1"><img src="/img/bund-s3.jpg" alt=""><div class="cap">the Bund, late</div></div>
    <div class="ph p2"><img src="/img/circus-b-4x5.jpg" alt=""><div class="cap">Shanghai Circus World</div></div>
    <div class="ph p3"><img src="/img/natali.jpg" alt=""><div class="cap">me, in the studio</div></div>
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
  <div class="pic"><img src="/img/nanjing-s2.jpg" alt="Nanjing Road in Shanghai at night" loading="lazy"><div class="sm"><img src="/img/river-s2.jpg" alt="Pudong towers from the Huangpu river" loading="lazy"><img src="/img/bund-s5.jpg" alt="Pudong skyline from the Bund" loading="lazy"></div></div>
  <div>
    <p class="eyebrow">The person</p>
    <h2>Making things by day, filming by night</h2>
    <p>I have a background in graphic design and I run a small studio in Ireland. Travel is the thing I do with the time in between, and the camera comes along because I want to remember the practical bits as much as the views: which exit, which pier, what it cost.</p>
    <p>My husband and family turn up in the videos sometimes, and so does the work on the days I am not travelling. Nothing here is sponsored. If a rule or a price is on a page, I checked it on the date written next to it.</p>
  </div>
</div></section>

<section class="sec"><div class="wrap story flip">
  <div class="pic"><div class="scard" style="max-width:380px;margin:0 auto"><div class="head"><span class="mk">Scratch <em>&amp;</em> Roam</span><span class="no">Card no. 001 · Shanghai</span></div><div class="win open" style="background:#1F1C28"><img src="/img/bund-3x4.jpg" alt="The Bund in Shanghai at night" loading="lazy"><span class="done" style="opacity:1">Shanghai, scratched off</span></div><div class="foot"><span class="hand">Scratch to reveal. Roam to discover.</span></div></div></div>
  <div>
    <p class="eyebrow">The idea</p>
    <h2>Why a scratch card?</h2>
    <p>A place stays hidden until you scratch it, and then it is all there. Every video opens that way: the name of the place under silver foil, a coin, and then the real thing. On the site a city gets scratched off once we have actually been, so the foil over Chengdu, Chongqing and Xi'an comes off in December.</p>
    <p>It is also a reminder of how I like to travel: not knowing everything in advance, but having the practical parts sorted so the rest can be a surprise.</p>
  </div>
</div></section>

<section class="sec alt"><div class="wrap story">
  <div class="pic wide"><img src="/img/arrival-pc-16x9.jpg" alt="Cover of the China arrival card guide" loading="lazy"><div class="sm"><img src="/img/first-time-16x9.jpg" alt="Cover of the first time in China checklist" loading="lazy"><img src="/img/arrival-alipay-16x9.jpg" alt="Cover of the Alipay arrival card guide" loading="lazy"></div></div>
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
     og_image=SITE+"/og/circus-photo.jpg", dark=True)

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
      SITE+"/og/arrival-pc.jpg",
      chapters=[("0:00","Intro: the arrival card on a PC"),("0:15","What the arrival card is"),("0:44","Get ready"),("1:04","Open the website"),("1:20","Passport page: the form fills itself"),("1:43","Basic information"),("2:04","Personal information"),("2:28","Travel information"),("2:51","Sign and confirm"),("3:01","Save your QR code"),("3:29","Your move")],
      related=[("/guides/china-arrival-card-alipay/","arrival-alipay-16x9","GUIDE 14","China arrival card in Alipay on your phone"),("/guides/first-time-in-china/","first-time-16x9","GUIDE 13","First time in China: 13 things to set up before you fly")],
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
      SITE+"/og/arrival-alipay.jpg",
      chapters=[("0:00","Intro: the arrival card in Alipay"),("0:13","What the arrival card is"),("0:42","Get ready"),("1:03","Find the mini program in Alipay"),("1:21","Agree and passport page"),("1:42","Basic information"),("1:59","Personal information"),("2:15","Travel information"),("2:32","Sign and confirm"),("2:42","Save your QR code"),("3:10","Your move")],
      related=[("/guides/china-arrival-card-pc/","arrival-pc-16x9","GUIDE 14","China arrival card online on a computer"),("/guides/first-time-in-china/","first-time-16x9","GUIDE 13","First time in China: 13 things to set up before you fly")],
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
      SITE+"/og/first-time.jpg",minutes="PT5M45S",upload="2026-10-16",
      chapters=[("1","Entry rules"),("2","Arrival card"),("3","Get the apps"),("4","Pay setup"),("5","Mini-programs"),("6","The ¥200 fee"),("7","Cash"),("8","Flights"),("9","Booking"),("10","Trains"),("11","Station day"),("12","Maps"),("13","Pack light")],
      related=[("/guides/china-arrival-card-pc/","arrival-pc-16x9","GUIDE 14","China arrival card online on a computer"),("/guides/china-arrival-card-alipay/","arrival-alipay-16x9","GUIDE 14","China arrival card in Alipay on your phone")])

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
      related=[("/guides/first-time-in-china/","first-time-16x9","GUIDE 13","First time in China: 13 things to set up before you fly"),("/guides/china-arrival-card-alipay/","arrival-alipay-16x9","GUIDE 14","China arrival card in Alipay on your phone")],
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
      SITE+"/og/bund.jpg",
      related=[("/guides/nanjing-road-shanghai/","nanjing-4x5","SHANGHAI","Nanjing Road: how to walk it and when the neon is on"),("/guides/huangpu-river-night-cruise/","river-4x5","SHANGHAI","Huangpu River night cruise: which pier and which ticket")],
      gallery=[("bund-4x5","The Bund after dark, gold lit bank buildings"),("bund-s2","Bund buildings lit at night"),("bund-s3","The Bund promenade at night"),("bund-s4","Bund facade detail at night"),("bund-s5","Pudong skyline from the Bund")],
      place={"name":"The Bund","city":"Shanghai","free":True},steps_title="How to do the Bund in one evening",
      shorts={"Instagram":"https://www.instagram.com/scratchandroam/","TikTok":"https://www.tiktok.com/@scratchandroam","Pinterest":"https://www.pinterest.com/scratchandroam/"})

guide("nanjing-road-shanghai","Nanjing Road Shanghai: how to get there, what to see, when the neon is on","Nanjing Road in Shanghai: how to walk it, which metro exit, when the neon comes on",
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
      SITE+"/og/nanjing.jpg",
      related=[("/guides/the-bund-shanghai-at-night/","bund-4x5","SHANGHAI","The Bund at night: how to get there and when to go"),("/guides/huangpu-river-night-cruise/","river-4x5","SHANGHAI","Huangpu River night cruise: which pier and which ticket")],
      gallery=[("nanjing-4x5","Nanjing Road neon shop fronts"),("nanjing-s2","Nanjing Road at night"),("nanjing-s3","Shops on Nanjing Road"),("nanjing-s4","Nanjing Road crowd and lights"),("nanjing-s5","Nanjing Road by day")],
      place={"name":"Nanjing Road Pedestrian Street","city":"Shanghai","free":True},steps_title="How to walk Nanjing Road",
      shorts={"Instagram":"https://www.instagram.com/scratchandroam/","TikTok":"https://www.tiktok.com/@scratchandroam","Pinterest":"https://www.pinterest.com/scratchandroam/"})

guide("huangpu-river-night-cruise","Huangpu River night cruise Shanghai: which pier, ticket and time","Huangpu River night cruise in Shanghai: which pier, which ticket, and which side to stand on",
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
      SITE+"/og/river.jpg",
      related=[("/guides/the-bund-shanghai-at-night/","bund-4x5","SHANGHAI","The Bund at night: how to get there and when to go"),("/guides/shanghai-circus-world-era-show/","circus-4x5","SHANGHAI","Shanghai Circus World ERA show: tickets and how to get there")],
      gallery=[("river-4x5","Shanghai skyline from the Huangpu river at night"),("river-s2","Pudong towers from the water"),("river-s3","Bund buildings from the cruise"),("river-s4","Lujiazui lit up from the river"),("river-s5","The Oriental Pearl tower from the water")],
      place={"name":"Huangpu River Cruise","city":"Shanghai","free":False},steps_title="How to book and board",
      shorts={"Instagram":"https://www.instagram.com/scratchandroam/","TikTok":"https://www.tiktok.com/@scratchandroam","Pinterest":"https://www.pinterest.com/scratchandroam/"})

guide("shanghai-circus-world-era-show","Shanghai Circus World ERA show: tickets, seats and how to get there","Shanghai Circus World ERA show: how to book tickets, where to sit, how to get there",
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
      SITE+"/og/circus.jpg",
      related=[("/guides/huangpu-river-night-cruise/","river-4x5","SHANGHAI","Huangpu River night cruise: which pier and which ticket"),("/guides/the-bund-shanghai-at-night/","bund-4x5","SHANGHAI","The Bund at night: how to get there and when to go")],
      gallery=[("circus-4x5","Aerial silks act at Shanghai Circus World"),("circus-b-4x5","Hand balance act"),("circus-c-4x5","Laser light act"),("circus-d-4x5","Act four at Shanghai Circus World"),("circus-e-4x5","Act five at Shanghai Circus World")],
      place={"name":"Shanghai Circus World","city":"Shanghai","free":False},steps_title="How to book and get there",
      shorts={"YouTube":"https://www.youtube.com/@scratchandroam","Instagram":"https://www.instagram.com/scratchandroam/","TikTok":"https://www.tiktok.com/@scratchandroam"})
