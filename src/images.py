# IMAGE REGISTRY. Every image used on the site must be listed here (build.py stops if one is missing).
# key = path under docs/img/ ; alt = what the image shows (the same alt is used on every page) ; cap = optional visible caption
# Rules: describe what is really in the picture (and any text in it), 15 to 140 characters, no "image of", no keyword stuffing.
# File names: lowercase words joined by hyphens that say what the picture is, never IMG_0001, slide-3, s2, 1.jpg.
R={}
def a(k,alt,cap=None): R[k]=dict(alt=alt,cap=cap)
a("china-travel-apps-12-apps-to-set-up-before-china.jpg","Cover: 12 apps to set up before China, with the chips Alipay, Amap, 12306 and eSIM, a phone showing a lit Shanghai street and a Chinese flag sticker")
a("china-arrival-card-in-alipay-step-by-step.jpg","Cover: the number 14, the China arrival card in Alipay step by step, with a passport, a plane and a red arrival card stamp")
a("china-arrival-card-on-a-pc-step-by-step.jpg","Cover: the number 14, the China arrival card on a PC step by step, with a passport, a plane and a red arrival card stamp")
a("china-arrival-card-on-a-pc-vertical.jpg","Vertical cover: the China arrival card on a PC, step by step")
a("the-bund-shanghai-after-dark-cover-4x5.jpg","Two gold-lit historic buildings on the Bund in Shanghai at night, one with a green pointed roof, under the title The Bund after dark")
a("the-bund-shanghai-after-dark-cover-3x4.jpg","Two gold-lit historic buildings on the Bund in Shanghai at night, one with a green pointed roof, under the title The Bund after dark")
a("the-bund-shanghai-52-historic-buildings-slide.jpg","Bund carousel slide 2: lit historic buildings above a crowd, with the text 52 historic buildings in many styles and 1.6 km of Huangpu riverbank","Slide 2: 52 historic buildings along 1.6 km of riverbank")
a("the-bund-shanghai-mix-of-architecture-styles-slide.jpg","Bund carousel slide 3: a lit Bund building under the words A mix of styles, with chips for Romanesque, Gothic, Baroque, Neo-Classical, Beaux-Arts and Art Deco","Slide 3: a mix of architecture styles")
a("pudong-oriental-pearl-tower-468-metres-slide.jpg","Bund carousel slide 4: the Oriental Pearl Tower lit pink across the river with a badge reading 468 metres and the text Pudong lights up too","Slide 4: the Oriental Pearl Tower, 468 metres")
a("the-bund-save-it-for-your-trip-slide.jpg","Bund carousel slide 5: the Oriental Pearl Tower lit red and blue, with the text Save it for your trip and @scratchandroam","Slide 5: save it for your trip")
a("shanghai-at-night-film-strip-cover-4x5.jpg","A gold-lit Bund building on a film strip with sprocket holes, labelled Roll 01 Shanghai")
a("shanghai-at-night-film-strip-cover-3x4.jpg","A gold-lit Bund building on a film strip with sprocket holes, labelled Roll 01 Shanghai")
a("huangpu-river-night-cruise-from-the-water-cover-4x5.jpg","The Shanghai Tower and Pudong skyline lit at night, seen from the Huangpu river, under the title From the water, Shanghai lit up")
a("huangpu-river-night-cruise-from-the-water-cover-3x4.jpg","The Shanghai Tower and Pudong skyline lit at night, seen from the Huangpu river, under the title From the water, Shanghai lit up")
a("huangpu-river-light-show-times-slide.jpg","Huangpu river carousel slide 2: the lit skyline over the water, with light show times of about 6 pm in winter and 7 pm in summer, lasting 15 to 20 minutes","Slide 2: light show times")
a("huangpu-river-same-river-new-angle-slide.jpg","Huangpu river carousel slide 3: two phone photos of the lit skyline reflected in the water, with the text Same river, new angle every minute","Slide 3: a new angle every minute")
a("huangpu-river-bund-side-and-pudong-side-slide.jpg","Huangpu river carousel slide 4: the lit skyline with notes on the Bund side, for unobstructed views, and the Pudong side, for Shanghai Tower up close","Slide 4: the Bund side and the Pudong side")
a("huangpu-river-take-the-cruise-slide.jpg","Huangpu river carousel slide 5: the lit Pudong skyline over the water, with the text Take the cruise and @scratchandroam","Slide 5: take the cruise")
a("nanjing-road-shanghai-neon-shop-fronts-cover-4x5.jpg","Two photos of lit shop fronts on Nanjing Road in Shanghai on a pink background, with the title Nanjing Road and the line Shop. Glow. Repeat.")
a("nanjing-road-shanghai-neon-shop-fronts-cover-3x4.jpg","Two photos of lit shop fronts on Nanjing Road in Shanghai on a pink background, with the title Nanjing Road and the line Shop. Glow. Repeat.")
a("nanjing-road-day-mood-night-mood-slide.jpg","Nanjing Road carousel slide 2: two photos of the street, one by day and one by night, under the words Day mood. Night mood.","Slide 2: day mood, night mood")
a("nanjing-road-1-2-km-pedestrian-street-slide.jpg","Nanjing Road carousel slide 3: two night photos of the lit street with the text 1.2 km of pedestrian street and the label He'nan Rd to Xizang Rd","Slide 3: 1.2 km of pedestrian street")
a("nanjing-road-cute-stop-shanghai-in-chocolate-slide.jpg","Nanjing Road carousel slide 4: photos of cartoon figures in a shop display and a chocolate treat, with the text Cute stop and the label Shanghai in chocolate","Slide 4: a cute stop")
a("nanjing-road-come-roam-with-me-slide.jpg","Nanjing Road carousel slide 5: a busy street corner with shop signs, with the text Come roam with me and @scratchandroam","Slide 5: come roam with me")
a("shanghai-circus-world-full-show-cover.jpg","Cover: aerial silk performers on a green-lit stage, with the title Full show Shanghai Circus World")
a("shanghai-circus-world-photo-dump-cover.jpg","Cover: a performer on a glowing round platform, with the title Photo dump Shanghai Circus")
a("shanghai-circus-world-act-1-aerial-silks.jpg","Act 1, aerial silks: performers hanging from silk ribbons above a green-lit stage at Shanghai Circus World","Act 1: aerial silks")
a("shanghai-circus-world-act-2-hand-balance.jpg","Act 2, hand balance: a performer upside down on one hand on a round platform at Shanghai Circus World","Act 2: hand balance")
a("shanghai-circus-world-act-3-laser-lights.jpg","Act 3, laser lights: performers on a stage under laser beams with the audience behind, at Shanghai Circus World","Act 3: laser lights")
a("shanghai-circus-world-act-4-aerial-hoop.jpg","Act 4, aerial hoop: a performer in a lit hoop hanging from a rope in a yellow spotlight at Shanghai Circus World","Act 4: aerial hoop")
a("shanghai-circus-world-act-5-the-sphere.jpg","Act 5, the sphere: a large steel mesh globe lit blue on the stage at Shanghai Circus World","Act 5: the sphere")
a("china-will-take-your-drone-15-dos-and-donts.jpg","Cover: China will take your drone, 15 do's and don'ts, with a drone on an airport X-ray screen stamped confiscated")
a("china-dos-and-donts-carousel-1-china-will-take-your-drone.jpg","Carousel slide 1: China will take your drone, 15 do's and don'ts, with a drone on an X-ray screen stamped confiscated")
a("china-dos-and-donts-carousel-2-customs-will-take-it.jpg","Carousel slide 2: customs will take it, fruit, meat and dairy, sensitive media, and a drone in Beijing")
a("china-dos-and-donts-carousel-3-security-will-take-it.jpg","Carousel slide 3: security will take it, a power bank with no 3C mark, lighters and matches, cold medicine like Sudafed, and cash over 20,000 yuan")
a("china-dos-and-donts-carousel-4-dont-do-this.jpg","Carousel slide 4: don't do this, chopsticks upright in rice, tapping your bowl, touching heads, and drinking tap water")
a("china-dos-and-donts-carousel-5-do-this-instead.jpg","Carousel slide 5: do this instead, bring a plug adapter, bring deodorant, SPF and tampons, buy tissues there, and check the date is not expired")
a("first-time-in-china-13-things-before-you-fly.jpg","Cover: 13 things before China, with a card saying 200 yuan is the number that matters")
a("first-time-in-china-13-things-before-you-fly-vertical.jpg","Vertical cover: 13 things before China")
a("how-to-order-on-taobao-step-by-step-guide-cover.jpg","Cover: Order on Taobao, a full step by step guide, with a phone showing the Taobao app")
a("natali-portrait-at-her-desk.jpg","Natali, the author, taking a selfie at her desk with shelves, plants and a printer behind her")
for n,t in {"apple":"an apple","books":"a stack of books","drone":"a drone","power-bank":"a power bank","lighter-flame":"a flame for lighters and matches","cold-medicine-capsule":"a cold medicine capsule","euro-cash-bundle":"a bundle of euro notes","rice-bowl-with-chopsticks":"a rice bowl with chopsticks standing upright","chopsticks":"a pair of chopsticks","head-massage":"a person having a head massage","tap-water-glass":"a tap filling a glass","travel-plug":"a travel plug","lotion-bottle":"a lotion bottle","toilet-roll":"a toilet roll","tin-can":"a tin can"}.items():
    a(f"dd/china-customs-xray-icon-{n}.png",f"Icon of {t} in an airport X-ray scanner frame")
