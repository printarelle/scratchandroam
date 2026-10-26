# How to order food in China without speaking Chinese (SR-0046). Ember phrase-card look. Facts checked 26 Oct 2026.
OR_SLUG="how-to-order-food-in-china-without-speaking-chinese"
OR_STEPS=[
 ("Load a translator camera before you fly","China Navigators calls Baidu Translate's camera mode the most accurate free tool for reading Chinese menus live, and says to download the offline Chinese pack before you travel. Hold the camera steady for 2 to 3 seconds, use your phone torch in a dim restaurant, and scan a long menu in sections. It says Google Translate's camera is less accurate for Chinese."),
 ("Set up Alipay or WeChat Pay at home","Scan-to-order menus and most stall QR codes run on one of these two apps, so set one up before the trip. See the payment section below for what the sources say about foreign cards."),
 ("Point, then say what you want","Point at the dish on a picture menu or at the food itself and say <b>我要这个</b> (wǒ yào zhège), I want this one. China Navigators gives the same sentence with 那个 (nà gè), that one, and calls it universally understood. If there is no picture, point at the characters on a list or on your phone screen."),
 ("Show how many","Say <b>一份</b> (yī fèn), one portion, which China Highlights gives for picture menus. For dumplings it gives <b>一笼</b> (yī lóng), one tray. For anything else, hold up fingers or type the number on your phone. I have not found a source for the hand signs for 6 to 10, so I do not teach them here."),
 ("Ask the price","<b>多少钱？</b> (duōshao qián?) means how much? It is standard Mandarin that I wrote myself, not copied from a guide. Show it on your phone if you are unsure of the pronunciation."),
 ("Take it away with 打包","<b>打包</b> (dǎbāo) means to pack up, which is what you say for takeaway. Also my own standard-Mandarin phrase, so check it in a translator app first."),
 ("Pay by QR code, or with small cash","Scan the stall's QR code in Alipay or WeChat Pay, or pay cash. Trip.com says small vendors often lack change, so carry ¥10, ¥20 and ¥50 notes and avoid ¥100."),
]
OR_PHRASES=[
 ("我要这个","wǒ yào zhège","I want this one","Mine. China Navigators gives the same pattern with 那个 (that one)."),
 ("我要那个","wǒ yào nà gè","I want that one (point at someone else's dish)","China Navigators"),
 ("一份","yī fèn","One portion","China Highlights"),
 ("一笼","yī lóng","One tray (of dumplings)","China Highlights"),
 ("多少钱？","duōshao qián?","How much?","Mine, standard Mandarin."),
 ("打包","dǎbāo","Takeaway, to go","Mine, standard Mandarin."),
 ("不要辣","bù yào là","No spice","China Navigators"),
 ("不要猪肉","bù yào zhūròu","No pork","China Navigators"),
 ("最受欢迎的是什么？","zuì shòu huānyíng de shì shénme?","What is most popular?","China Navigators"),
 ("买单","mǎidān","The bill","China Navigators"),
]
OR_PAY=[
 ("works","📲","Alipay or WeChat Pay","China Navigators says both are accepted at almost all restaurants in Chinese cities. Trip.com calls Alipay the most reliable option for street food, scanning the printed code on the table or the vendor's own QR code.","China Navigators; Trip.com"),
 ("works","💳","Link a foreign card to the app","A People's Bank of China payment guide (reported by China Briefing, March 2024) says foreign cards can be linked with just a mobile number, and that single-transaction limits rose from US$1,000 to US$5,000. Trip.com says tourist Alipay links Visa, Mastercard and JCB, and that WeChat Pay has stricter limits.","China Briefing; Trip.com"),
 ("works","💴","Cash","China Navigators says cash works everywhere. Trip.com says small vendors often lack change, so carry small notes. The PBOC guide says foreign cards can also take out RMB at ATMs showing the card's logo.","China Navigators; Trip.com; China Briefing"),
 ("no","💳","Relying on a foreign card at a stall","China Navigators says foreign credit cards work only at international hotel restaurants and some chains. Do not count on tapping a card at a market stall.","China Navigators"),
]
def _or_extra():
    ph="".join(f'<tr><td class="zh">{z}</td><td>{p}</td><td><b>{m}</b></td><td>{n}</td></tr>' for z,p,m,n in OR_PHRASES)
    pay="".join(f'<div class="sp-c sp-{v}"><div class="sp-e">{e}</div><div><b>{t}</b><span class="sp-v">{ {"works":"Works","no":"Do not count on it"}[v]}</span><p>{d}</p><small>Source: {s}</small></div></div>' for v,e,t,d,s in OR_PAY)
    slides=["order-food-china-ordering-without-chinese-hook-slide","order-food-china-point-and-ask-the-price-slide","order-food-china-take-it-away-dabao-slide","order-food-china-pay-with-qr-or-cash-slide","order-food-china-scan-to-order-menus-slide"]
    figs='<div class="shots sp-shots">'+"".join(f'<figure><a href="/img/{k}.jpg"><img src="/img/{k}.jpg" alt=""></a><figcaption>{html.escape(IMGREG[k+".jpg"]["cap"])}</figcaption></figure>' for k in slides)+'</div>'
    return f'''<section class="sp" id="phrases"><div class="sp-head"><span class="sp-k">Phrase cards</span><h2>Ten phrases to point at or show on your phone</h2></div>
<p class="sp-lead">You do not need to pronounce these well. Show the characters, point, and use your fingers for numbers.</p>
<div class="sp-tw"><table class="sp-t"><thead><tr><th>Chinese</th><th>Pinyin</th><th>Meaning</th><th>Where it is from</th></tr></thead><tbody>{ph}</tbody></table></div>
<p class="sp-fine">Where a source is named, I copied the phrase from it. Where it says mine, it is standard Mandarin I wrote myself. Check any phrase in a translator app before you rely on it.</p></section>
<section class="sp" id="scan"><div class="sp-head"><span class="sp-k">At a table</span><h2>Scan-to-order menus</h2></div>
<p class="sp-lead">In many restaurants you do not get a paper menu. You scan a QR code on the table, order from your own phone, and pay there too.</p>
<div class="sp-two"><div><h3 class="sp-h3">How it works</h3><p>The China Project (Siyuan Meng, 18 November 2021) says diners scan a code to see the menu, order from their phones and pay separately. The menu opens in the restaurant's own mini program or a food service app such as Meituan, or you are asked to follow the restaurant's WeChat account. China Navigators (23 March 2026) says it is common in Beijing, Shanghai, Guangzhou and Chengdu, that you scan the table sticker with WeChat, and that most items have photos.</p></div>
<div><h3 class="sp-h3">The catch for visitors</h3><p>The China Project notes that digital menus often require scanning through WeChat or Alipay, and says some people may be shut out. It does not say what a visitor without those apps should do. My advice, not a source's: set up one of the apps before you fly, and if it will not open, ask the staff for a paper menu or point at food.</p></div></div></section>
<section class="sp" id="markets"><div class="sp-head"><span class="sp-k">Markets and street stalls</span><h2>Night markets: point, count, pay</h2></div>
<p class="sp-lead">At a stall there is no menu to scan. You point at the food, say how many, and pay.</p>
<p>The night-market photos in this guide are from <b>Sijing Night Market</b> in Songjiang, Shanghai. The Shanghai government's English site (7 December 2023) gives the address as Sanxiang Square, No 2 Sibao Road, describes it as Shanghai's biggest open-air night market, and lists regional specialities such as sweet potato starch grilled rolls, oyster pancakes and Taiwan-style lemon tea. It does not give opening hours, so check before you go.</p>
<ol class="sp-say"><li><span class="zh">我要这个</span><span>wǒ yào zhège</span><em>Point at it</em></li><li><span class="zh">一份 / 一笼</span><span>yī fèn / yī lóng</span><em>One portion or one tray</em></li><li><span class="zh">多少钱？</span><span>duōshao qián?</span><em>Ask the price</em></li><li><span class="zh">打包</span><span>dǎbāo</span><em>Takeaway</em></li></ol>
<p class="sp-fine">Two sources disagree on pointing at other diners' food. China Navigators calls it universally understood. China Highlights says it is somewhat rude, though locals usually excuse foreigners. At a stall, pointing at the food for sale is normal. At a restaurant table, be polite about it.</p></section>
<section class="sp" id="pay"><div class="sp-head"><span class="sp-k">Paying</span><h2>How to pay for street food and restaurant meals</h2></div>
<div class="sp-grid">{pay}</div></section>
<section class="sp sp-safe" id="allergy"><div class="sp-head"><span class="sp-k">Be careful</span><h2>Allergies and dietary needs</h2></div>
<p>The phrases for no spice and no pork are from China Navigators. If you have a serious allergy, a phrase is not enough: use a translator card written by a native speaker and ask at a sit-down restaurant, not a busy stall. This is travel advice, not medical advice.</p></section>
<h2>The five slides</h2><p>The same guide as a 5 slide carousel, to save for your trip. Tap a slide to open it larger.</p>{figs}'''

