# Top 25 China apps, Boarding Pass style (SR-0027). Same data and look as the Short.
# Rows PURPOSE / WHAT / HOW / WHY / WITHOUT IT are the words used in the video; FINE PRINT is the checked detail (18 Oct 2026).
import html as _h

BP_IMPW=['','OPTIONAL','HANDY','VERY USEFUL','ESSENTIAL','CRITICAL']
BP_COL=['#E05A7A','#2F6F73','#C98A1B','#6B4BB8','#2E6BB0','#3C9A5F']
BP_CATI={'PAY':0,'CHAT':1,'NET':2,'MAP':3,'RIDE':4,'BOOK':5,'RAIL':6,'TRANS':7,'FOOD':8,'SOCIAL':9,'SHOP':10}
BP_GROUPS=[
 ("critical",5,"Critical: set these up before you fly","Money, messages, data and maps. Without these, the first day is hard.",1,5),
 ("essential",4,"Essential: day one and the first week","Rides, trains, translation and food. You can get by without them, but not comfortably.",6,10),
 ("useful",3,"Very useful: for eating, metro and backup","Where to eat, the metro in English, and a spare translator for when one fails.",11,15),
 ("handy",2,"Handy: shopping, scouting and price checks","Nice to have. Install them when you have time, or when you need them.",16,20),
 ("optional",1,"Optional: backups and skip-it apps","Second and third options. Two of these come with a warning.",21,25),
]
# n, name, glyph, cn, cat, purpose, what, how, why, without, boarding, fine print (html), source line
BP=[
 (1,"Alipay","支","支付宝","PAY","Pay for almost anything","China's wallet, takes your Visa","Link your card before you fly","DiDi and Meituan live inside it","You struggle to pay for almost anything.","Before you fly",
  "Verify your passport first, then link a Visa or Mastercard. Do it two or three days before you fly: guides report waits of up to 72 hours for the passport check. Payments up to ¥200 are free and a payment over ¥200 carries a 3% fee, so check the fee shown in your own Alipay. Taxis, food delivery, trains and the arrival card all open as mini-programs inside it. Full setup: <a href=\"/guides/china-travel-apps/\">China travel apps guide</a>.",
  "Trip.com; China for Travelers; Alipay"),
 (2,"WeChat","微","微信","CHAT","Chat, pay and open mini apps","Chat, pay and mini apps in one","Register at home, add a card in Me","Hotels and guides message here","No chat with guides, no mini apps.","Before you fly",
  "Add your card under Me, Pay and Services, Wallet, Bank Cards. New accounts are sometimes asked for a friend verification, where someone already on WeChat scans a code for you, so start at home. Tencent announced on 27 May 2026 that first-time users who link an international card pay no transaction fee for 90 days, on up to ¥1,000 a day. After that, WeChat's own help page says payments over ¥200 carry 3%.",
  "WeChat Help Center; Tencent, 27 May 2026"),
 (3,"VPN","V","VPN","NET","Unlock your usual apps","Unlocks Google, WhatsApp, Instagram","Install and test it at home","VPN stores are blocked in China","No Google, no WhatsApp, no Instagram.","Before you fly",
  "You cannot get one after you land: Apple removed VPN apps from the China App Store in 2017 and provider sites are blocked. LetsVPN, long the one people recommended, said in April 2026 it was ending service for mainland China. Pick a paid VPN with a stealth or obfuscation mode, test it at home, and treat it as a backup. Using one sits in a legal grey area in China.",
  "Airalo; China Digital Times; Comparitech"),
 (4,"Airalo eSIM","e","eSIM","NET","Get data the moment you land","Data that routes outside China","Install at home, switch on at landing","Online the moment you land","No maps, no rides, no messages on arrival.","Before you fly",
  "Airalo, Holafly, Nomad and Trip.com say their China plans route your data outside China, so Google, WhatsApp and Instagram work without a VPN; read the plan description to be sure. Install it on Wi-Fi at home. An eSIM is data only, so keep your home SIM for text codes from your bank, Alipay and WeChat. Hotel Wi-Fi does not route abroad, which is why a VPN is still the backup.",
  "Airalo; Nomad"),
 (5,"Amap","高","高德地图","MAP","Walk, ride and find metro exits","China's main map, 360 million daily users","Search in English, pick walk or metro","Google Maps is weak there","Wrong pins and the wrong metro exit.","Before you fly",
  "Amap (Gaode) reported a record 360 million daily users on 1 October 2025. The AMap Global app has had English since January 2025 and 14 more languages since July 2025, and it books taxis in English. Paste the Chinese name of your hotel from the booking into the search box. On an iPhone, Apple Maps also works in China without a VPN and is a fine second map.",
  "Alibaba Group; Shanghai government; AMap, Aug 2026"),
 (6,"DiDi","滴","滴滴","RIDE","Book a car without haggling","Ride hailing, price shown upfront","Open it inside Alipay, pay in app","No haggling, no Mandarin needed","Haggling in Mandarin at the curb.","Day one",
  "DiDi opens inside Alipay under Transport, so you do not need the standalone app. AMap Global also books rides in English and pays through Alipay or WeChat Pay. Link Alipay at home first.",
  "Alipay; AMap; DiDi on the App Store"),
 (7,"Trip.com","携","携程","BOOK","Book trains, flights and hotels","Trains, flights, hotels in English","Search the route, pay with your Visa","Plan B when 12306 says no","No plan B when 12306 says no.","Before you fly",
  "The easiest place to book in English, with 24/7 English support and guest checkout for trains that does not need a verified passport. Its hotel search can filter for hotels that accept foreign guests, which matters because some hotels in China still cannot take foreigners. Compare the final price with 12306 before you pay.",
  "Trip.com; China Railway 12306"),
 (8,"12306","铁","12306","RAIL","Book trains at the real price","The official China Railway app","Register with your passport","Cheapest fare, no booking fee","Paying a fee on third party apps.","Before you fly",
  "Register and verify your passport at home. Tickets normally open 15 days ahead, counting the travel day. Quiet features: a waitlist for sold-out trains, where you prepay and get a refund if it fails, and a 60-day reservation pilot on more than 200 Beijing to Shanghai trains since 20 July 2026. Beware of lookalike apps: the official one is 铁路12306.",
  "China Railway 12306; Beijing government, July 2026"),
 (9,"Baidu Translate","百","百度翻译","TRANS","Read signs and menus","Camera translates menus and signs","Point, tap, read","Works without a VPN","Menus and signs you cannot read.","Before you fly",
  "A March 2026 guide says it works on any Chinese network, so no VPN. Text works offline after you download the Chinese pack; the camera needs a connection.",
  "Chinavigators, March 2026; Trip.com, June 2026"),
 (10,"Pleco","词","词","TRANS","Look up any Chinese word","Chinese dictionary with camera and pen input","Draw or scan a character","Catches what translators miss","Words that translators get wrong.","Before you fly",
  "A free offline Chinese dictionary: when a menu translation makes no sense, look up the characters one by one. Drawing a character with your finger is free; camera recognition is a paid add-on (€9.99 on the Irish App Store).",
  "Pleco on the App Store"),
 (11,"Meituan","美","美团","FOOD","Get food delivered","Food delivery and local deals","Order through the Alipay mini app","Hungry at the hotel? Solved","Stuck with the minibar.","Day one",
  "Use the Meituan mini-program inside Alipay or WeChat rather than the standalone app. One 2026 guide found the standalone app is Chinese only and its phone field expects a mainland number, so use your hotel's number and the front desk can pass the food on. Restaurants set minimum orders, and the remarks field takes notes like less spicy.",
  "WanderInChina; Chinaguidelines, 2026"),
 (12,"Dianping","点","大众点评","FOOD","Choose where to eat","Where locals read restaurant reviews","Search your area, sort by rating","Skip the tourist trap menus","Tourist trap menus.","Day one",
  "China's main restaurant review app. The App Store lists English, but in practice it is partial and reviews are not translated. The feature worth installing it for is 排队 (queue): take a number for a busy restaurant from your phone and watch how many tables are ahead of you.",
  "WanderInChina, Feb 2026"),
 (13,"MetroMan China","地","地铁","RAIL","Plan metro trips","Metro maps for Chinese cities","Pick the city, tap your stations","Plan transfers in English","Lost between transfers.","Day one",
  "Offline metro maps for 53 Chinese cities, including Chengdu, Chongqing and Xi'an, in English. Free with an optional paid upgrade. In Beijing, Shanghai and Chengdu you can also tap a foreign Visa or Mastercard straight on the gate.",
  "MetroMan on the App Store; China for Travelers"),
 (14,"Google Translate","译","译","TRANS","Translate offline","Chinese pack works offline","Download Chinese at home","Still works with no signal","A dead translator in a tunnel.","Before you fly",
  "Download the Chinese pack before you go, because the offline pack is what you can count on. Guides disagree on whether the online version works on Chinese Wi-Fi without a VPN (one from March 2026 says it is blocked, one from June 2026 says it no longer needs a VPN), so treat online use as a bonus.",
  "Chinavigators, March 2026; Trip.com, June 2026"),
 (15,"Microsoft Translator","译","译","TRANS","Keep a backup translator","A second translator on standby","Download Chinese for offline use","Backup when one app fails","One app fails and you are stuck.","Before you fly",
  "A March 2026 guide says it is not blocked on Chinese networks and has a full offline mode with downloaded packs, including text, voice and camera. It also supports Cantonese. On an iPhone, Apple Translate works offline too once Chinese is downloaded.",
  "Chinavigators, March 2026; Trip.com, June 2026"),
 (16,"Taobao","淘","淘宝","SHOP","Shop online in China","China's biggest online shop","Search in English, pay with Alipay","Gifts and supplies, tiny prices","Missing the tiny prices.","Anytime",
  "First-hand: on my account, bought from Ireland, Chinese was the only language on offer, but I could switch the currency to euro and search in English. Add a delivery address first, ask your hotel before sending a parcel there, and pay with Alipay. The full 12 steps are in my <a href=\"/guides/taobao-for-foreigners/\">Taobao guide</a>.",
  "Natali, first-hand"),
 (17,"RedNote","红","小红书","SOCIAL","Find local food and places","Locals share places and food spots","Search a place, read the posts","Find spots before they trend","Missing what locals love.","Anytime",
  "Ask anyone in China where to eat and they open RedNote. It added AI translation in January 2025 and you can sign up with a foreign number, but the interface is still mostly Chinese, so search with the Chinese name of a place copied from Amap.",
  "TechNode, Jan 2025"),
 (18,"Douyin","抖","抖音","SOCIAL","Scout places in short videos","China's short video app","Search a place, watch locals","See queues and crowds first","Walking into crowds blind.","Anytime",
  "The app is entirely in Chinese, so paste the Chinese name of the place into search. Guest browsing works without an account. Full features need real-name verification, and a June 2026 guide says foreign passports are not reliably accepted. On an iPhone you may need to switch your App Store region to download it. It is separate from TikTok.",
  "ChinaSurvivalKit, June 2026"),
 (19,"Fliggy","飞","飞猪","BOOK","Compare trip prices","Alibaba's travel booking app","Open it inside Alipay","Another price check for trips","Overpaying for a trip.","Anytime",
  "Alibaba's travel app, with a mini-program inside Alipay. Alipay and Fliggy ran a flight coupon campaign for international visitors in January 2024. I would use it only as a price check next to Trip.com.",
  "Business Today, Jan 2024"),
 (20,"Youdao","有","有道","TRANS","Translate from a photo","Translator with a photo mode","Snap the sign, read the result","Third opinion on hard text","Stuck on a sign two apps missed.","Anytime",
  "A June 2026 list calls it best for offline chats, with a Chinese-English offline package and, recently, offline voice translation. Download the package at home.",
  "Trip.com, June 2026"),
 (21,"DeepL","D","DeepL","TRANS","Translate long texts","Sharp translation of long text","Paste copied Chinese, read English","Best for long messages","Clumsy translations of long messages.","Anytime",
  "Good for long copied messages and files. I could not confirm whether it works in China without a VPN: a June 2026 list says you need one, so test it at home and keep it as an optional third translator.",
  "Trip.com, June 2026"),
 (22,"Waygo","W","Waygo","TRANS","Read menus offline","Offline menu translator","Point the camera at a menu","No data needed","No signal, no menu.","Skip it",
  "Skip it unless you already have it. It is still in the App Store but has not been updated since 2017, and one 2026 list says its translations can be rough. Use Baidu Translate or Microsoft Translator for menus instead.",
  "Waygo on the App Store; Trip.com, June 2026"),
 (23,"Ele.me","饿","饿了么","FOOD","Order food as a backup","A second delivery app","Open it from Alipay","Backup when Meituan has no courier","No dinner when Meituan fails.","Anytime",
  "The Ele.me brand was retired in December 2025: it is now called Taobao Flash Sale (淘宝闪购), same service, and runs as a mini-program in Alipay. Look for that name. One 2026 guide found it has no English and needs a Chinese-format phone number for the rider, so use your hotel's.",
  "TechNode, Dec 2025; Caixin; Chinaguidelines"),
 (24,"Hellobike","哈","哈啰","RIDE","Rent a bike or scooter","Bike and scooter rental","Scan the code on the bike","Short hops without a taxi","Waiting for a taxi for a short hop.","Anytime",
  "Scan the QR code on the handlebars; a 2026 guide says the China version lets you log in with WeChat or Alipay. Prices are around ¥1 to ¥1.50 for the first 15 minutes, most users pay no deposit, and parking outside the marked zones can be fined. Check the app for current prices and zones.",
  "Trip.com, April 2026"),
 (25,"Kuli Kuli","K","Kuli Kuli","TRANS","Know before you tap","Travel translator with a paywall","Check the free allowance in the app","Know before you tap","A surprise paywall mid menu.","Skip it or be warned",
  "Free to download, but its App Store listing sells unlimited-translation passes from $1.99 for 3 days up to $19.99 for life. I could not confirm the free daily allowance on the listing, so check it in the app before you rely on it.",
  "Kuli Kuli on the App Store"),
]