# Taobao screenshots from Natali's own phone. The app is in Chinese, the English labels were added by Natali.
T={
"taobao-app-my-taobao-tab-and-settings-gear-english-labels":("Taobao app My Taobao page with English labels added: My Taobao is the bottom right tab and Settings is the gear at the top right","Tap My Taobao (我的淘宝) at the bottom right, then the gear for Settings (设置)."),
"taobao-settings-country-language-currency-english-label":("Taobao Settings page with an English label on the row Country, Language and Currency (国家与地区/语言/货币)","The row to tap: country, language and currency (国家与地区/语言/货币)."),
"taobao-settings-delivery-address-english-label":("Taobao Settings page with an English label on the Delivery address row (收货地址)","Delivery address (收货地址) lives in Settings too."),
"taobao-language-country-currency-page-english-labels":("Taobao country, language and currency page with English labels on Country / region, Language and Currency, the language shown is Chinese","On my account the only language on offer was Chinese (中文)."),
"taobao-currency-list-pick-euro-english-label":("Taobao currency list with an English label pointing at EUR, the euro, in the list of payment currencies (支付币种)","Payment currency (支付币种): pick EUR."),
"taobao-euro-estimate-under-every-price-english-label":("Taobao home feed with an English label saying a euro estimate sits under every yuan price","After switching to euro, a small ≈€ estimate sits under each yuan price."),
"taobao-search-bar-english-label":("Taobao search page with an English label on the search bar at the top","The search bar (搜索) at the top."),
"taobao-search-type-in-english-labels":("Taobao search with the English words phone case typed in, labelled Type it in English and Search","Typing phone case in English worked for me."),
"taobao-add-new-address-button-english-label":("Taobao delivery address page with no addresses yet and an English label on the Add new address button (添加收货地址)","No address yet: tap Add new address (添加收货地址)."),
"taobao-address-form-full-address-and-door-number-english-label":("Taobao address form with an English label on the field for the full address and door number (详细地址与门牌号)","Full address and door number (详细地址与门牌号)."),
"taobao-address-form-recipient-name-and-phone-english-labels":("Taobao address form with English labels on the recipient name (收货人名字) and phone number (手机号) fields","Recipient name (收货人名字) and phone number (手机号)."),
"taobao-product-options-phone-model-colour-add-to-cart-english-labels":("Taobao product options with English labels on Phone model, Colour and the Add to cart button (加入购物车)","Choose the phone model (适用手机型号) and colour (颜色分类), then Add to cart (加入购物车)."),
"taobao-product-page-favourite-star-english-label":("Taobao product page with an English label on the favourite star (收藏) at the bottom","The star (收藏) saves it to your favourites."),
"taobao-cart-tick-items-and-checkout-english-labels":("Taobao cart with English labels on the tick box for items and the Checkout button (结算)","Tick your items (勾选), then Checkout (结算)."),
"taobao-checkout-popup-set-delivery-address-first-english-label":("Taobao checkout pop-up in Chinese with an English label saying Set your delivery address first (请先设置收货地址)","The pop-up that stops you at checkout without an address (请先设置收货地址)."),
"taobao-my-orders-to-pay-to-ship-to-receive-refunds-english-labels":("Taobao My Taobao page with English labels on My orders and its rows To pay, To ship, To receive and Refunds","My orders (我的订单): to pay, to ship, to receive, refunds."),
}
for k,(alt,cap) in T.items(): a(k+".jpg",alt,cap)
a("china-visa-free-30-days-departure-board-cover-4x5.jpg","Aerial view of misty mountains behind a departure board reading China, visa free, to 31 Dec, with chips 30 days and IE UK EU and a China flag sticker")
a("china-visa-free-30-days-departure-board-cover-3x4.jpg","Aerial view of misty mountains behind a departure board reading China, visa free, to 31 Dec, with chips 30 days and IE UK EU and a China flag sticker")
a("china-visa-free-30-days-departure-board-cover-16x9.jpg","Hangzhou light show at night beside a departure board reading China, visa free, to 31 Dec, with chips 30 days and IE UK EU and a China flag")
a("china-visa-free-30-days-who-can-board-slide.jpg","Carousel slide 2: a departure board with Ireland OK, UK OK, EU 25 of 27 OK and CZ, LT NO, over a station hall photo","Who can board: Ireland, UK and 25 of 27 EU countries")
a("china-visa-free-30-days-time-left-slide.jpg","Carousel slide 3: a departure board reading visa free until, ends 31 Dec 2026, 24:00 Beijing time, 2027 not announced, over a light show photo","Time left: ends 31 December 2026, 2027 not announced")
a("china-visa-free-30-days-at-the-desk-slide.jpg","Carousel slide 4: a departure board with passport 6 months, arrival card free, official site only and ticket plus hotel proof, over a delta coast photo","At the desk: passport, arrival card, proof of trip")
a("china-visa-free-30-days-changes-slide.jpg","Carousel slide 5: a departure board with extend NO, leave and return OK, longer stay visa, over an old street photo","What you cannot change: no extension, return allowed")
a("china-visa-free-30-days-last-call-slide.jpg","Carousel slide 6: a departure board reading save this, before 31 Dec, send to a friend, follow for updates, over a tower photo","Last call: save this before 31 December")

