# What to buy before China, and what to buy there (12 Nov 2026).
# Product picks are Natali's own Amazon.ie links (resolved 12 Nov 2026); /go/<name> lives in src/amazon-links.json.
# "We use this" only on the two things she said they own and take on trips (luggage scale, Xiaomi daypack).
# Souvenir list is from other travellers' guides (sources at the bottom), not her own shopping.
import bright as _B
BUY_SLUG="what-to-buy-before-china-and-what-to-buy-there"
BUY_LINE="Based on my trips in December 2025 and April 2026. Rules change, so double check before you fly."

BUY_STEPS=[
 ("A plug adapter with USB-C ports",
  "Irish and UK plugs do not fit the standard sockets in mainland China, which take two flat pins (Type A) or three angled pins (Type I). Every hotel we stayed in in Shanghai had UK sockets as well, so my adapter stayed in the bag. I still pack one every time, because I would not count on that in every city. A universal one with USB-C ports means one plug charges the phone, the camera and the watch."),
 ("Charging cables that are long enough",
  "Hotel sockets are not always beside the bed. A two metre USB-C cable costs very little and saves you sitting on the floor to charge your phone. Bring a spare, because the cable is the thing that gets left behind in a hotel room."),
 ("The toiletries you trust, in travel sizes",
  "You can buy shampoo and shower gel anywhere in China. The things worth bringing are the ones where you want your own brand: deodorant and sun cream are the two that travellers say are hardest to find in the versions they are used to. Refillable bottles let you bring your own products without the full-size weight."),
 ("Tampons, if you use them",
  "China is very limited on tampons. Pads are everywhere, tampons are not. Bring the brand and size you actually use and are used to, enough for the whole trip."),
 ("Soap sheets and wipes for public toilets",
  "Many public toilets have no soap, and some have no paper. Paper soap sheets weigh nothing and dissolve under the tap. A small pack of wipes covers the times there is no tap at all. Tissues are the one thing I would not pack: pocket packs are sold in every corner shop in China, so buy those there."),
 ("Toilet seat covers, and a travel bidet if you are used to one",
  "Public toilets in China are often squat toilets, and the Western ones in busy places are not always clean. Disposable seat covers fold flat in a day bag. And for those who are used to a bidet at home, for personal or any other reasons, a small rechargeable travel bidet is a very good thing to bring."),
 ("A small medical kit",
  "Finding the right medicine in a Chinese pharmacy with a translation app is slow when you feel unwell. Bring a small kit with plasters and the basics, then add your own: something for an upset stomach, rehydration sachets, pain relief and a cold remedy. Check the ingredients of cold and flu tablets first, because pseudoephedrine (in Sudafed and similar) is controlled in China. My <a href=\"/guides/china-dos-and-donts/\">do's and don'ts guide</a> has the detail. Keep prescription medicine in its original box with the prescription."),
 ("A sleep mask and earplugs for the flight",
  "Ireland to China is a long way with at least one change for most of us. A sleep mask that comes with earplugs is the cheapest way to arrive less tired."),
 ("Packing cubes",
  "A China trip usually means several hotels. Cubes keep one suitcase tidy when you repack every few days, and the compression kind leaves room for what you buy there."),
 ("A luggage scale",
  "This is the one we personally use, and we take it on every trip. You will buy things in China, and it is much better to find out what your suitcase weighs in the hotel room than at the check-in desk."),
 ("A small daypack",
  "We have this one too and use it on our trips. It is small and compact, perfect for days out, and it keeps everything organised: tissues, wipes, a water bottle and whatever you pick up on the way."),
 ("A passport and document organiser",
  "You show your passport a lot in China: hotels, train stations, some attractions. Keep it with your printed bookings and copies in one organiser, so you are not digging through a bag at a ticket gate."),
 ("For a winter trip: thermal layers and hand warmers",
  "Our next trip is in December, and winter in much of China is properly cold, with a lot of time spent outdoors in queues and on platforms. A thin thermal set under normal clothes takes less room than a second coat. Air-activated hand warmers are small and need no charging. I could not confirm how airport security inside China treats them, so check with your airline before a domestic flight."),
 ("For a summer trip: a handheld fan",
  "Summer in the big cities is hot and humid. A small rechargeable fan helps in queues. One warning: if your fan can also charge a phone, airport security may treat it as a power bank, and power banks have their own rule on flights inside China. That rule is in the next part of this page."),
 ("Not from Amazon: an eSIM and a VPN",
  "The two things that matter most on arrival are not in a suitcase. Sort your mobile data and a VPN at home, on your own wifi. The ones I use are in <a href=\"#links\">Links for this guide</a> below, and the full story of what went wrong for us the first time is in my <a href=\"/guides/china-travel-apps/\">China travel apps guide</a>."),
]

