# Travelling to China from Ireland (1 Nov 2026). Written after Natali asked for a post from TheJournal.ie / Embassy of China in Ireland article.
# RULE: only things Natali told us happened. Facts from the article and the RTE piece are marked as sourced, not as her experience.
# The article is sponsored by the Embassy of China in Ireland, so it is labelled that way and used for the embassy's own claims only.
def _fi(k,w=""):
    return f'<figure{w}><a href="/img/{k}.jpg"><img src="/img/{k}.jpg" alt="" loading="lazy"></a><figcaption>{html.escape(IMGREG[k+".jpg"]["cap"])}</figcaption></figure>'
def _wide(col,tall):
    return '<div class="shots wideshots"><div class="col">'+"".join(_fi(k) for k in col)+'</div>'+_fi(tall,' class="tall"')+'</div>'
def _two(a,b):
    return '<div class="shots wideshots"><div class="col">'+_fi(a)+'</div><div class="col">'+_fi(b)+'</div></div>'

IE_STEPS=[
 ("Check the entry rules for your own passport",
  "Right now ordinary passports from Ireland, the UK and most EU countries can enter China without a visa for up to 30 days, for tourism, business, visiting family or friends, exchanges or transit. The policy runs until 24:00 Beijing time on 31 December 2026, and nothing has been announced for 2027. I keep the details, the border documents and the date maths on one page: <a href=\"/guides/china-visa-free-30-days/\">China visa free for 30 days</a>. Open the embassy page linked there once more before you fly, because this is the part that can change."),
 ("Pick your route: nonstop or a change of planes",
  "China Eastern started a nonstop Dublin to Shanghai flight in July 2026, three times a week on an Airbus A350-900 (RTE, 20 July 2026). The embassy article also mentions nonstop flights to Beijing and puts the flight at about 10 hours in the air. I could not confirm Beijing myself, so check the airline site for days and times. I have not flown the nonstop yet. I have flown to Shanghai with a change in London, and with a change in Helsinki, and in December we fly Cork, London, Chengdu. When you compare fares, look at the full price per person with seats and bags added, because the first price you see often leaves them out. I am not quoting fares here, since they change every day."),
 ("Fill in the free arrival card before you fly",
  "China has a free online arrival card, and it should only be filled in on official channels. Paid copycat sites exist. I have both versions with every screen: <a href=\"/guides/china-arrival-card-alipay/\">in Alipay on your phone</a> and <a href=\"/guides/china-arrival-card-pc/\">on a computer</a>."),
 ("Sort your phone and your VPN before you leave home",
  "This is where our first trip went wrong. My eSIM was ready and I forgot to switch it on before we landed, so we bought Chinese SIM cards at the airport, which I would not do again. I also had only one VPN, and it needed wifi to activate again. Our hotel concierge shared LetsVPN and that got us back online. Install your eSIM at home, switch it on before you land, and have a second VPN as a backup. I use Firsty for eSIMs in Japan and Saudi Arabia and plan to use it in China in December, and my code is in the links box below. The full list of apps, with the steps, is in the <a href=\"/guides/china-travel-apps/\">China travel apps guide</a>."),
 ("Set up Alipay and WeChat Pay at home",
  "The embassy article says Visa and Mastercard are accepted at almost every major shopping centre and that the payment apps are handy in smaller shops. I have both apps linked to my foreign card, and I have written each one step by step: <a href=\"/guides/alipay-add-foreign-card-china/\">add a card to Alipay</a>, <a href=\"/guides/wechat-pay-add-foreign-card-china/\">add a card to WeChat Pay</a>, and <a href=\"/guides/alipay-vs-wechat-pay-china/\">which one I used for what</a>."),
 ("Plan the way from the airport to your hotel",
  "On one trip I flew into Pudong and took the maglev to Longyang Road, which takes about 8 minutes, then Line 2 of the metro towards Lujiazui, and walked about 10 minutes to the hotel. The listed maglev ticket price was ¥50, so check it before you go. If you would rather not do that after a long flight, you can book a transfer in advance. I have not used the transfer sites below, so they are links only. The metro is easy once your Alipay <a href=\"/guides/alipay-metro-qr-code-china/\">metro QR code</a> is set up."),
 ("Book trains in an app you have already tested",
  "High-speed trains connect the big cities, and for December we will use them between Chengdu, Chongqing and Xi'an. I could not get through the 12306 registration in the Alipay version, so I booked all our train tickets on Trip.com and paid a small fee. If you want to use 12306 itself, download the real app from the App Store or Google Play."),
 ("Pack for the sockets and leave space in the case",
  "Irish plugs are the same type as UK ones. In every hotel I stayed in in Shanghai there were UK sockets too, so I never needed an adapter there, but I always carry one in case a hotel is different. I also order a lot on Taobao and send it to the hotel: I have ordered tens of parcels to hotels and none were lost, so leave room for the trip home. The <a href=\"/guides/taobao-for-foreigners/\">Taobao guide</a> shows how, and the <a href=\"/guides/china-dos-and-donts/\">do's and don'ts</a> shows what to leave at home."),
]