# Alt text for the social share images in docs/og/ (1200x630, one per guide)
a("top-25-china-apps-boarding-pass-cover.jpg","Cover: Top 25 China apps on a dark teal background, with an Access Denied stamp and three boarding passes for Alipay, Amap and Hellobike")
a("top-25-china-apps-short-frame-alipay-pass-critical-gate-01.jpg","Frame from the Short: the Alipay boarding pass, gate 01, class critical, 5 of 5, with the red stamp You struggle to pay for almost anything")
a("top-25-china-apps-short-frame-amap-pass-critical-gate-05.jpg","Frame from the Short: the Amap boarding pass, gate 05, class critical, with the red stamp Wrong pins and the wrong metro exit")
a("top-25-china-apps-short-frame-taobao-pass-handy-gate-16.jpg","Frame from the Short: the Taobao boarding pass, gate 16, class handy, 2 of 5, with the red stamp Missing the tiny prices")
a("top-25-china-apps-short-frame-boarding-complete-checklist-of-25-apps.jpg","Frame from the Short: Boarding complete, a checklist of all 25 apps ticked, and a button reading send it to your travel buddy")
a("china-before-you-fly-10-things-cover-16x9.jpg","Cover: 10 steps before China with the chips eSIM, VPN and insurance, the Shanghai skyline lit at night and a China flag sticker")
a("alipay-metro-qr-code-china-cover-16x9.jpg","Cover: Metro QR in China with the chips Alipay, Metro and Bus, the line set it up before you travel, a phone showing the Alipay Transport screen and a China flag sticker")
a("alipay-home-screen-with-transport-icon-and-quick-tutorial-caption.jpg","Alipay home screen on a phone with the Transport icon in the top row next to Scan, Pay/Receive and Pocket","Transport is in the top row of the Alipay home screen.")
a("alipay-select-city-list-with-chengdu-highlighted-for-metro-qr.jpg","Alipay Select city list with the recent cities and the popular cities, including Chengdu, Xi'an and Shanghai","Pick the city you are going to.")
a("alipay-transport-tab-tap-bus-and-metro-icon-for-xian.jpg","Alipay Transport tab for Xi'an with the BusMetro icon first in the row, next to Taxi, Fuel, 12306 and Flight","After picking the city, the BusMetro icon shows up.")
a("alipay-obtain-metro-card-agree-and-obtain-card-button-xian.jpg","Alipay Obtain card to take Metro screen for Xi'an with the blue Agree and obtain card button and the options Swipe to ride, Free card and Travel assistant","Agree and obtain card. The card is free.")
a("alipay-payment-password-notice-for-claiming-metro-qr-card.jpg","Black screen with a paper notice reading Enter your Alipay payment password, the one you set up for payments, above six dots","The password screen goes black on a recording, so this notice stands in for it.")
a("alipay-metro-card-collected-successfully-use-now-button.jpg","Alipay screen reading Card collected successfully with a blue Use now button and the line Take Metro and get green energy","Card collected. Tap Use now to open your QR code.")
a("alipay-wrong-qr-code-switch-city-top-left-notice.jpg","Alipay home screen for Xi'an with a notice reading Wrong QR code? Switch the city top left to switch your QR code","Wrong QR code? Switch the city at the top left.")