def _go_cards(items):
    out=""
    for name,why,go,used in items:
        href=go if go.startswith("/go/") else "/go/"+go
        badge='<span class="dbadge booked">We use this</span>' if used else '<span class="dbadge">My pick</span>'
        out+=(f'<div class="amz">{badge}<b>{html.escape(name)}</b><p>{html.escape(why)}</p>'
              f'<a class="btn alt2" href="{href}" rel="sponsored nofollow noopener" target="_blank">See on Amazon</a></div>')
    return '<div class="amzs">'+out+'</div>'

BUY_PICKS={
 1:[("TESSAN universal travel adapter","One universal socket and four USB ports, two of them USB-C. Covers plug types C, G, A and I.","tessan-travel-adapter",False),
    ("LENCENT 65W GaN travel adapter","A stronger option if you charge a laptop: 65W, three USB-C and two USB ports. Types A, C, G and I.","lencent-65w-travel-adapter",False)],
 2:[("INIU USB-C to USB-C cable, 2 pack","Two braided 2 metre cables.","iniu-usb-c-cable",False)],
 3:[("Silicone travel bottles, 4 pack","Refillable 100 ml bottles, sold as leak-proof.","silicone-travel-bottles",False),
    ("Deodorant wipes, 10 sachets","Single wipes that take no space in a day bag.","deodorant-wipes",False),
    ("Travel size solid deodorant","A small 0.5 oz stick.","travel-size-deodorant",False),
    ("Garnier Ambre Solaire SPF 30, 50 ml","A 50 ml sun cream that fits a liquids bag.","travel-sunscreen-spf30",False)],
 4:[("Tampons","This opens a search, so you can pick your own brand and size.","/go/amazon?k=tampons",False)],
 5:[("Paper soap sheets, 10 boxes","500 sheets in small boxes. One box in each bag.","paper-soap-sheets",False),
    ("Carex antibacterial wipes, 10 packs","Ten small packs of 15 wipes.","antibacterial-wipes",False),
    ("Mini wet wipes, 8 packs","Fragrance free, 99% water, small enough for a pocket.","mini-wet-wipes",False)],
 6:[("Disposable toilet seat covers, 60 pack","Flushable paper covers in an XL size.","toilet-seat-covers",False),
    ("Portable travel bidet","USB rechargeable, with a 400 ml bottle.","portable-travel-bidet",False)],
 7:[("Small travel first aid kit, 90 pieces","A compact kit with the basics. Add your own medicines.","travel-first-aid-kit",False),
    ("Empty travel medicine bag","If you would sooner build your own kit from what you already use.","travel-medicine-bag",False)],
 8:[("Sleep mask with earplugs","A contoured mask that blocks light, with earplugs included.","sleep-mask-with-earplugs",False)],
 9:[("Compression packing cubes, 5 set","Compression cubes with a shoe bag.","compression-packing-cubes",False),
    ("Packing cubes, 4 set","A simple set of four in different colours.","packing-cubes-4-set",False)],
 10:[("Digital luggage scale","The one we take on every trip. Weighs up to 50 kg.","luggage-scale",True)],
 11:[("Xiaomi Mi Casual Daypack","The small daypack we use on our trips.","xiaomi-daypack",True)],
 12:[("Passport holder with strap","An RFID blocking family travel wallet for passports, tickets and cards.","passport-holder-with-strap",False),
     ("Passport travel wallet, crossbody","A larger organiser with a crossbody and a wrist strap.","passport-travel-wallet",False)],
 13:[("HotHands hand warmers, 40 pairs","Air activated, up to 10 hours of heat each.","hand-warmers",False),
     ("Men's thermal set","A top and bottom base layer set.","mens-thermal-set",False),
     ("Women's thermal set","This opens a search for now, so you can pick your size and style.","womens-thermal-set",False)],
 14:[("EasyAcc handheld fan","Foldable, USB-C rechargeable, five speeds.","handheld-fan",False)],
}

