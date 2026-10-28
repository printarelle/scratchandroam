# IHG hotels we stayed at in China (Shanghai and Hangzhou). Told by Natali 28 Oct 2026.
# RULE: only what she said and what her IHG screenshots show. Never put confirmation numbers, card digits or phone numbers here.
def _fig(k,w=""):
    return f'<figure{w}><img src="/img/{k}.jpg" alt="" loading="lazy"><figcaption>{html.escape(IMGREG[k+".jpg"]["cap"])}</figcaption></figure>'
def _row(*ks): return '<div class="gal2">'+"".join(_fig(k) for k in ks)+'</div>'
def _gl(label,items):
    return '<ul class="glance">'+"".join(f'<li><b>{a}</b> {b}</li>' for a,b in items)+'</ul>'
def _maplink(name,addr):
    q=(name+" "+addr).replace(" ","+").replace(",","%2C")
    return f'<a href="https://www.google.com/maps/search/?api=1&amp;query={q}" rel="noopener">Open {html.escape(name)} in Google Maps</a>'

_MAP='''<figure class="hmap"><svg viewBox="0 0 720 270" role="img" aria-labelledby="hmt hmd" xmlns="http://www.w3.org/2000/svg">
<title id="hmt">Where our three Shanghai IHG hotels are, west to east</title>
<desc id="hmd">A simple diagram of Shanghai from west to east: voco Hongqiao Hub in the far west, Crowne Plaza on Nanjing Road near the river, the Huangpu river, then InterContinental Pudong on the east side. Not to scale.</desc>
<rect width="720" height="270" rx="14" fill="#FBF3E6"/>
<path d="M470 0 C 440 70, 520 120, 480 180 S 500 250, 490 270 L 530 270 C 540 240, 520 190, 520 170 C 560 120, 480 60, 510 0 Z" fill="#BFE3E0"/>
<text x="505" y="30" font-size="13" fill="#2F6F73" font-family="Plus Jakarta Sans,Arial,sans-serif" font-weight="700" text-anchor="start">Huangpu river</text>
<line x1="110" y1="150" x2="440" y2="150" stroke="#14213D" stroke-width="3" stroke-dasharray="2 9" stroke-linecap="round" opacity=".55"/>
<text x="270" y="178" font-size="12" fill="#14213D" font-family="Plus Jakarta Sans,Arial,sans-serif" text-anchor="middle" opacity=".75">Nanjing Road runs from People's Square to the river</text>
<circle cx="110" cy="150" r="13" fill="#E8613C"/><text x="110" y="155" font-size="13" fill="#fff" text-anchor="middle" font-weight="700" font-family="Plus Jakarta Sans,Arial,sans-serif">1</text>
<circle cx="430" cy="150" r="13" fill="#E8613C"/><text x="430" y="155" font-size="13" fill="#fff" text-anchor="middle" font-weight="700" font-family="Plus Jakarta Sans,Arial,sans-serif">2</text>
<circle cx="610" cy="135" r="13" fill="#E8613C"/><text x="610" y="140" font-size="13" fill="#fff" text-anchor="middle" font-weight="700" font-family="Plus Jakarta Sans,Arial,sans-serif">3</text>
<text x="110" y="115" font-size="14" fill="#14213D" text-anchor="middle" font-weight="700" font-family="Plus Jakarta Sans,Arial,sans-serif">voco Hongqiao Hub</text>
<text x="110" y="98" font-size="12" fill="#14213D" text-anchor="middle" font-family="Plus Jakarta Sans,Arial,sans-serif" opacity=".75">far west, quiet</text>
<text x="400" y="115" font-size="14" fill="#14213D" text-anchor="middle" font-weight="700" font-family="Plus Jakarta Sans,Arial,sans-serif">Crowne Plaza</text>
<text x="400" y="98" font-size="12" fill="#14213D" text-anchor="middle" font-family="Plus Jakarta Sans,Arial,sans-serif" opacity=".75">on Nanjing Road</text>
<text x="610" y="105" font-size="14" fill="#14213D" text-anchor="middle" font-weight="700" font-family="Plus Jakarta Sans,Arial,sans-serif">InterContinental</text>
<text x="610" y="88" font-size="12" fill="#14213D" text-anchor="middle" font-family="Plus Jakarta Sans,Arial,sans-serif" opacity=".75">Pudong, Lujiazui</text>
<text x="360" y="252" font-size="12" fill="#14213D" text-anchor="middle" font-family="Plus Jakarta Sans,Arial,sans-serif" opacity=".7">West to east. A simple diagram, not to scale.</text>
</svg><figcaption>Our three Shanghai hotels from west to east. The Hangzhou hotel is in another city, so it is not on this diagram.</figcaption></figure>'''

