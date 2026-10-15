# Pages for scratchandroam.com. Facts only from Natali's own guides and the sources listed on each page.

SCRATCH_JS = '''<script>
(function(){var box=document.getElementById('scratch'),c=document.getElementById('foil');if(!box||!c)return;
var ctx=c.getContext('2d'),down=false,cleared=false,px=0;
function size(){var r=box.getBoundingClientRect();c.width=Math.max(1,Math.round(r.width));c.height=Math.max(1,Math.round(r.height));paint();}
function paint(){var g=ctx.createLinearGradient(0,0,c.width,c.height);g.addColorStop(0,'#d6d9de');g.addColorStop(.5,'#b7bcc3');g.addColorStop(1,'#e2e5e9');ctx.globalCompositeOperation='source-over';ctx.fillStyle=g;ctx.fillRect(0,0,c.width,c.height);ctx.fillStyle='rgba(255,255,255,.35)';for(var i=0;i<60;i++){ctx.fillRect(Math.random()*c.width,Math.random()*c.height,2,2);}ctx.fillStyle='#1E1B1F';ctx.font='700 '+Math.round(c.height*.11)+'px "Special Elite", monospace';ctx.textAlign='center';ctx.fillText('SCRATCH TO REVEAL',c.width/2,c.height/2+6);}
function pos(e){var r=c.getBoundingClientRect();var t=e.touches?e.touches[0]:e;return{x:t.clientX-r.left,y:t.clientY-r.top};}
function scratch(e){if(!down||cleared)return;var p=pos(e);ctx.globalCompositeOperation='destination-out';ctx.beginPath();ctx.arc(p.x,p.y,Math.max(18,c.width*.05),0,Math.PI*2);ctx.fill();px++;if(px>70){cleared=true;c.style.transition='opacity .6s';c.style.opacity='0';var h=box.querySelector('.hint');if(h)h.textContent='';}e.preventDefault();}
c.addEventListener('mousedown',function(e){down=true;scratch(e);});c.addEventListener('touchstart',function(e){down=true;scratch(e);},{passive:false});
c.addEventListener('mousemove',scratch);c.addEventListener('touchmove',scratch,{passive:false});
window.addEventListener('mouseup',function(){down=false;});window.addEventListener('touchend',function(){down=false;});window.addEventListener('resize',size);
if(document.fonts&&document.fonts.ready){document.fonts.ready.then(size);}size();})();
</script>'''