BUY_EXTRA=(
 '<h2 id="buy-in-china">What to buy in China instead</h2>'
 '<p>These are the things I would leave out of the suitcase and pick up after landing. The first two are practical. The others are what travellers and China guides recommend most often as things worth bringing home. I have not bought all of them myself, so the sources are listed at the bottom.</p>'
 '<h3>A power bank, if you take a flight inside China</h3>'
 '<p>This is the one that catches people. Since 28 June 2025, China\'s aviation authority only allows power banks with a clear <b>3C mark</b> (China Compulsory Certification) on domestic flights. Most power banks sold in Ireland, the UK and on Amazon do not have that mark, even when they were made in China, and security takes them at the gate. The rule is written for domestic flights, but several guides report power banks being checked on international departures from Shanghai and Beijing too.</p>'
 '<p>So if your trip includes a flight inside China, do not buy a power bank before you go. Buy one there with the 3C mark printed on it. It always goes in hand luggage, never in a checked bag. If you only travel by train, the power bank you already have is fine, as the rule is about flights.</p>'
 '<h3>Pocket tissues</h3>'
 '<p>Most packing lists tell you to bring toilet paper. I would not. Every corner shop sells pocket packs for very little, so buy a few on the first day and keep two in your day bag.</p>'
 '<h3>Tea</h3>'
 '<p>Tea is at the top of nearly every list, and it makes sense: it is light, it travels well and the good ones are hard to find at home. Longjing green tea from Hangzhou is the one named most often. Buy it in a sealed tin or bag.</p>'
 '<h3>A silk scarf</h3>'
 '<p>The budget way to bring home silk. A scarf is small, light and easy to give as a present. Hangzhou and Suzhou are the cities known for it.</p>'
 '<h3>A tea set or porcelain cups</h3>'
 '<p>Beautiful, and the hardest thing on this list to get home in one piece. Ask the shop for a padded box and carry it in your hand luggage.</p>'
 '<h3>A name seal</h3>'
 '<p>A small stone stamp, called a chop, carved with your name in Chinese characters while you wait. It is personal, it weighs very little, and it is one of the few souvenirs you cannot order from home.</p>'
 '<h3>Panda things in Chengdu, terracotta warriors in Xi\'an</h3>'
 '<p>Some souvenirs belong to one city. Guides point to the Chengdu panda base for panda gifts and to Xi\'an for small terracotta warrior figures. Both cities are on our December route, so I will update this part with what we actually find.</p>'
 '<h3>Small, cheap and light: chopsticks, knots, fans, phone cases, snacks</h3>'
 '<p>Chopsticks, red Chinese knots and paper fans are the easy presents. Phone cases and cables cost very little in China. And the snack aisle is a souvenir shop of its own: look for flavours you will not see at home, like cucumber crisps.</p>'
 '<h3>What to skip</h3>'
 '<p>A famous brand at a bargain price is probably a copy, so leave those. Guides also advise against buying a phone there, as models, warranties and software can differ from home.</p>'
 '<h2 id="get-it-home">How to get it all home</h2>'
 '<p>Weigh your suitcase before you leave for the airport: the <a href="/go/luggage-scale" rel="sponsored nofollow noopener" target="_blank">luggage scale</a> from number 10 is the reason we have never had a surprise at check-in. Leave some room on the way out, or pack <a href="/go/compression-packing-cubes" rel="sponsored nofollow noopener" target="_blank">compression cubes</a> so the space is there on the way back.</p>'
 '<p>If you would like to shop the way people in China do, my guides to <a href="/guides/taobao-for-foreigners/">ordering on Taobao</a> and <a href="/guides/pinduoduo-for-foreigners/">Pinduoduo in English</a> show how I have parcels sent to our hotels.</p>'
 f'<p class="amzline">The product buttons on this page are my Amazon links. Readers in Ireland go to Amazon.ie and everyone else to Amazon.com. {_B.AMZ_LINE}</p>'
 f'<p><b>{BUY_LINE}</b></p>'
)

_B.STEP_PICKS[BUY_SLUG]={k:_go_cards(v) for k,v in BUY_PICKS.items()}
_B.GUIDE_DEALS[BUY_SLUG]=(["Firsty","NordVPN","ExpressVPN"],"Number 15: the eSIM I use, the VPN I had on our first trip, and a second VPN as a backup. For China, read the plan description first: you want one that routes data outside China.")
_B.HERO_OWN[BUY_SLUG]=(BUY_SLUG+"-cover-16x9","Buy before, or buy in China")
_B.TICK_GUIDES.add(BUY_SLUG)