OR_INTRO='''<p>To order food in China without speaking Chinese, point at the dish, say 我要这个 (wǒ yào zhège), show the number with your fingers, ask 多少钱 (duōshao qián), and pay by QR code or small cash. This guide gives the phrases, how scan-to-order menus work, how to order at a night market or street stall, and how to pay as a visitor.</p>
<p>It is the written version of my Scratch &amp; Roam video and slides, filmed at a bun stall and at Sijing Night Market in Shanghai. The facts were checked against the sources at the bottom on 26 October 2026. Where sources disagree, or where I could not find one, I say so.</p>'''

OR_FAQ=[
 ("How do you order food in China without speaking Chinese?","Point at the dish, or at someone else's, and say 我要这个 (wǒ yào zhège), I want this one. Show how many with fingers or a typed number, use a translator camera for menus, and pay with a QR code in Alipay or WeChat Pay, or with small cash."),
 ("What is scan-to-order in China?","It is a menu you open by scanning a QR code on the table. You order and often pay from your own phone. According to The China Project, the menu opens in a restaurant's mini program or a food app, or asks you to follow the restaurant's WeChat account. Many need WeChat or Alipay, so set one up before you fly."),
 ("Can you pay with a foreign card at street food stalls in China?","Do not count on it. China Navigators says foreign credit cards work only at international hotel restaurants and some chains. A People's Bank of China guide says foreign cards can be linked to Alipay and WeChat Pay with a mobile number, which is the usual workaround. Cash also works, but small vendors may lack change."),
 ("How do you say takeaway in Chinese?","打包 (dǎbāo) is the standard word for packing up food to take away. It is a phrase I wrote from standard Mandarin, not copied from a guide, so check it in a translator app."),
 ("Is it rude to point at food in China?","Sources differ. China Navigators calls pointing at another table's dish universally understood. China Highlights says it is somewhat rude, though locals usually excuse foreigners. At a stall, pointing at the food for sale is normal."),
 ("What do you say to ask for no spice in Chinese?","不要辣 (bù yào là), from China Navigators. China Highlights gives 我不要辣 for no chillies. For a full guide to spice levels, read the spice tolerance guide.")]