IE_FAQ=[
 ("Do I need a visa to travel to China from Ireland?","With an ordinary Irish passport you can currently enter visa free for up to 30 days, for tourism, business, visiting family or friends, exchanges or transit. The policy runs until 24:00 Beijing time on 31 December 2026 and nothing is announced for 2027. Check the embassy page before you book."),
 ("Is there a direct flight from Ireland to China?","Yes to Shanghai. RTE reported on 20 July 2026 that China Eastern has started a nonstop Dublin to Shanghai service on an Airbus A350-900, three times a week. The embassy article also says there are nonstop flights to Beijing, which I could not confirm. From Cork I would change planes, and so far I have changed in London and in Helsinki."),
 ("How long is the flight from Ireland to China?","The embassy article says about 10 hours in the air on the nonstop. With a change, the total depends on the connection, so compare the full journey time and not just the flying time."),
 ("Can I use my Irish bank card in China?","The embassy article says Visa and Mastercard are accepted at almost every major shopping centre. I use Alipay and WeChat Pay with my foreign card, and I link both guides above. I would not rely on one way to pay."),
 ("Do I need a plug adapter for China?","China uses Type A and Type I sockets. The hotels I stayed in in Shanghai also had UK sockets, so I did not need an adapter there, but I always pack one. Your hotel may be different."),
 ("Can I get tax back on shopping in China?","The embassy article says more than 13,000 stores take part in tax refunds for overseas visitors, either at the till or when you leave. I have not tried it, so I link the official tax-free site in the sources."),
 ("How much do hotels cost?","The embassy article says a five-star hotel can often be had for around €100 a night, and about €50 in smaller cities. That is the embassy's figure, not mine, and prices change by city and season. My own stays are on the <a href=\"/guides/ihg-hotels-china-shanghai-hangzhou-review/\">IHG hotels page</a>."),
]

IE_SOURCES=[
 ("Embassy of China in Ireland: FAQ on visa-free entry","https://ie.china-embassy.gov.cn/eng/qzfw/202412/t20241219_11506444.htm",True),
 ("Embassy of China in Ireland: notice on extending the unilateral visa-free policy (4 Nov 2025)","https://ie.china-embassy.gov.cn/eng/qzfw/202511/t20251104_11746287.htm",True),
 ("China tax-free shopping for overseas visitors (official)","https://taxfree.mofcom.gov.cn/taxfreeEnPc/index.html",True),
 ("TheJournal.ie: Beyond Visa-Free, sponsored by the Embassy of China in Ireland (23 Oct 2026)","https://www.thejournal.ie/travelling-to-china-from-ireland-7203152-Oct2026/",False),
 ("RTE: New route from Dublin Airport to Shanghai takes off (20 July 2026)","https://www.rte.ie/news/business/2026/0720/1584141-new-china-route-from-dublin-airport/",False),
]

