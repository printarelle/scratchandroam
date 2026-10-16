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
      <a class="q" href="/guides/first-time-in-china/"><span class="k">Paying</span><b>How do I pay when nobody takes cash or cards?</b><span class="go">Alipay and WeChat, in the checklist</span></a>
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
CHINA = '''<main class="wrap guide">
<p class="eyebrow">China</p>
<h1>China guides for first-timers</h1>
<p class="lede">The practical part first: entry, payments, trains. The city pages (Shanghai now, Chengdu, Chongqing and Xi'an after December) come next.</p>
<section class="sec" style="padding-top:30px"><h2 style="margin-bottom:16px">Before you fly</h2><div class="tickets">
<a class="tk" href="/guides/first-time-in-china/"><img src="/img/first-time-16x9.jpg" alt="13 things before China guide cover" loading="lazy"><span class="num">GUIDE 13</span><div class="cb"><div class="meta"><span>CHECKLIST</span></div><h3>First time in China: 13 things to set up before you fly</h3><span class="go">Read the guide</span></div></a>
<a class="tk" href="/guides/china-arrival-card-pc/"><img src="/img/arrival-pc-16x9.jpg" alt="China arrival card on a PC guide cover" loading="lazy"><span class="num">GUIDE 14</span><div class="cb"><div class="meta"><span>STEP BY STEP</span></div><h3>China arrival card online on a computer</h3><span class="go">Read the guide</span></div></a>
<a class="tk" href="/guides/china-arrival-card-alipay/"><img src="/img/arrival-alipay-16x9.jpg" alt="China arrival card in Alipay guide cover" loading="lazy"><span class="num">GUIDE 14</span><div class="cb"><div class="meta"><span>STEP BY STEP</span></div><h3>China arrival card in Alipay on your phone</h3><span class="go">Read the guide</span></div></a>
</div></section>
<section class="sec"><h2 style="margin-bottom:14px">Shanghai, mostly at night</h2><div class="wall" style="margin-bottom:20px"><a class="tile t-wide" href="/guides/the-bund-shanghai-at-night/"><img src="/img/bund-4x5.jpg" alt="The Bund at night" loading="lazy"><span class="cap"><small>Guide</small>The Bund at night: how to get there</span></a><a class="tile" href="/guides/nanjing-road-shanghai/"><img src="/img/nanjing-4x5.jpg" alt="Nanjing Road" loading="lazy"><span class="cap"><small>Guide</small>Nanjing Road</span></a><a class="tile" href="/guides/huangpu-river-night-cruise/"><img src="/img/river-4x5.jpg" alt="Huangpu river skyline" loading="lazy"><span class="cap"><small>Guide</small>River cruise</span></a><a class="tile t-wide" href="/guides/shanghai-circus-world-era-show/"><img src="/img/circus-16x9.jpg" alt="Shanghai Circus World" loading="lazy"><span class="cap"><small>Guide</small>ERA show: tickets and how to get there</span></a></div><p class="intro">The videos and photo sets behind these pages are on <a href="https://www.youtube.com/@scratchandroam" rel="noopener">YouTube</a>, <a href="https://www.instagram.com/scratchandroam/" rel="noopener">Instagram</a> and <a href="https://www.tiktok.com/@scratchandroam" rel="noopener">TikTok</a>. Shanghai Disneyland after dark is next.</p></section>
</main>'''
page("/china/","China guides for first-timers: entry, payments, trains",
     "Practical China guides from Scratch & Roam: the arrival card, Alipay and WeChat setup, visa-free rules, trains and getting around, each with a video and written steps.",
     CHINA,[{"@context":"https://schema.org","@type":"CollectionPage","name":"China guides for first-timers","url":SITE+"/china/"}])

ABOUT = '''<main class="wrap guide" style="max-width:800px">
<p class="eyebrow">About</p>
<h1>Scratch &amp; Roam with Natali</h1>
<div class="polaroid" style="float:right;margin:0 0 20px 24px;max-width:280px"><div class="img"><img src="/img/natali.jpg" alt="Natali in her studio"></div><div class="cap">hello from the studio</div></div>
<div class="intro" style="margin-top:20px">
<p>I am Natali, a maker from Ireland. I make things for a living and film the trips in between: China, Japan and wherever comes next. My husband and family turn up in the videos sometimes, and so does the work on the days I am not travelling.</p>
<p>The scratch card is the idea behind the name. A place stays hidden until you scratch it, and then it is all there. Every video opens that way, and the guides on this site are the parts I wish someone had written down for me before my first trip.</p>
<p>How the guides are made: I film the real screens and the real streets, check every rule against the official page on the day, and write the date on the guide. When a rule changes, the guide gets updated, not left to go stale.</p>
</div>
<div class="sidebox"><h3>Say hello</h3><p>scratchandroam@gmail.com</p><p>Handle everywhere: @scratchandroam</p></div>
</main>'''
page("/about/","About Scratch & Roam with Natali","Natali is a maker from Ireland who films her trips and writes first-timer travel guides. Scratch to reveal. Roam to discover.",ABOUT,
     [{"@context":"https://schema.org","@type":"AboutPage","name":"About Scratch & Roam with Natali","url":SITE+"/about/","mainEntity":{"@type":"Person","name":"Natali","sameAs":json.loads(SAMEAS)}}])

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
      "first time in China",None,
      "<p>This is the checklist we wish we had before the first trip: not sights, just the setup. Everything on it was checked on 15 October 2026 against the sources at the bottom, and the video walks through the same 13 things.</p>",
      FT_STEPS,
      [("Do I need a visa for China?","It depends on your passport. In October 2026 China listed 50 countries with visa-free entry for short stays, most of it dated to 31 December 2026. Check the official list for your own country before booking."),
       ("Which app do I need, Alipay or WeChat?","Both work for paying. Set both up at home, link a card to each, and you will not be stuck when one of them does not like your card."),
       ("Does Google Maps work in China?","No. Use Amap or Apple Maps, and keep the Chinese names of your hotel and stations saved offline."),
       ("When should I book high-speed trains?","Tickets go on sale about 15 days before the travel date. Book as soon as they open for busy routes.")],
      [("Shanghai municipal government (English): visa-free entry policy","https://english.shanghai.gov.cn/en-Individuals-ImmigrationandVisas-Visa-freepolicies/20260709/469e8c5656534926a04b31a1084351f0.html",True),
       ("National Immigration Administration: arrival card filling page",NIA,True),
       ("China Railway 12306","https://www.12306.cn/en/",True)],
      SITE+"/og/first-time.jpg",
      chapters=[("1","Entry rules"),("2","Arrival card"),("3","Get the apps"),("4","Pay setup"),("5","Mini-programs"),("6","The ¥200 fee"),("7","Cash"),("8","Flights"),("9","Booking"),("10","Trains"),("11","Station day"),("12","Maps"),("13","Pack light")],
      related=[("/guides/china-arrival-card-pc/","arrival-pc-16x9","GUIDE 14","China arrival card online on a computer"),("/guides/china-arrival-card-alipay/","arrival-alipay-16x9","GUIDE 14","China arrival card in Alipay on your phone")])

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