OR_SOURCES=[("China Navigators: How to order food without English menus, app tips, 23 March 2026","https://www.chinavigators.com/order-food-china-apps/",False),
 ("The China Project, Siyuan Meng: Scan-to-order sweeps across China, to customers' chagrin, 18 November 2021","https://thechinaproject.com/2021/11/18/scan-to-order-sweeps-across-china-to-customers-chagrin",False),
 ("China Highlights: how to order Chinese food (no date shown)","https://www.chinahighlights.com/travelguide/chinese-food/how-to-order-chinese-food.htm",False),
 ("Trip.com: how to pay in China for foreigners (no date shown)","https://www.trip.com/guide/phone/how-to-pay-in-china.html",False),
 ("China Briefing: China unveils new guidelines on optimized payment services for foreigners, 29 March 2024, reporting the People's Bank of China guide","https://www.china-briefing.com/news/china-unveils-new-guidelines-on-optimized-payment-services-for-foreigners-an-overview/",False),
 ("Shanghai government English site: Sijing Night Market, 7 December 2023","https://english.shanghai.gov.cn/en-Nightlife/20231207/73e1410199d44e1d949608a22c503d41.html",True)]

guide(OR_SLUG,"How to Order Food in China Without Speaking Chinese","How to order food in China without speaking Chinese",
      "How to order food in China without speaking Chinese: phrases to point at, scan-to-order menus, night market and street stall ordering, and how to pay.",
      "how to order food in china without speaking chinese","",OR_INTRO,
      OR_STEPS,OR_FAQ,OR_SOURCES,SITE+"/og/how-to-order-food-in-china-without-speaking-chinese.jpg",
      related=[("/guides/build-spice-tolerance-before-china/","build-spice-tolerance-before-china-cover-16x9","SPICE","How to build spice tolerance before China: a 6 week plan"),
               ("/guides/china-travel-apps/","china-travel-apps-12-apps-to-set-up-before-china","GUIDE","Apps to download before you go to China"),
               ("/guides/china-before-you-fly-checklist/","china-before-you-fly-10-things-cover-16x9","10 THINGS","China first trip checklist: 10 things to sort before you fly")],
      checked="2026-10-26",published="2026-10-26",vschema=False,steps_title="How to order, step by step",
      lift='<div class="bp-hero sp-hero"><img data-hero src="/img/order-food-in-china-without-speaking-chinese-cover-16x9.jpg" alt="" width="1280" height="720"></div>',
      extra=_or_extra(),
      head='<style>@font-face{font-family:"Brico";font-weight:600;font-display:swap;src:url(/fonts/bricolage-600.woff2) format("woff2")}@font-face{font-family:"Brico";font-weight:700;font-display:swap;src:url(/fonts/bricolage-700.woff2) format("woff2")}@font-face{font-family:"Brico";font-weight:800;font-display:swap;src:url(/fonts/bricolage-800.woff2) format("woff2")}</style>')