OGALT={
"china-visa-free-30-days.jpg":R["china-visa-free-30-days-departure-board-cover-16x9.jpg"]["alt"],
"china-arrival-card-in-alipay.jpg":R["china-arrival-card-in-alipay-step-by-step.jpg"]["alt"],
"china-arrival-card-on-a-pc.jpg":R["china-arrival-card-on-a-pc-step-by-step.jpg"]["alt"],
"the-bund-shanghai-at-night.jpg":"Gold-lit historic buildings on the Bund in Shanghai at night, with the title The Bund",
"china-dos-and-donts.jpg":R["china-will-take-your-drone-15-dos-and-donts.jpg"]["alt"],
"china-travel-apps.jpg":R["china-travel-apps-12-apps-to-set-up-before-china.jpg"]["alt"],
"shanghai-circus-world-photo-dump.jpg":R["shanghai-circus-world-photo-dump-cover.jpg"]["alt"],
"shanghai-circus-world-era-show.jpg":R["shanghai-circus-world-full-show-cover.jpg"]["alt"],
"first-time-in-china-13-things.jpg":R["first-time-in-china-13-things-before-you-fly.jpg"]["alt"],
"nanjing-road-shanghai.jpg":"Two close photos of lit shop fronts on Nanjing Road in Shanghai on a pink background",
"huangpu-river-night-cruise.jpg":"Pudong towers lit at night seen from the Huangpu river, with the words Huangpu River night cruise",
"top-25-china-apps.jpg":R["top-25-china-apps-boarding-pass-cover.jpg"]["alt"],
"taobao-for-foreigners.jpg":R["how-to-order-on-taobao-step-by-step-guide-cover.jpg"]["alt"],
"alipay-metro-qr-code-china.jpg":R["alipay-metro-qr-code-china-cover-16x9.jpg"]["alt"],
"china-before-you-fly-checklist.jpg":R["china-before-you-fly-10-things-cover-16x9.jpg"]["alt"],
}

