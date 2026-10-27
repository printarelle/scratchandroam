# China hotel reviews: data skeleton, filled in AFTER each stay (December 2026).
# Nothing here is built or published until a stay is done and `stayed=True`.
# RULE: only what Natali saw, paid and said. No invented rooms, prices, meals or feelings.
# Each review becomes a guide at /guides/<slug>/ using guide() in src/content.py,
# with an #Ad booking box (needs a booking affiliate link she has: see "links" below).

FIELDS = [
 # (key, label shown in the "At a glance" table, what to capture during the stay)
 ("verdict", "Would I book it again?", "Yes / no, and one line on who it suits"),
 ("area", "Area", "District and what is around it"),
 ("metro", "Nearest metro", "Station, line, exit letter, minutes on foot (time it)"),
 ("from_arrival", "Getting there", "From the airport or station: how, how long, what it cost"),
 ("room", "Room we had", "Room type, floor, nights, how many of us"),
 ("price", "What we paid", "Per night and total, with the date booked and where"),
 ("breakfast", "Breakfast", "Included or not, hours, what was on it, any western options"),
 ("checkin", "Check-in", "Time, deposit taken (how much, card or Alipay), passport registration done by the hotel or not"),
 ("wifi", "Wi-Fi and VPN", "Speed test, did the VPN connect, did Google/WhatsApp work on the eSIM"),
 ("sockets", "Sockets", "UK, EU or Chinese, USB in the room"),
 ("noise", "Noise and sleep", "Street noise, aircon, blackout curtains"),
 ("parcels", "Parcels and delivery", "Did reception take Taobao parcels and food delivery to the room"),
 ("status", "IHG status", "IHG hotels only: what the status actually gave (upgrade, breakfast, late checkout), or nothing"),
 ("staff", "Staff and English", "How check-in and questions went"),
]

HOTELS = [
 dict(slug="yunzhongyue-apartment-chengdu-review", city="Chengdu", name="Yunzhongyue Apartment, Taikoo Li",
      kind="apartment", dates="6 to 29 Dec 2026 (kept during the side trips)", stayed=False,
      extra_checks=["Police registration for foreigners staying in an apartment: where, how long it took, what they asked for",
                    "Kitchen, washing machine, how check-in and keys worked, who to message"]),
 dict(slug="hotel-indigo-chongqing-chaotianmen-review", city="Chongqing", name="Hotel Indigo Chongqing Chaotianmen",
      kind="hotel", dates="9 to 13 Dec 2026", stayed=False,
      extra_checks=["View of the rivers and the drone show (Saturday 12 Dec)", "How new the hotel is and anything still being finished"]),
 dict(slug="han-tang-house-xian-review", city="Xi'an", name="Han Tang House (Guardian Han Tang)",
      kind="hotel", dates="14 to 18 Dec 2026", stayed=False,
      extra_checks=["Walk to the Bell and Drum Towers and the Muslim Quarter", "Getting to the Terracotta Army from here"]),
 dict(slug="intercontinental-chengdu-global-center-review", city="Chengdu", name="InterContinental Chengdu Global Center",
      kind="hotel", dates="24 to 25 Dec 2026 (Christmas)", stayed=False,
      extra_checks=["Christmas at the hotel: decorations, dinner, what was on", "Size of the Global Center and how to find your way"]),
]