BP_SOURCES=[
 ("WeChat Help Center: international cards on Weixin Pay","https://cs.help.wechat.com/hc/en-us/articles/11975770896271-How-to-Set-Up-International-Cards-for-Weixin-Pay",True),
 ("Tencent: Weixin Pay 90-day fee waiver, 27 May 2026","https://www.tencent.com/en-us/articles/2202338.html",True),
 ("Alipay on the App Store","https://apps.apple.com/app/alipay/id333206289",True),
 ("Trip.com: how to add a card to Alipay, June 2026","https://www.trip.com/guide/payments/how-to-add-card-to-alipay.html",False),
 ("China for Travelers: Alipay for foreigners, August 2026","https://chinafortravelers.com/guides/alipay-for-foreigners/",False),
 ("Alibaba Group: Amap daily users pass 360 million, 3 October 2025","https://www.alibabagroup.com/document-1910786468402429952",True),
 ("Shanghai government: AMap in 15 languages, July 2025","https://english.shanghai.gov.cn/en-Latest-WhatsNew/20250711/8f2fcf3c6b624a56a6b2c0d8152ea2f2.html",True),
 ("AMap: ride-hailing for international visitors, August 2026","https://en.prnasia.com/releases/global/amap-brings-ride-hailing-to-international-visitors-in-china-543611.shtml",True),
 ("DiDi China on the App Store","https://apps.apple.com/app/id554499054",True),
 ("China Railway 12306: FAQ","https://www.12306.cn/en/faq.html",True),
 ("Beijing government: 12306 ticket reservation pilot, July 2026","https://english.beijing.gov.cn/travellinginbeijing/transportation/railway/202607/t20260720_4772390.html",True),
 ("Trip.com: sold-out trains and the waitlist, August 2026","https://my.trip.com/guide/transport/china-train-tickets-sold-out.html",False),
 ("MetroMan China on the App Store","https://apps.apple.com/app/id466351433",True),
 ("China for Travelers: paying with a foreign card at metro gates, August 2026","https://chinafortravelers.com/guides/china-metro-foreign-card/",False),
 ("Airalo: is a VPN needed in China?","https://www.airalo.com/help/using-managing-esims/ZSEEHBT5HW6F/stay-connected-in-china-your-guide-to-unfiltered-internet-access-is-a-vpn-required/ZDZBNIKI4TFP",False),
 ("Nomad: do eSIMs work in China?","https://www.nomadesim.com/blog/do-esims-work-in-china",False),
 ("China Digital Times: LetsVPN ends mainland service, April 2026","https://chinadigitaltimes.net/chinese/726869.html",False),
 ("Comparitech: are VPNs legal in China? June 2026","https://www.comparitech.com/blog/vpn-privacy/are-vpns-legal-in-china",False),
 ("Chinavigators: the best translation apps for China, March 2026","https://www.chinavigators.com/translation-apps-china/",False),
 ("Trip.com: top 10 China translation apps, June 2026","https://www.trip.com/guide/info/china-translate-app.html",False),
 ("Pleco on the Irish App Store","https://apps.apple.com/ie/app/pleco-chinese-dictionary/id341922306",True),
 ("Chinaguidelines: food delivery in China for foreigners, 2026","https://chinaguidelines.com/en/posts/food-delivery",False),
 ("WanderInChina: Dianping and Meituan, February 2026","https://wanderinchina.com/survival-guide/useful-mobile-apps/dazhong-dianping-meituan/",False),
 ("TechNode: Ele.me rebrands as Taobao Flash Sale, 5 December 2025","https://technode.com/2025/12/05/ele-me-rebrands-as-taobao-flash-sale-ending-17-years-as-an-independent-brand/",False),
 ("Caixin: Alibaba retires the Ele.me brand, December 2025","https://www.caixinglobal.com/2025-12-05/alibaba-retires-eleme-brand-in-shift-to-instant-retail-102390218.html",False),
 ("TechNode: RedNote adds translation, January 2025","https://technode.com/2025/01/20/xiaohongshu-rolls-out-ai-powered-translation-feature-likely-using-gpt-4/",False),
 ("ChinaSurvivalKit: Douyin guide for foreigners, June 2026","https://chinasurvivalkit.com/blog/douyin-chinese-tiktok-guide-foreigners",False),
 ("Business Today: Alipay and Fliggy for international visitors, January 2024","https://www.businesstoday.com.my/2024/01/31/alipay-fliggy-collaborate-to-enhance-travel-experience-for-international-visitors-to-china/",False),
 ("Trip.com: HelloRide (Hellobike) in China, April 2026","https://sg.trip.com/guide/transport/helloride.html",False),
 ("Waygo on the Irish App Store","https://apps.apple.com/ie/app/waygo-chinese-japanese-and-korean-translator/id496038103",True),
 ("Kuli Kuli on the App Store","https://apps.apple.com/app/id6458146511",True),
]