# ---- Build spice tolerance before China (SR-0045) ----
a("build-spice-tolerance-before-china-cover-16x9.jpg","Cover: the title Spice tolerance before China in white and orange on a dark ember background, a heat bar, a hot-faced emoji, a chilli, a glass of milk and a China flag sticker")
a("spice-tolerance-china-can-you-handle-chongqing-hotpot-slide.jpg","Slide 1: Can you handle Chongqing hotpot, with a heat bar filling from mild to Chongqing and a hot-faced emoji at the end","Slide 1: can you handle Chongqing hotpot?")
a("spice-tolerance-china-mala-two-sensations-and-three-rules-slide.jpg","Slide 2: the characters 麻 má numbing and 辣 là burning joined into 麻辣 málà, with three rules: start small, repeat often, step up slowly","Slide 2: two sensations, three rules")
a("spice-tolerance-china-six-week-plan-ladder-slide.jpg","Slide 3: a six step ladder from W1 chilli flakes to W6 a mild mala dish, in bars that change from yellow to red","Slide 3: the six week ladder")
a("spice-tolerance-china-cool-it-down-foods-slide.jpg","Slide 4: six foods that cool the burn, milk, rice, lemon or lime, vinegar or pickles, honey and coconut milk, and a red box saying not water","Slide 4: cool it down, and not with water")
a("spice-tolerance-china-order-like-a-pro-slide.jpg","Slide 5: four ways to order spice in Chinese, 不辣, 微辣, 中辣 and 鸳鸯锅, with a START MILD stamp","Slide 5: order like a pro")
OGALT["build-spice-tolerance-before-china.jpg"]=R["build-spice-tolerance-before-china-cover-16x9.jpg"]["alt"]
# ---- How to order food in China without speaking Chinese (SR-0046) ----
a("order-food-in-china-without-speaking-chinese-cover-16x9.jpg","Cover: the title Order food in China, no Chinese needed, over a steamed bun stall, with the phrase 我要这个 and a China flag sticker")
a("order-food-china-ordering-without-chinese-hook-slide.jpg","Slide 1: Order food, no Chinese needed, under the glowing neon sign of Sijing Night Market in Shanghai","Slide 1: order food, no Chinese needed")
a("order-food-china-say-i-want-we-want-can-we-have-slide.jpg","Slide 2: a steamed bun stall worker, with the phrases 我要这个 I want, 我们要这个 we want and 可以给我们这个吗 can we have","Slide 2: I want, we want, can we have")
a("order-food-china-count-one-to-five-slide.jpg","Slide 3: the neon welcome sign of Sijing Night Market above the numbers 一 二 三 四 五 and the counting phrases one of this, two of that","Slide 3: numbers one to five")
a("order-food-china-ask-the-price-and-take-away-slide.jpg","Slide 4: the rainbow-lit arch at Sijing Night Market in Shanghai with the phrases 多少钱 how much and 打包 dǎbāo, to go","Slide 4: how much, and to go")
a("order-food-china-say-please-and-thank-you-slide.jpg","Slide 5: neon signs at Sijing Night Market with the phrases 请 please, 谢谢 thank you and 麻烦你 a softer please","Slide 5: please and thank you")
a("order-food-china-pay-with-qr-or-cash-slide.jpg","Slide 6: a lit shopping street at night with two ways to pay, scan the stall QR code or small cash notes","Slide 6: scan or pay cash")
a("order-food-china-scan-to-order-menus-slide.jpg","Slide 7: pan-fried buns with the phrase 扫码点餐 sǎomǎ diǎncān, scan to order, and a note about WeChat and Alipay","Slide 7: scan-to-order menus")
a("order-food-china-how-to-read-pinyin-and-tones-slide.jpg","Slide 8: how to read pinyin, with the letters q x zh c and the four tone marks and what they sound like","Slide 8: how to read pinyin")
a("order-food-china-save-this-phrase-list-slide.jpg","Slide 9: Save this, a list of the Chinese phrases from the guide, from 我要这个 to 扫码点餐","Slide 9: save this phrase list")
OGALT["order-food-in-china-without-speaking-chinese.jpg"]=R["order-food-in-china-without-speaking-chinese-cover-16x9.jpg"]["alt"]

