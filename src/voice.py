# First-hand stories shown as a "From our trip" section near the top of a guide.
# RULE: only things Natali has told us happened. Never invent a scene, a time or a feeling.
# Source for each story is noted next to it (the date she told it).

_INTERNET = ('<p>On our first trip, Christmas 2025, my eSIM was ready, and I forgot to switch it on before we landed. '
  'So we did the thing I would not do again: we bought Chinese SIM cards at the airport. '
  'I also had only one VPN, NordVPN, and it needed wifi to activate again. '
  'In the end our hotel concierge shared the VPN he used, LetsVPN, and that got us back online.</p>'
  '<p>When we went back for Easter 2026 we were fully prepared. '
  'My lesson from it: even when you research everything, have a backup plan.</p>')  # told 17 Oct 2026

_SIM = ('<p>Another time I pre-ordered a Nihao Mobile SIM and picked it up at the airport. '
  'The internet worked, and Meituan and food ordering worked. But a lot of other apps and attraction ticket sites kept refusing it, '
  'because the number counted as a virtual number. A full China Mobile SIM never gave me any of those errors.</p>')  # told 20 Oct 2026

_12306 = ('<p>Trains: I could not get through the 12306 registration in the Alipay version, '
  'so I booked all our train tickets on Trip.com and paid a small fee. '
  'If you want to use 12306 itself, download the real app from the App Store or Google Play.</p>')  # told 16 Oct 2026

STORIES = {
 "first-time-in-china": ("What went wrong on our first trip", _INTERNET + _12306),
 "china-travel-apps": ("What I got wrong with apps the first time", _INTERNET + _SIM + _12306),
 "top-25-china-apps": ("Why the eSIM and VPN rank so high", _INTERNET),
 "china-before-you-fly-checklist": ("Where this list comes from", _INTERNET),
 "taobao-for-foreigners": ("How I send parcels to hotels",
   '<p>I have ordered tens of parcels to hotels in China this way and not one was lost. '
   'Before anything arrives, I message the hotel by email or WeChat with my name, my booking number and my dates. '
   'I ask for their exact address in Chinese and the reception phone number. '
   'On the order I put my English name and my own phone number with the country code, '
   'because staff match parcels by the last 4 digits.</p>'
   '<p>One thing I learned: I do not order to a hotel when I am staying only one to three days. '
   'Delivery can take up to three days, and the parcel arrives after you leave.</p>'
   '<p>I have also used Pinduoduo. To me it is a cheaper version of Taobao.</p>'),  # told 17 and 19 Oct 2026
 "taobao-11-11-singles-day-for-foreigners": ("How I send parcels to hotels",
   '<p>I have ordered tens of parcels to hotels in China and not one was lost. '
   'Before anything arrives, I message the hotel by email or WeChat with my name, my booking number and my dates. '
   'I ask for their exact address in Chinese and the reception phone number. '
   'On the order I put my English name and my own phone number with the country code, '
   'because staff match parcels by the last 4 digits.</p>'
   '<p>One thing I learned: I do not order to a hotel when I am staying only one to three days. '
   'Delivery can take up to three days, and the parcel arrives after you leave.</p>'
   '<p>I have also used Pinduoduo. To me it is a cheaper version of Taobao.</p>'),  # told 17 and 19 Oct 2026, same story as the Taobao guide
 "the-bund-shanghai-at-night": ("New Year on the Bund",
   '<p>Our first China trip was Christmas 2025. We spent Christmas at Shanghai Disneyland, and then New Year and the day after on the Bund and Nanjing Road. '
   'Honestly, it was the best decision we made on that trip. '
   'The photos on this page are mine.</p>'
   '<p>We stayed at the Crowne Plaza on Nanjing Road, so we could literally go to the Bund every day. '
   'At night we usually went after 8pm. It was Christmas and New Year, so it was always full, and we did not want to stand in the crowd just watching the lights go up. '
   'What we did enjoy was the light show of the city from our cruise, and walking down the Bund and having a good time.</p>'
   '<p>The crowds are always there, because it is the most popular area, so you will see them wherever you go. '
   'And it is really easy to get to. Ask anyone and they will tell you: all roads lead to the Bund.</p>'),  # told 21 and 30 Oct 2026
 "nanjing-road-shanghai": ("New Year on Nanjing Road",
   '<p>Our first China trip was Christmas 2025. After Christmas at Shanghai Disneyland, we spent New Year and the day after on Nanjing Road and the Bund. '
   'It was the best decision we made on that trip. The photos here are mine.</p>'
   '<p>We stayed at the Crowne Plaza on Nanjing Road, so the street was right outside and the Bund was a short walk away.</p>'),  # told 21 and 30 Oct 2026
 "huangpu-river-night-cruise": ("Our night on the river",
   '<p>We took the night cruise on our first China trip, Christmas 2025, when we spent New Year and the day after on the Bund and Nanjing Road. '
   'What we loved at night was the light show of the city from our cruise. The photos on this page are mine, taken from the water.</p>'
   '<p>We booked the Huangpu River Cruise (Qingjiang Line) on Klook for the night of 26 December 2025, three night cruise tickets for €40.29 in total. The departure location on the booking was Shiliupu Marina.</p>'),  # told 21 and 30 Oct 2026
 "china-dos-and-donts": ("One rule I broke without needing to",
   '<p>Number 12 says pack a plug adapter, and I still do. But every hotel we stayed in in Shanghai had UK sockets, '
   'so we never actually needed it there. I carry one anyway, just in case, because the next hotel might not.</p>'),  # told 21 Oct 2026
}