_PTS='''<div class="tablewrap"><table class="tbl"><thead><tr><th>Hotel</th><th>When</th><th>What our IHG account shows</th></tr></thead><tbody>
<tr><td style="min-width:11em"><b>InterContinental Shanghai Pudong</b></td><td>23 to 28 Dec 2025, 5 nights</td><td>Paid with points. A confirmable suite upgrade was redeemed for 0 points. IHG lists a total spending of ¥3,200.17 (about $452.28), before taxes and fees.</td></tr>
<tr><td style="min-width:11em"><b>Crowne Plaza Shanghai Nanjing Road</b></td><td>28 Dec 2025 to 2 Jan 2026, 5 nights</td><td>Paid with points. IHG lists a total spending of ¥5,941.20 (about $848.57), before taxes and fees.</td></tr>
<tr><td style="min-width:11em"><b>voco Shanghai Hongqiao Hub</b></td><td>April 2026</td><td>Paid with points, from 12,750 to 22,100 points a night on the nights listed.</td></tr>
<tr><td style="min-width:11em"><b>InterContinental Hangzhou ICC</b></td><td>3 to 5 Apr 2026, 2 nights</td><td>34,850 points for the first night and 51,000 points for the second, so 85,850 points in all.</td></tr>
</tbody></table></div>'''