HOME = f'''<main>
<section class="hero wrap" id="top">
  <div>
    <p class="eyebrow">Travel guides and videos from Ireland</p>
    <h1 style="margin-top:10px">First time in China? <span>Scratch here first.</span></h1>
    <p class="lede">Step by step guides for the things nobody explains before you fly: the arrival card, Alipay, visa-free rules, trains and metros. Filmed on the trip, written down so you can follow along at the airport.</p>
    <div class="cta"><a class="btn pri" href="/china/">Start with the China guides</a><a class="btn" href="https://www.youtube.com/@scratchandroam?sub_confirmation=1" rel="noopener">Subscribe on YouTube</a></div>
    <p style="margin-top:22px"><span class="hand">Scratch to reveal. Roam to discover.</span></p>
  </div>
  <div class="ticket"><span class="tape"></span><span class="stamp">BON VOYAGE</span>
    <div class="top"><span>FROM: CORK, IRELAND</span><span>SEAT 12A</span></div>
    <div class="to">TO: <span style="color:var(--pink)">???</span></div>
    <div class="scratch" id="scratch"><div class="photo"><b>SHANGHAI</b></div><canvas id="foil" aria-label="Scratch the foil to reveal the destination"></canvas><div class="hint">scratch me ✎</div></div>
  </div>
</section>

<section class="sec"><div class="wrap">
  <div class="sechead"><div><p class="eyebrow">Start here</p><h2>China first-timer guides</h2><p>Each guide is the video plus the full written steps, so you can read it without sound. Facts checked against official pages, with the date we checked them.</p></div><span class="pill">Rules change, so every guide is dated</span></div>
  <div class="grid">
    <a class="card" href="/guides/china-arrival-card-pc/"><div class="thumb t1"><b>ARRIVAL CARD<br>ON A PC</b></div><div class="cb"><div class="meta"><span>GUIDE</span><span>VIDEO + STEPS</span></div><h3>China arrival card online, step by step on a computer</h3><p>Upload your passport, let it fill the form, save the QR. Every screen shown.</p><span class="go">Read the guide →</span></div></a>
    <a class="card" href="/guides/china-arrival-card-alipay/"><div class="thumb t2"><b>ARRIVAL CARD<br>IN ALIPAY</b></div><div class="cb"><div class="meta"><span>GUIDE</span><span>VIDEO + STEPS</span></div><h3>China arrival card in Alipay on your phone</h3><p>The same card through the Alipay mini program, for people who do it on the way.</p><span class="go">Read the guide →</span></div></a>
    <a class="card" href="/guides/first-time-in-china/"><div class="thumb t3"><b>13 THINGS<br>BEFORE YOU FLY</b></div><div class="cb"><div class="meta"><span>GUIDE</span><span>VIDEO + CHECKLIST</span></div><h3>First time in China: 13 things to set up before you fly</h3><p>Visa-free list, arrival card, Alipay and WeChat, cards, cash, trains, maps, packing.</p><span class="go">Read the guide →</span></div></a>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="route"><div><p class="eyebrow" style="color:#CFC7D4">Next trip</p><h2>December: Chengdu, Chongqing, Xi'an</h2><p>Pandas, hotpot, a metro that runs through a building, and the Terracotta Army. The guides from this trip land here first, then the videos.</p></div>
  <div class="stops"><span class="stop home">CORK</span><span class="dash">- - -</span><span class="stop">LONDON</span><span class="dash">- - -</span><span class="stop">CHENGDU</span><span class="dash">- - -</span><span class="stop">CHONGQING</span><span class="dash">- - -</span><span class="stop">XI'AN</span></div></div>
</div></section>

<section class="sec"><div class="wrap about">
  <div class="polaroid"><div class="img">photo of Natali</div><div class="cap">Natali, somewhere with a camera</div></div>
  <div><p class="eyebrow">About</p><h2>A maker from Ireland who travels with a camera and a lot of curiosity</h2><p>I make things for a living and film the trips in between. The scratch card is the idea: a place stays hidden until you scratch it, then it is all there. These pages are the parts I wish someone had written down for me.</p><p style="margin-top:16px"><a href="/about/">More about Scratch &amp; Roam →</a></p></div>
</div></section>
</main>
{SCRATCH_JS}'''

page("/","Scratch & Roam with Natali: China first-timer guides and travel videos",
     "Travel guides and videos from Natali, a maker from Ireland. First-timer China guides: arrival card, Alipay, visa-free rules. Scratch to reveal. Roam to discover.",
     HOME,
     [{"@context":"https://schema.org","@type":"WebSite","name":"Scratch & Roam with Natali","url":SITE,"inLanguage":"en","publisher":{"@type":"Person","name":"Natali","url":SITE+"/about/","sameAs":json.loads(SAMEAS)}},
      {"@context":"https://schema.org","@type":"Person","name":"Natali","url":SITE+"/about/","jobTitle":"Travel creator and maker","homeLocation":{"@type":"Place","name":"Ireland"},"sameAs":json.loads(SAMEAS)}])