def bp_board():
    esc=_h.escape
    rail="".join(f'<a href="#app-{a[0]}" style="--c:{BP_COL[BP_CATI[a[4]]%6]}" aria-label="Pass {a[0]}: {esc(a[1])}"><i></i></a>' for a in BP)
    out=f'<section class="bp" id="board" aria-label="Top 25 China apps as boarding passes"><div class="bp-top"><span>HOME → CHINA · BOARDING IN ORDER OF IMPORTANCE</span><span class="bp-cnt">25 PASSES</span></div><nav class="bp-rail" aria-label="Jump to a pass">{rail}</nav>'
    for gid,imp,title,sub,lo,hi in BP_GROUPS:
        out+=f'<div class="bp-grp" id="{gid}"><p class="bp-k">BOARDING GROUP {6-imp} · {BP_IMPW[imp]}</p><h2>{esc(title)}</h2><p class="bp-sub">{esc(sub)}</p>'
        for a in BP:
            n,name,g,cn,cat,job,what,how,why,wo,when,fine,src=a
            if not lo<=n<=hi: continue
            c=BP_COL[BP_CATI[cat]%6]
            pips="".join(f'<i{" class=on" if k<imp else ""}></i>' for k in range(5))
            bars="".join(f'<i style="width:{1+((n*7+k*13)%4)}px"></i>' for k in range(46))
            out+=f'''<article class="bp-pass" id="app-{n}" style="--c:{c}"><div class="bp-h"><span class="bp-g" aria-hidden="true">{esc(g)}</span><div class="bp-tx"><span class="bp-air">HOME → CHINA · BOARDING PASS</span><h3>{esc(name)}<small>{esc(cn) if cn!=name else ""}</small></h3></div><span class="bp-rk">#{n:02d}</span></div>
<div class="bp-b"><div class="bp-fg"><div><b>GATE</b>#{n:02d}</div><div><b>CLASS</b>{BP_IMPW[imp]}</div><div><b>BOARDING</b>{esc(when)}</div><div><b>IMPORTANCE</b>{imp}/5 <span class="bp-pips" aria-hidden="true">{pips}</span></div></div>
<div class="bp-perf"></div>
<div class="bp-rows"><div class="bp-r"><b>PURPOSE · USE IT TO</b>{esc(job)}</div><div class="bp-r"><b>WHAT IT IS</b>{esc(what)}</div><div class="bp-r"><b>HOW</b>{esc(how)}</div><div class="bp-r"><b>WHY IT RANKS</b>{esc(why)}</div></div>
<p class="bp-fine"><b>FINE PRINT · CHECKED 18 OCT 2026</b>{fine}</p>
<div class="bp-st"><b>WITHOUT IT</b>{esc(wo)}</div>
<p class="bp-src">SRC: {esc(src)}</p></div><div class="bp-bc" aria-hidden="true">{bars}</div></article>'''
        out+='</div>'
    chk="".join(f'<label><input type="checkbox" data-n="{a[0]}"><span class="no">{a[0]:02d}</span>{esc(a[1])}</label>' for a in BP)
    out+=f'''<div class="bp-end" id="complete"><p class="bp-k">CHECK IN</p><h2>Boarding complete?</h2><p class="bp-sub">Tick each app as you install it. Your ticks stay on this device only. <b id="bp-n">0 of 25</b> ready.</p><div class="bp-chk">{chk}</div></div></section>
<script>(function(){{var B=document.getElementById('board');if(!B)return;var N=document.getElementById('bp-n'),K='sr-top25-china-apps',s={{}};
try{{s=JSON.parse(localStorage.getItem(K)||'{{}}')||{{}}}}catch(e){{s={{}}}}
var bx=B.querySelectorAll('.bp-chk input'),rl=B.querySelectorAll('.bp-rail a');
function upd(){{var c=0;bx.forEach(function(x,i){{if(x.checked)c++;rl[i].classList.toggle('ok',x.checked)}});N.textContent=c+' of 25'}}
bx.forEach(function(x){{x.checked=!!s[x.dataset.n];x.addEventListener('change',function(){{s[x.dataset.n]=x.checked;try{{localStorage.setItem(K,JSON.stringify(s))}}catch(e){{}}upd()}})}});upd();
if(!('IntersectionObserver' in window)||matchMedia('(prefers-reduced-motion:reduce)').matches)return;
var ps=B.querySelectorAll('.bp-pass');B.classList.add('bp-js');
var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}})}},{{rootMargin:'0px 0px -12% 0px'}});ps.forEach(function(p){{io.observe(p)}});
var cur=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{var i=+e.target.id.split('-')[1]-1;rl.forEach(function(r){{r.classList.remove('cur')}});rl[i].classList.add('cur')}}}})}},{{rootMargin:'-30% 0px -60% 0px'}});ps.forEach(function(p){{cur.observe(p)}});
}})();</script>'''
    return out