_EXTRA='''
<h2 id="how-we-paid">How we paid: IHG points, not cash</h2>
<p>We are IHG Diamond Elite members. Over about two years we collected IHG points, and we used them to book every hotel in this post. Nothing here was paid in cash, so the numbers below are points, and I put IHG's own money figure next to them where the account showed one.</p>
<p>IHG changes the points price by date, so nightly prices move. The table shows what our account listed for our dates, not a price list. I have kept our booking numbers and card details off this page on purpose.</p>
'''+_PTS+'''
<p class="shotnote">The figures come from the Stays and Points pages of our own IHG account. They are what we saw for our dates, so check the IHG site for yours.</p>

<h2 id="map">Where the hotels are</h2>
'''+_MAP+'''
<p>Open each hotel on a map before you go. These links use the hotel name and street address: '''+" · ".join([
 _maplink("InterContinental Shanghai Pudong","777 Zhangyang Road, Pudong, Shanghai"),
 _maplink("Crowne Plaza Shanghai Nanjing Road","719 Nanjing East Road, Shanghai"),
 _maplink("voco Shanghai Hongqiao Hub","No. 1 Lane 958 Jinshajiang West Road, Shanghai"),
 _maplink("InterContinental Hangzhou ICC","No. 2 Jiefang East Road, Hangzhou")])+'''.</p>
<p class="shotnote">Google Maps can be slow or blocked in China. Use Amap or Apple Maps on the ground, and show your driver the address in Chinese from the hotel's booking email.</p>

<h2 id="pudong">InterContinental Shanghai Pudong: the suite upgrade</h2>
'''+_gl("",[("Stayed:","23 to 28 December 2025, 5 nights"),("Room:","Diplomatic Suite, 68 to 72 sq m, 1 king bed, on a higher floor"),("Area:","Lujiazui financial district, Pudong"),("Breakfast:","free, in the top floor club lounge"),("Our verdict:","the one that felt special")])+'''
<p>This was our first hotel in China, over Christmas 2025. We booked a normal room with points and then used a confirmable suite upgrade, so we ended up in the Diplomatic Suite. The upgrade cost 0 points on our account.</p>
'''+_row("intercontinental-shanghai-pudong-diplomatic-suite-living-area","intercontinental-shanghai-pudong-diplomatic-suite-sofa-and-city-view")+'''
<p>It was a higher floor with a great view. The living room has a TV and a huge open window, and the bedroom is separate, so you are not sleeping next to your suitcase. The toilet is separate, and there is a big shower and a bathtub. The cleaning service was great.</p>
'''+_row("intercontinental-shanghai-pudong-diplomatic-suite-king-bedroom")+'''
<h3>Diamond status, in real life</h3>
<p>At reception they recognised our Diamond status straight away, and their English was good. Breakfast was free in the lounge on the top floor, cooked to order, with a small buffet as well. Lounge access also came with a free drink, plus cakes, snacks and fruit. We used the lounge one or two days.</p>
<h3>Parcels</h3>
<p>I contacted the hotel before we arrived about my Taobao orders. They received almost 60-something parcels. The staff put them on a baggage cart, sorted them, counted them and covered them for us. I wrote about how I do this in the <a href="/guides/taobao-for-foreigners/">Taobao guide</a>.</p>
<h3>Getting there</h3>
<ul>
<li><b>From Pudong airport:</b> I took the maglev, then the metro. The maglev runs to Longyang Road in about 8 minutes, and the listed ticket price is ¥50. From there, Line 2 takes you into Lujiazui.</li>
<li><b>Nearest big metro station:</b> Century Avenue, where Lines 2, 4, 6 and 9 meet. The hotel's address is 777 Zhangyang Road. I walked about 10 minutes from the metro with luggage, but I do not remember which station it was, so check the walking route on your map before you leave.</li>
<li><b>The area:</b> the hotel is in Lujiazui, the financial district, which is well placed for the metro.</li>
</ul>
<p><b>Would we book it again?</b> Yes. The suite, the lounge breakfast and the way they handled my parcels made it a great start to our first China trip.</p>

<h2 id="crowne-plaza">Crowne Plaza Shanghai Nanjing Road: right on the walking street</h2>
'''+_gl("",[("Stayed:","28 December 2025 to 2 January 2026, 5 nights"),("Room:","older style, smaller, one small window, top floor"),("Area:","literally on Nanjing Road"),("Breakfast:","free, and one of my favourites in China"),("Our verdict:","for the location, yes")])+'''
<p>We spent New Year here, and the location is the whole point. The hotel is literally on Nanjing Road. It is an older building, and our room was in the older style: smaller, with one small window, on the top floor. I tried for the upgrade, but there was nothing available because of the holiday.</p>
'''+_row("crowne-plaza-shanghai-nanjing-road-lobby-christmas-tree")+'''
<p>The bed was comfortable and the cleaning was very good. Breakfast was free and it was one of my favourite breakfasts in China: a huge choice and always fresh. There were many foreign tourists, because it was Christmas and New Year.</p>
<p>We had few deliveries here, and the hotel received them without trouble. We had no luggage issues. As Diamond members we could have used the lounge, but we did not use it.</p>
<h3>Getting there</h3>
<ul>
<li><b>Two entrances.</b> One is on Nanjing Road and one is on the other side, on Jiujiang Road. Didi and taxis can only come to one side, so check which entrance you are being taken to. The address on the booking is 719 Nanjing East Road.</li>
<li><b>Metro:</b> the metro and Didi connections are good. People's Square station is a short walk away, and East Nanjing Road station is a bit further towards the river.</li>
<li><b>The Bund</b> is at the other end of the walking street. We have a guide for the <a href="/guides/nanjing-road-shanghai/">Nanjing Road walk</a> and for the <a href="/guides/the-bund-shanghai-at-night/">Bund at night</a>.</li>
</ul>
<p><b>Would we book it again?</b> For New Year on Nanjing Road, yes.</p>

<h2 id="voco">voco Shanghai Hongqiao Hub: the one we would not repeat</h2>
'''+_gl("",[("Stayed:","April 2026"),("Room:","a big, beautiful room with two toilets and a huge bathroom"),("Area:","outside the town centre, little to see nearby"),("Breakfast:","very limited, mostly for Chinese guests"),("Our verdict:","not again")])+'''
<p>I am going to be honest here. The room itself was lovely: big and beautiful, with two toilets and a huge bathroom. Deliveries were accepted without any problems.</p>
'''+_row("voco-shanghai-hongqiao-room-living-area","voco-shanghai-hongqiao-lounge-dessert-plate-with-view")+'''
<h3>What went wrong</h3>
<ul>
<li><b>The smart toilet.</b> On the first use it would not flush. The service team came, but their English was limited, and it failed again, so we used the other toilet.</li>
<li><b>The smell.</b> There was a constant smell of sulfur in the room. I think it came from the sewage pipes or the air conditioning. We reported it multiple times. Sometimes it was fine and sometimes it was very bad.</li>
<li><b>We did not ask for another room.</b> Even with Diamond status, we never asked to move. That was our own fault. If this happens to you, ask for a new room straight away.</li>
<li><b>Getting ill.</b> We went to Hangzhou for a few days. On our last 2 days at the voco we got sick with vomiting and diarrhoea. I think the smell caused it, but I cannot prove that. By then it was too late to complain.</li>
<li><b>The review.</b> I left a negative review on the IHG site and nobody contacted us.</li>
</ul>
'''+_row("voco-shanghai-hongqiao-lounge-window-view-of-the-river")+'''
<p>Breakfast was very limited and mostly for Chinese guests. We did use the lounge. It was ok, but nothing special: a few drinks, some fruit and pastries, and a view over the water. The dessert plate and the view in the pictures are from there.</p>
<h3>Getting there</h3>
<ul>
<li><b>The area:</b> it is outside the centre. There is little to see around the hotel, so plan on using the metro.</li>
<li><b>Metro:</b> the nearest station is West Jinshajiang Road on Line 13. Listings say 7 to 13 minutes on foot. It felt like about 15 minutes to me with bags.</li>
<li><b>The address:</b> No. 1 Lane 958 Jinshajiang West Road. Save it in Chinese for your driver.</li>
</ul>
<p><b>Would we book it again?</b> No. We will not be choosing voco again, or, if we did, we would ask for a room change straight away.</p>

<h2 id="hangzhou">InterContinental Hangzhou ICC: five stars from us</h2>
'''+_gl("",[("Stayed:","3 to 5 April 2026, 2 nights"),("Room:","no upgrade, because it was a one night booking"),("Area:","next to the metro, with the golden globe building"),("Breakfast:","free"),("Our verdict:","5 stars for us")])+'''
<p>We booked one night, and it rained. The hotel was so good that we extended for one more night with points, so we stayed 2 nights in all. The second night cost 51,000 points on our account, which is more than the first (34,850), so it is worth knowing that extending can cost more.</p>
'''+_row("hangzhou-civic-center-dome-at-night-in-the-rain")+'''
<p>Check-in was great, and they recognised our Diamond status. There was no upgrade, because it was a one night booking when we arrived. Breakfast was free, the service was great and the view was great. At night there is a light show.</p>
'''+_row("hangzhou-lit-towers-across-the-water-at-night","hangzhou-light-show-pagoda-pattern-on-the-towers")+'''
<h3>Getting there</h3>
<ul>
<li><b>Metro:</b> Civic Center station, on Lines 4 and 7, is a few steps from the hotel. That is what makes it such an easy base.</li>
<li><b>The address:</b> No. 2 Jiefang East Road, Hangzhou.</li>
</ul>
<p><b>Would we book it again?</b> Yes, without thinking about it.</p>

<h2 id="compare">The four side by side</h2>
<div class="tablewrap"><table class="tbl"><thead><tr><th>Hotel</th><th>Best thing</th><th>Watch out for</th><th>Again?</th></tr></thead><tbody>
<tr><td style="min-width:11em"><b>InterContinental Pudong</b></td><td>The suite upgrade, the lounge breakfast, the parcel care</td><td>About 10 minutes' walk from the metro with luggage</td><td>Yes</td></tr>
<tr><td style="min-width:11em"><b>Crowne Plaza Nanjing Road</b></td><td>The location, a huge fresh breakfast</td><td>An older, smaller room with one small window</td><td>Yes, for the location</td></tr>
<tr><td style="min-width:11em"><b>voco Hongqiao Hub</b></td><td>A big, beautiful room</td><td>The sulfur smell, a smart toilet that would not flush, a limited breakfast</td><td>No</td></tr>
<tr><td style="min-width:11em"><b>InterContinental Hangzhou ICC</b></td><td>The metro next door, the service, the view and the light show</td><td>An extra night can cost more points</td><td>Yes</td></tr>
</tbody></table></div>

<h2 id="tips">What I would tell you before you book with points</h2>
<ul>
<li><b>Check the status perks on the day.</b> Diamond was recognised at both InterContinentals. An upgrade depends on what is free: it worked at Pudong, not at the Crowne Plaza over New Year, and not on a one night booking in Hangzhou.</li>
<li><b>Write to the hotel before you arrive</b> if you are sending parcels, and read the <a href="/guides/taobao-for-foreigners/">Taobao guide</a> first.</li>
<li><b>If something is wrong in the room, ask to move on day one.</b> I waited, and I would not do that again.</li>
<li><b>Check the metro walk on a map,</b> not just the hotel's description.</li>
</ul>

<h2 id="disclosure">Is this sponsored?</h2>
<p>No. We booked these stays ourselves with our own IHG points, and I have no affiliate link for IHG, so there is no link on this page that earns me money. If that ever changes, I will say so here and on the <a href="/affiliate-disclosure/">affiliate disclosure page</a>.</p>
'''