guide(BUY_SLUG,"What to buy before China, and what to buy there","What to buy before China, and what to buy there",
      "What to buy before you fly to China and what to buy there: adapter, toiletries, a small medical kit, and why your power bank may be better bought in China.",
      "what to buy before going to China",None,
      "<p>Every hotel we stayed in in Shanghai had UK sockets, so the plug adapter I packed never left my bag. I still pack it for every trip. A power bank is the opposite story: it is on every packing list, and it is the one thing I would now buy after landing.</p>"
      "<p>This page is two lists. First, the 15 things worth buying at home before you fly, with the exact products I picked. Then what to leave out of the suitcase and buy in China, from a power bank to tea. Two of the products are ones we own and take on every trip, and they are marked. The others are my picks from Amazon.</p>"
      f"<p>{BUY_LINE} The facts were checked on 12 November 2026 against the sources at the bottom.</p>",
      BUY_STEPS,
      [("What should I buy before going to China?","A plug adapter, the toiletries you want in your own brand (deodorant, sun cream, tampons), soap sheets and wipes, a small medical kit, and an eSIM and a VPN set up at home. The full list of 15 is below."),
       ("Can I bring my power bank to China?","You can bring it into the country. The problem is flights inside China: since 28 June 2025 a power bank needs a clear 3C mark to pass security on a domestic flight, and most power banks sold abroad do not have one. If you fly inside China, buy one there."),
       ("Do I need a plug adapter for China?","With Irish or UK plugs, yes. Standard sockets in mainland China take Type A and Type I plugs. All our Shanghai hotels had UK sockets too, but I would not rely on that everywhere."),
       ("Should I pack toilet paper for China?","I would not. Many public toilets have no paper, but pocket tissue packs are sold in every corner shop. Bring soap sheets and wipes from home and buy the tissues there."),
       ("What is worth buying in China?","Tea, a silk scarf, a carved name seal and small local gifts are what guides recommend most. And, for practical reasons, a power bank with the 3C mark and pocket tissues.")],
      [("Shanghai municipal government: check your power bank before boarding a plane","https://english.shanghai.gov.cn/en-MobileAndInternet/20250807/163f513d5ed343efb1932932cad43a68.html",True),
       ("Shanghai municipal government: items you may need during your stay in China (plug types)","https://english.shanghai.gov.cn/en-FAQs-StudyinShanghai/20250924/e961a223e45a4adca7969b3f7691132b.html",True),
       ("South China Morning Post: China's power bank crackdown, 6 preflight answers","https://www.scmp.com/economy/china-economy/article/3316836/chinas-power-bank-crackdown-6-preflight-answers-wary-travellers",False),
       ("Trip.com: China power bank limits on flights (14 April 2026)","https://in.trip.com/guide/info/china-power-bank-limit.html",False),
       ("China Discovery: China power bank rules and 3C certification","https://www.chinadiscovery.com/articles/china-power-bank-rules-3c-certification-guide.html",False),
       ("The Helpful Panda: China packing list","https://thehelpfulpanda.com/china-packing-list",False),
       ("The Helpful Panda: best souvenirs to buy in China","https://thehelpfulpanda.com/best-souvenirs-to-buy-in-china/",False),
       ("Chinavigators: best souvenirs from China","https://www.chinavigators.com/best-souvenirs-china/",False),
       ("Holafly: 20 best Chinese souvenirs (6 June 2026)","https://esim.holafly.com/travel-tips/chinese-souvenirs/",False),
       ("Travel of China: top 24 China souvenirs","https://www.travelofchina.com/top-24-china-souvenirs-to-buy-2025-travel-gift-guide/",False),
       ("Trip.com: best things to buy in China","https://uk.trip.com/guide/shopping/what-to-buy-in-china.html",False),
       ("China Highlights: shopping in China","https://chinahighlights.com/travelguide/guidebook/shopping.htm",False)],
      SITE+"/og/"+BUY_SLUG+".jpg",checked="2026-11-12",published="2026-11-12",vschema=False,
      steps_title="15 things to buy before you fly",
      extra=BUY_EXTRA,
      related=[("/guides/china-dos-and-donts/","china-will-take-your-drone-15-dos-and-donts","15 RULES","China do's and don'ts: what not to bring, and what not to do"),("/guides/china-before-you-fly-checklist/","china-before-you-fly-10-things-cover-16x9","10 THINGS","China first trip checklist: safety and backups"),("/guides/taobao-for-foreigners/","how-to-order-on-taobao-step-by-step-guide-cover","SHOPPING","How to order on Taobao as a foreigner, step by step"),("/guides/first-time-in-china/","first-time-in-china-13-things-before-you-fly","GUIDE 13","First time in China: 13 things to set up before you fly")])