# clean photos from the China folder, no text on them (27 Oct 2026)
a("the-bund-peace-hotel-green-roofs-lit-at-night.jpg","The green-roofed Peace Hotel and the tower beside it on the Bund in Shanghai, lit gold at night with a crowd below")
a("the-bund-gold-lit-historic-buildings-at-night.jpg","Gold-lit historic buildings on the Bund in Shanghai at night")
a("the-bund-oriental-pearl-tower-from-the-promenade.jpg","The Oriental Pearl Tower lit up across the Huangpu river, seen from the Bund promenade at night")
a("the-bund-pudong-skyline-and-shanghai-tower-at-night.jpg","Shanghai Tower and the Pudong skyline lit in blue and purple, seen from the Bund at night")
a("the-bund-pink-lit-pearl-tower-over-the-crowd.jpg","The Oriental Pearl Tower lit pink above the crowd on the Bund at night")
a("nanjing-road-pedestrian-street-gold-lit-facades.jpg","Shoppers walking down pedestrian Nanjing Road at night between gold-lit old buildings")
a("nanjing-road-clock-tower-and-neon-at-night.jpg","A lit clock tower and neon signs above the crowd on Nanjing Road at night")
a("nanjing-road-curved-corner-building-neon-lights.jpg","A curved corner building on Nanjing Road lit gold and red under a large glowing sign at night")
a("nanjing-road-red-traffic-lights-and-shoppers-at-night.jpg","Nanjing Road at night with red traffic lights, people crossing and a tall tower behind")
a("nanjing-road-shopping-street-at-dusk-with-big-screen.jpg","Nanjing Road shopping street at dusk with shop signs, a big screen and people walking")
a("huangpu-river-shanghai-tower-reflected-in-the-water.jpg","Shanghai Tower and the Pudong skyline lit at night, reflected in the Huangpu river")
a("huangpu-river-pudong-towers-lit-red-and-pink-at-night.jpg","Pudong towers lit in red and pink over the dark Huangpu river at night")
a("huangpu-river-pudong-skyline-with-gold-reflections.jpg","The Pudong skyline across the Huangpu river with gold and pink reflections on the water")
a("huangpu-river-lujiazui-skyline-wide-night-view.jpg","Wide night view of the Lujiazui skyline and Shanghai Tower across the Huangpu river")
a("huangpu-river-blue-lit-towers-from-the-water.jpg","Blue and gold lit towers on the Pudong bank seen from the Huangpu river at night")