guide("ihg-hotels-china-shanghai-hangzhou-review","IHG hotels in China: 4 stays in Shanghai and Hangzhou",
 "IHG hotels we stayed at in China: Shanghai and Hangzhou, paid with points",
 "Our four IHG stays in China, paid with points: InterContinental Pudong, Crowne Plaza Nanjing Road, voco Hongqiao and InterContinental Hangzhou. Reviews.",
 "IHG hotels in China",None,
 "<p>My husband and I are IHG Diamond Elite members. For about two years we collected IHG points, and we spent them on hotels in China: three in Shanghai and one in Hangzhou. This is what each one was really like, what the points cost on our account, and how to get to each one.</p><p>Two were great, one was just right for its location, and one we will not repeat. I will tell you which and why.</p><p>I only write about what we stayed in and what we saw.</p>",
 [],
 [("Which IHG hotels did we stay at in China?","InterContinental Shanghai Pudong (23 to 28 December 2025), Crowne Plaza Shanghai Nanjing Road (28 December 2025 to 2 January 2026), voco Shanghai Hongqiao Hub (April 2026) and InterContinental Hangzhou ICC (3 to 5 April 2026)."),
  ("Which one was our favourite?","InterContinental Hangzhou ICC, which we gave 5 stars. The InterContinental Pudong suite was a close second."),
  ("Did our IHG Diamond status help?","At both InterContinentals they recognised it at check-in and we got free breakfast. At Pudong we also had a suite upgrade and lounge access. At the Crowne Plaza the upgrade was not available over New Year, and we did not use the lounge."),
  ("Would we stay at the voco Hongqiao Hub again?","No. The room was beautiful, but there was a constant sulfur smell and we both got ill in the last 2 days. If you stay, ask for another room on the first day."),
  ("How do you get from Pudong airport to the InterContinental Pudong?","I took the maglev to Longyang Road, then the metro towards Lujiazui. The hotel is at 777 Zhangyang Road, and I walked about 10 minutes from the metro."),
  ("Do Chinese hotels accept Taobao parcels?","They did at all four. Write to the hotel before you arrive. The InterContinental Pudong received almost 60-something of my parcels and sorted and counted them.")],
 [("IHG Hotels and Resorts (official)","https://www.ihg.com/",True),
  ("Shanghai Metro (official)","https://service.shmetro.com/",True),
],
 SITE+"/img/intercontinental-shanghai-pudong-diplomatic-suite-living-area.jpg",
 related=[("/guides/nanjing-road-shanghai/","nanjing-road-shanghai-neon-shop-fronts-cover-4x5","SHANGHAI","Nanjing Road: how to walk it and when the neon is on"),("/guides/taobao-for-foreigners/","how-to-order-on-taobao-step-by-step-guide-cover","SHOPPING","How to order on Taobao as a foreigner, step by step")],
 gallery=[("intercontinental-shanghai-pudong-diplomatic-suite-living-area","The Diplomatic Suite at InterContinental Pudong"),("hangzhou-lit-towers-across-the-water-at-night","Hangzhou lit up"),("crowne-plaza-shanghai-nanjing-road-lobby-christmas-tree","Christmas at the Crowne Plaza"),("voco-shanghai-hongqiao-room-living-area","The voco room"),("hangzhou-civic-center-dome-at-night-in-the-rain","Hangzhou in the rain")],
 place={"name":"IHG hotels in China","city":"Shanghai","free":False},
 extra=_EXTRA,published="2026-10-28",checked="2026-10-28",
 shorts={"Instagram":"https://www.instagram.com/scratchandroam/","TikTok":"https://www.tiktok.com/@scratchandroam","Pinterest":"https://www.pinterest.com/scratchandroam/"})
