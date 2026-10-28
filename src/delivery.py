# Food delivery in China for foreigners: how we used Meituan inside WeChat (told by Natali 28 Oct 2026).
# RULE: her experience only as she told it; everything else is sourced and dated below. No invented orders, prices or feelings.
DL_SLUG="food-delivery-in-china-for-foreigners-meituan"
DL_STEPS=[
 ("Open Meituan inside WeChat",
  "You do not need to download anything new. In WeChat, tap search, type <b>meituan</b> and open the mini program called <b>美团外卖</b> (Meituan Waimai, the food delivery one, with the yellow kangaroo). I had a Chinese phone number on this trip, so Meituan let me in without any trouble.",
  ["meituan-mini-program-in-wechat-search-results"]),
 ("Turn on translation",
  "This is what made it easy for us. Tap the <b>···</b> button at the top right of the mini program and tap <b>Translation</b>. The menus, shop names and buttons switch to English, so you can actually choose what you are ordering. It is not a perfect translation, but with the food photos it is more than enough.",
  ["wechat-mini-program-menu-with-the-translation-button","meituan-wechat-mini-program-home-screen-translated-to-english"]),
 ("Check the delivery address",
  "When you order, WeChat fills in the address for you from where you are. Check that it really is your hotel, and add your room number. If it says the shop cannot deliver to your location, that shop is too far away, so pick one closer to you.",
  None),
 ("Pick your food",
  "Every dish has a photo, a price and how many were sold that month, and each shop shows the delivery time. On our biggest order, ten dishes from a pot sticker place came to ¥225.80, and the delivery and packing fee was ¥3.",
  ["meituan-restaurant-menu-in-wechat-translated-to-english"]),
 ("Leave a note for the rider",
  "There is a note box when you order. This is where you tell the rider what to do: leave it at reception, or bring it to the room with your room number if the hotel has a delivery robot. If you do not speak Chinese, write that they should not call you and should send a message instead. Messages translate automatically, phone calls do not. The Chinese for these is in the phrase list below.",
  None),
 ("Collect it at the hotel",
  "This depends on the hotel. At the voco in Shanghai a delivery robot brought the food up to our room. Other hotels we stayed at had a delivery spot where riders leave the orders. We ordered delivery at the InterContinental Pudong, the voco and in Hangzhou, and it was easy every time.",
  ["voco-shanghai-hongqiao-food-delivery-robot-in-the-hotel-corridor"]),
 ("Find your past orders",
  "The Orders tab keeps everything you ordered, so you can order the same thing again. The orders tab shows in Chinese for us, but the photos and prices make it easy to follow.",
  ["meituan-orders-list-in-wechat-delivered-to-our-hotel"]),
]

DL_PHRASES=[
 ("请放前台","qǐng fàng qiántái","Please leave it at reception","Mine, standard Mandarin. Travel to China gives 请送到前台, please deliver to reception."),
 ("请送到房间","qǐng sòng dào fángjiān","Please bring it to the room","Mine, standard Mandarin. Add your room number."),
 ("房间号","fángjiān hào","Room number","Mine, standard Mandarin. Write the number after it."),
 ("我不会说中文，请不要打电话，发消息","wǒ bú huì shuō zhōngwén, qǐng bú yào dǎ diànhuà, fā xiāoxi","I do not speak Chinese, please do not call, send a message","Mine, standard Mandarin."),
]

def _dl_extra():
    rows="".join(f'<tr><td data-label="Chinese"><b>{z}</b></td><td data-label="Pinyin">{p}</td><td data-label="Meaning">{m}</td><td data-label="Where it comes from">{n}</td></tr>' for z,p,m,n in DL_PHRASES)
    return f'''<h2 id="notes">Notes for the rider, ready to copy</h2>
<p>Copy these into the note box. Most of them are my own standard Mandarin, so I mark where each one comes from. Check them in a translator if you are unsure.</p>
<div class="tablewrap"><table class="stack"><thead><tr><th>Chinese</th><th>Pinyin</th><th>Meaning</th><th>Where it comes from</th></tr></thead><tbody>{rows}</tbody></table></div>
<h2 id="no-chinese-number">No Chinese phone number?</h2>
<p>I had a Chinese number, so I did not have this problem. Here is what the sources say for when you do not:</p>
<ul>
<li><b>Try the Meituan mini program in WeChat first.</b> Hidden China Travel (updated 5 September 2026) says it may work without a separate Meituan account, depending on your WeChat verification.</li>
<li><b>Or use Alipay.</b> Travel to China (updated 3 July 2026) says the Meituan mini program inside Alipay piggybacks on your Alipay account, so no Chinese number is needed.</li>
<li><b>The other big delivery app, Ele.me, is now called Taobao Instant</b> (淘宝闪购). Hidden China Travel says it runs as a mini program in Alipay with no separate sign-up, and searching eleme in Alipay takes you there.</li>
<li><b>The standalone apps are harder.</b> My China Guide says the standalone Meituan and Ele.me apps ask for a Chinese number for the text message code.</li>
</ul>
<p>Whichever you use, you pay through WeChat Pay or Alipay, so link your card before you fly. My <a href="/guides/china-travel-apps/">China travel apps guide</a> shows how, and my <a href="/guides/china-travel-apps/#our-trip">SIM story</a> explains why a full Chinese SIM made apps like this easier for me.</p>
<h2 id="if-it-goes-wrong">If it goes wrong</h2>
<p>My China Guide says riders call from a +86 number when they arrive, and some upscale hotels stop riders in the lobby, so you go down to collect. If you cannot order at all, the same sources suggest asking reception to order for you, or walking to a convenience store.</p>'''