# China index
CHINA = '''<main class="wrap guide">
<p class="eyebrow">China</p>
<h1>China guides for first-timers</h1>
<p class="lede">The practical part first: entry, payments, trains. The city pages (Shanghai now, Chengdu, Chongqing and Xi'an after December) come next.</p>
<section class="sec" style="border:0;padding-top:30px"><h2 style="margin-bottom:16px">Before you fly</h2><div class="grid">
<a class="card" href="/guides/first-time-in-china/"><div class="thumb t3"><b>13 THINGS<br>BEFORE YOU FLY</b></div><div class="cb"><div class="meta"><span>CHECKLIST</span></div><h3>First time in China: 13 things to set up before you fly</h3><span class="go">Read →</span></div></a>
<a class="card" href="/guides/china-arrival-card-pc/"><div class="thumb t1"><b>ARRIVAL CARD<br>ON A PC</b></div><div class="cb"><div class="meta"><span>STEP BY STEP</span></div><h3>China arrival card online on a computer</h3><span class="go">Read →</span></div></a>
<a class="card" href="/guides/china-arrival-card-alipay/"><div class="thumb t2"><b>ARRIVAL CARD<br>IN ALIPAY</b></div><div class="cb"><div class="meta"><span>STEP BY STEP</span></div><h3>China arrival card in Alipay on your phone</h3><span class="go">Read →</span></div></a>
</div></section>
<section class="sec"><h2 style="margin-bottom:10px">Shanghai, mostly at night</h2><p class="intro">Short videos and photo sets from the last trip are on <a href="https://www.youtube.com/@scratchandroam" rel="noopener">YouTube</a>, <a href="https://www.instagram.com/scratchandroam/" rel="noopener">Instagram</a> and <a href="https://www.tiktok.com/@scratchandroam" rel="noopener">TikTok</a>: the Bund after dark, Nanjing Road, the Huangpu river cruise, Shanghai Circus World and Shanghai Disneyland after dark. Pages for each are coming.</p></section>
</main>'''
page("/china/","China guides for first-timers: entry, payments, trains",
     "Practical China guides from Scratch & Roam: the arrival card, Alipay and WeChat setup, visa-free rules, trains and getting around, each with a video and written steps.",
     CHINA,[{"@context":"https://schema.org","@type":"CollectionPage","name":"China guides for first-timers","url":SITE+"/china/"}])