IE_EXTRA=(
 '<h2 id="shanghai">Shanghai: where I start</h2>'
 '<p>Shanghai is the city I know best. In December 2025 we spent Christmas at Disneyland Shanghai, then New Year and the day after on the Bund and Nanjing Road, and I call it the best decision ever. On the Bund at New Year we usually went after 8pm, which is when it is crowded, and the city light show was lovely from our river cruise. I booked the <a href="https://klook.tpm.li/W4dyROGI" rel="sponsored noopener" target="_blank">cruise on Klook</a>.</p>'
 +_wide(["pudong-skyline-and-oriental-pearl-tower-from-the-shanghai-sightseeing-bus","shanghai-steel-bridge-seen-from-the-front-of-the-sightseeing-bus"],"shanghai-disneyland-castle-lit-pink-and-blue-at-night")+
 '<p>My Shanghai tips: take a daytime sightseeing bus (the <a href="https://klook.tpm.li/ho7P5Di3" rel="sponsored noopener" target="_blank">Big Bus on Klook</a> is the same one we rode), see the Bund from the Pudong side, and go up the Jin Mao Tower for a view without paying for the expensive decks. The <a href="https://klook.tpm.li/AXPosEZw" rel="sponsored noopener" target="_blank">Jin Mao tickets are on Klook</a>. We also booked the ERA circus show on <a href="https://klook.tpm.li/YtyjQpDu" rel="sponsored noopener" target="_blank">Klook</a>.</p>'
 +_wide(["jin-mao-tower-deck-view-of-the-huangpu-river-and-pearl-tower","shanghai-temple-with-gold-roof-ornaments-and-modern-towers-behind"],"yu-garden-bazaar-lit-pavilion-at-dusk")+
 '<p>Read these next: <a href="/guides/the-bund-shanghai-at-night/">the Bund at night</a>, <a href="/guides/nanjing-road-shanghai/">Nanjing Road</a>, <a href="/guides/huangpu-river-night-cruise/">the Huangpu River night cruise</a> and <a href="/guides/shanghai-circus-world-era-show/">the ERA show</a>. I also walked through the Yu Garden bazaar and a temple in the city, and I do not have guides for those yet.</p>'
 '<h2 id="hangzhou">Hangzhou: an easy extra</h2>'
 '<p>At Easter 2026 we added Hangzhou. We stayed at the InterContinental Hangzhou ICC from 3 to 5 April, the one with the golden globe, and we watched the light show on the towers across the river. I ordered food delivery there too, using the Meituan mini program inside WeChat, which I explain in the <a href="/guides/food-delivery-in-china-for-foreigners-meituan/">food delivery guide</a>. The full hotel story is on my <a href="/guides/ihg-hotels-china-shanghai-hangzhou-review/">IHG hotels page</a>.</p>'
 +_two("hangzhou-golden-globe-building-and-skyline-at-night","hangzhou-light-show-on-the-towers-across-the-river")+
 '<h2 id="next">Where I am going next</h2>'
 '<p>We fly from Ireland on 5 December and come home on 29 December. Chengdu is our base, with side trips to Chongqing and Xi\'an by high-speed train. The plan and the guides I am writing are on the <a href="/december-trip/">December trip page</a>.</p>'
 '<p class="note">Based on my trips in December 2025 and April 2026. Rules change, so double check before you fly.</p>'
)

guide("travelling-to-china-from-ireland","Travelling to China From Ireland: Flights and Setup",
 "Travelling to China from Ireland: visa-free entry, flights and what to set up",
 "How to travel to China from Ireland: visa-free entry, nonstop and connecting flights, eSIM, Alipay, trains and sockets, from two trips.",
 "travelling to china from ireland","",
 "<p>This is how I plan a trip to China from Ireland, written after two trips: Christmas 2025 and Easter 2026. It covers the entry rules, how to get there, and the setup that made the difference for me, with photos from Shanghai and Hangzhou so you can see where you could end up.</p>"
 "<p>Where something is my own experience I say so. Where I am passing on what the embassy or a news report says, I name it and link it. One of those sources is an article sponsored by the Embassy of China in Ireland, so I only use it for the embassy's own claims.</p>",
 IE_STEPS,IE_FAQ,IE_SOURCES,
 SITE+"/og/travelling-to-china-from-ireland.jpg",checked="2026-11-01",published="2026-11-01",vschema=False,
 steps_title="From Ireland to China, step by step",
 extra=IE_EXTRA,
 related=[("/guides/china-visa-free-30-days/","china-visa-free-30-days-departure-board-cover-4x5","VISA-FREE","China visa free 30 days: Irish, UK and EU passports"),("/guides/first-time-in-china/","first-time-in-china-13-things-before-you-fly","GUIDE 13","First time in China: 13 things to set up before you fly"),("/guides/china-travel-apps/","china-travel-apps-12-apps-to-set-up-before-china","GUIDE","Apps to download before you go to China")])