DL_INTRO='''<p>Food delivery was one of the best things about our trips to China. We ordered to the hotel at the InterContinental Pudong, at the voco in Shanghai and in Hangzhou, and at the voco a little robot brought it up to our room.</p>
<p>I used Meituan, inside WeChat. I did not install a separate app. WeChat translates the whole thing into English, it fills in the hotel address for you, and you can leave the rider a note. This guide is exactly how I did it, with my own screenshots, plus what the sources say if you do not have a Chinese phone number like I did.</p>'''

DL_FAQ=[
 ("Can foreigners use Meituan in China?","Yes. I used the Meituan mini program inside WeChat with a Chinese phone number, and turned on WeChat's translation to read it in English. Without a Chinese number, Travel to China says the Meituan mini program inside Alipay works on your Alipay account."),
 ("Do I need a Chinese phone number for food delivery in China?","Not always. I had one, so it was easy. Hidden China Travel says Taobao Instant (formerly Ele.me) works as a mini program in Alipay with no separate sign-up, and Travel to China says the same for Meituan in Alipay. The standalone apps usually want a Chinese number."),
 ("Can I get food delivered to my hotel room in China?","Often, yes. At the voco in Shanghai a robot brought our food to the room. Other hotels had a delivery spot downstairs. Write a note: leave it at reception, or bring it to the room with the room number."),
 ("How much is food delivery in China?","On our biggest order, ten dishes came to ¥225.80 and the delivery and packing fee was ¥3. Hidden China Travel says fees are usually ¥3 to ¥6 and often waived on bigger orders."),
 ("How do I talk to the delivery rider if I do not speak Chinese?","Write in the note that they should send a message, not call. Messages translate automatically. My China Guide also recommends the in-app chat with its translate button over phone calls."),
]

DL_SOURCES=[
 ("Travel to China: Can foreigners use Meituan? Updated 3 July 2026","https://www.traveltochina.net/guides/how-to-use-meituan-foreigner",False),
 ("Hidden China Travel: Order food in China without a Chinese number, updated 5 September 2026","https://hiddenchinatravel.com/order-food-china-without-chinese-number",False),
 ("My China Guide: What to expect when ordering food delivery to a hotel in China (2026, no exact date shown)","https://mychina.guide/questions/what-expect-when-ordering-food-delivery-hotel-apartment-china",False),
]

guide(DL_SLUG,"Food delivery in China for foreigners: Meituan in WeChat",
 "Food delivery in China as a foreigner: how we ordered Meituan in WeChat to our hotel",
 "How we ordered food delivery in China: Meituan inside WeChat in English, notes for the rider, hotel robots, and what to do with no Chinese number.",
 "food delivery in china for foreigners",None,DL_INTRO,DL_STEPS,DL_FAQ,DL_SOURCES,
 SITE+"/og/food-delivery-in-china-for-foreigners-meituan.jpg",
 related=[("/guides/how-to-order-food-in-china-without-speaking-chinese/","order-food-in-china-without-speaking-chinese-cover-16x9","FOOD","How to order food in China without speaking Chinese"),
          ("/guides/china-travel-apps/","china-travel-apps-12-apps-to-set-up-before-china","APPS","Apps to download before you go to China"),
          ("/guides/ihg-hotels-china-shanghai-hangzhou-review/","intercontinental-shanghai-pudong-diplomatic-suite-living-area","HOTELS","IHG hotels we stayed at in China")],
 checked="2026-10-28",published="2026-10-28",steps_title="How we ordered, step by step",
 extra=_dl_extra(),
 shotnote="From my own phone, April 2026.",
 gallery=[("hotel-food-delivery-robot-china-cover-4x5","Our delivery robot")],
 head='<style>.art .shots{display:flex;flex-wrap:wrap;gap:14px;align-items:flex-start}.art .shots figure{flex:0 1 300px;max-width:300px;margin:0}</style>')