ABOUT = '''<main class="wrap guide" style="max-width:800px">
<p class="eyebrow">About</p>
<h1>Scratch &amp; Roam with Natali</h1>
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
 ("What the arrival card is","China's arrival card is filled in online before you land. The official page is on the National Immigration Administration site and it is free."),
 ("Get ready","Have your passport, your flight number, the address of where you are staying and your reason for travel next to you."),
 ("Open the website",f'Go to the official page at <a href="{NIA}" rel="noopener">s.nia.gov.cn</a>. Use a computer with a camera or have a clear photo of your passport page ready to upload.'),
 ("Passport page: the form fills itself","Upload the photo page of your passport. The site reads it and fills in your name, passport number, nationality and dates. Check every field against your passport; type only what it did not recognise."),
 ("Basic and personal information","Confirm the basic details, then add the personal ones: contact details and anything the passport page could not supply."),
 ("Travel information","Flight number, where you will stay, how long, and why you are travelling. Use the address exactly as your booking shows it."),
 ("Sign and confirm","Sign on the screen and confirm. Read the summary once more before you submit."),
 ("Save your QR code","The site offers a QR code, a PDF download and an email copy. Take all of them. Keep the PDF on your phone in case there is no signal at the airport."),
]
guide("china-arrival-card-pc","China arrival card on a PC: step by step guide","China arrival card online on a PC, step by step",
      "Filling in the China arrival card online on a computer? Here is the whole form step by step, with the real form enlarged. Upload your passport and most of the details fill in for you.",
      "China arrival card online","33pgztdZT8Q",
      "<p>The arrival card is the one form every visitor fills in before landing in China. On a computer it takes a few minutes: the passport page does most of the typing, and at the end you save a QR code. This is the computer version; if you prefer your phone, use the <a href='/guides/china-arrival-card-alipay/'>Alipay guide</a>.</p>",
      PC_STEPS,COMMON_FAQ,
      [("National Immigration Administration: arrival card filling page",NIA,True)],
      None,
      chapters=[("0:00","Intro: the arrival card on a PC"),("0:15","What the arrival card is"),("0:44","Get ready"),("1:04","Open the website"),("1:20","Passport page: the form fills itself"),("1:43","Basic information"),("2:04","Personal information"),("2:28","Travel information"),("2:51","Sign and confirm"),("3:01","Save your QR code"),("3:29","Your move")],
      related=[("/guides/china-arrival-card-alipay/","t2","ARRIVAL CARD IN ALIPAY","China arrival card in Alipay on your phone"),("/guides/first-time-in-china/","t3","13 THINGS","First time in China: 13 things to set up before you fly")],
      minutes="PT3M41S",upload="2026-10-15")

AP_STEPS=[
 ("What the arrival card is","China's arrival card is filled in online before you land. The official version also lives inside Alipay as a mini program, and it is free."),
 ("Get ready","Have your passport, your flight number, the address of where you are staying and your reason for travel next to you. Install Alipay first if you have not yet."),
 ("Find the mini program in Alipay","Open Alipay and search for the arrival card mini program. Open it and agree to the terms."),
 ("Agree and passport page","Take a photo of the photo page of your passport. The app reads it and fills in your name, passport number, nationality and dates. Check each one."),
 ("Basic information","Confirm the basic details the passport page supplied."),
 ("Personal information","Add your contact details and anything the passport could not supply."),
 ("Travel information","Flight number, where you will stay, how long, and why you are travelling. Use the address exactly as your booking shows it."),
 ("Sign and confirm","Sign on the screen and confirm. Read the summary once more before you submit."),
 ("Save your QR code","Save the QR code, download the PDF and send it to your email, so it is on your phone even without signal."),
]
guide("china-arrival-card-alipay","China arrival card in Alipay: step by step guide","China arrival card in Alipay on your phone, step by step",
      "Filling in the China arrival card online with Alipay on your phone? Here is the whole form step by step. Upload your passport and most of the details fill in for you.",
      "China arrival card Alipay","YDdwz1ChMFE",
      "<p>If you already have Alipay set up for paying in China, the arrival card is inside it too. The passport page fills in most of the form, you check it, and you save the QR code at the end. Prefer a computer? Use the <a href='/guides/china-arrival-card-pc/'>PC guide</a>.</p>",
      AP_STEPS,COMMON_FAQ,
      [("National Immigration Administration: arrival card filling page",NIA,True)],
      None,
      chapters=[("0:00","Intro: the arrival card in Alipay"),("0:13","What the arrival card is"),("0:42","Get ready"),("1:03","Find the mini program in Alipay"),("1:21","Agree and passport page"),("1:42","Basic information"),("1:59","Personal information"),("2:15","Travel information"),("2:32","Sign and confirm"),("2:42","Save your QR code"),("3:10","Your move")],
      related=[("/guides/china-arrival-card-pc/","t1","ARRIVAL CARD ON A PC","China arrival card online on a computer"),("/guides/first-time-in-china/","t3","13 THINGS","First time in China: 13 things to set up before you fly")],
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
      None,
      chapters=[("1","Entry rules"),("2","Arrival card"),("3","Get the apps"),("4","Pay setup"),("5","Mini-programs"),("6","The ¥200 fee"),("7","Cash"),("8","Flights"),("9","Booking"),("10","Trains"),("11","Station day"),("12","Maps"),("13","Pack light")],
      related=[("/guides/china-arrival-card-pc/","t1","ARRIVAL CARD ON A PC","China arrival card online on a computer"),("/guides/china-arrival-card-alipay/","t2","ARRIVAL CARD IN ALIPAY","China arrival card in Alipay on your phone")])
