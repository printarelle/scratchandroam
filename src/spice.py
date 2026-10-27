# Build spice tolerance before China (SR-0045). Ember look from the Scratch & Roam video. Facts checked 26 Oct 2026.
SP_SLUG="build-spice-tolerance-before-china"
SP_WEEKS=[
 ("Week 1: a pinch of chilli flakes","Add a small pinch of dried chilli flakes to food you already eat and like: eggs, noodles, soup, pizza. Do it three times this week. The goal is not heat, it is getting used to the burn arriving and fading while you keep eating. If it makes you stop, use less next time."),
 ("Week 2: jalapeño or a mild hot sauce","Move to fresh or pickled jalapeño, or a mild bottled hot sauce, three times this week. A rule of thumb that is mine, not from a study: when last week's meals feel easy and the burn is gone within a few minutes, step up. If not, repeat the week."),
 ("Week 3: sriracha-level sauce","Use a sriracha-level sauce on whole meals, not only a bite. Keep milk, yoghurt, rice or bread on the table, because practising the cool-down is part of the training (the cooling section below says what works)."),
 ("Week 4: chilli oil or chilli crisp","Chilli oil and chilli crisp are closer to what you will meet in Sichuan and Chongqing food: the heat comes in oil and lingers. Start with a small spoon over rice, noodles or dumplings and add more only when it feels comfortable."),
 ("Week 5: add a pinch of Sichuan pepper","Now add the numbing half of màlà. Buy whole or ground Sichuan peppercorns (hua jiao) and add a very small pinch to your chilli oil dish. It does not feel like heat. It feels like buzzing or tingling on the lips and tongue, which surprises most first-timers, so do not start with a big amount."),
 ("Week 6: a mild mala dish","Eat an actual mild mala dish, ideally at a Sichuan restaurant, or a hotpot with a mild half (a split pot). Practise the ordering words in the ordering section below. If you can finish it comfortably, you are ready to start mild in China, not medium."),
]
SP_COOL=[
 ("works","🥛","Milk or yoghurt","Dairy fat and the protein casein help lift the chilli oil off your tongue. Whole milk beats fat-free, and yoghurt and ice cream also help.","Food Network"),
 ("works","🍚","Rice or bread","Starch acts like a mop and soaks up the oily capsaicin. Keep a bowl of plain rice next to the pot.","Food Network"),
 ("works","🍯","Sugar or honey","A little sugar or honey held in the mouth can take the burn down. A sweet drink does something similar.","Food Network; China for Travelers"),
 ("works","🥜","Peanut milk or sesame oil dip","China for Travelers calls peanut milk the classic antidote at Chongqing hotpot, and says the sesame oil and garlic dip is meant to cool the heat. It puts the fat or sugar to work.","China for Travelers"),
 ("partly","🍋","Lemon, lime juice or vinegar","Food Network says acids like vinegar, lemon and tomato may reduce the burn but it might take a lot. One commercial spice blog says citrus does not meaningfully help. The evidence is thin, so treat it as a try-it, not a fix.","Food Network; Alibaba spice blog"),
 ("partly","🥥","Coconut milk","It is rich in fat, so it should behave like other fats. I found no source about coconut milk specifically, so this one is my inference.","My inference"),
]
SP_AVOID=[("🚰","Cold or ice water","Chilli's heat comes from capsaicin, which is oil based, so water mostly spreads it around. Any relief is short."),
 ("🥤","Soda or sparkling water","China for Travelers says to avoid ice water, sodas and sparkling water. Fat or sugar neutralises capsaicin, plain cold water does not."),
 ("🍵","Hot tea","Food Network lists it as a myth: heat can make the burn feel stronger."),
 ("🍺","Beer","Mostly water with about 5 percent alcohol, so Food Network rates it a weak fix."),
 ("🥃","Strong baijiu","China for Travelers says it intensifies the burn for foreigners.")]
SP_TERMS=[("不辣","bù là","No spice","Chongqing servers may question a pure no-spice order but will honour it (China for Travelers)."),
 ("微微辣","wēiwēi là","Very mild","Listed by Baba goes China as the mildest step on the broth scale."),
 ("微辣","wēi là","Mild","Not mild by Western standards. China for Travelers says Chongqing's 微辣 is roughly Chengdu's 中辣."),
 ("中辣","zhōng là","Medium","Already hot for most first-timers."),
 ("重辣","zhòng là","Hot","China for Travelers calls this the local default in Chongqing. Skip it on your first night."),
 ("变态辣","biàntài là","Eating-challenge level","China for Travelers says do not. Neither should you."),
 ("鸳鸯锅","yuānyāng guō","Split hot pot","Mild broth in one half, spicy in the other. Both guides recommend it for first-timers, and it lets a group share one pot.")]
SP_SAY=[("我要微辣。","Wǒ yào wēi là.","I would like mild."),("不要太辣。","Bù yào tài là.","Not too spicy."),("我们要鸳鸯锅。","Wǒmen yào yuānyāng guō.","We would like a split pot.")]

def _sp_extra():
    cool="".join(f'<div class="sp-c sp-{v}"><div class="sp-e">{e}</div><div><b>{t}</b><span class="sp-v">{ {"works":"Works","partly":"Partly or unproven"}[v]}</span><p>{d}</p><small>Source: {s}</small></div></div>' for v,e,t,d,s in SP_COOL)
    avoid="".join(f'<div class="sp-c sp-no"><div class="sp-e">{e}</div><div><b>{t}</b><span class="sp-v">Skip</span><p>{d}</p></div></div>' for e,t,d in SP_AVOID)
    terms="".join(f'<tr><td class="zh">{z}</td><td>{p}</td><td><b>{m}</b></td><td>{n}</td></tr>' for z,p,m,n in SP_TERMS)
    say="".join(f'<li><span class="zh">{z}</span><span>{p}</span><em>{m}</em></li>' for z,p,m in SP_SAY)
    slides=[("spice-tolerance-china-can-you-handle-chongqing-hotpot-slide"),("spice-tolerance-china-mala-two-sensations-and-three-rules-slide"),("spice-tolerance-china-six-week-plan-ladder-slide"),("spice-tolerance-china-cool-it-down-foods-slide"),("spice-tolerance-china-order-like-a-pro-slide")]
    figs='<div class="shots sp-shots">'+"".join(f'<figure><a href="/img/{k}.jpg"><img src="/img/{k}.jpg" alt=""></a><figcaption>{html.escape(IMGREG[k+".jpg"]["cap"])}</figcaption></figure>' for k in slides)+'</div>'
    return f'''<section class="sp" id="cool"><div class="sp-head"><span class="sp-k">What to do when it burns</span><h2>Cool it down: what works and what does not</h2></div>
<p class="sp-lead">The burn comes from capsaicin, which dissolves in fat and oil, not in water. So the fixes are fat, protein, starch and sugar. Here is each one with how well it is backed up.</p>
<div class="sp-grid">{cool}</div>
<h3 class="sp-h3">Skip these</h3><div class="sp-grid">{avoid}</div></section>
<section class="sp" id="order"><div class="sp-head"><span class="sp-k">In China</span><h2>How to order mild in Chinese</h2></div>
<p class="sp-lead">Spice is a scale you pick when you order. Say your level, or point at it on the menu or the order screen.</p>
<div class="sp-tw"><table class="sp-t"><thead><tr><th>Chinese</th><th>Pinyin</th><th>Level</th><th>Good to know</th></tr></thead><tbody>{terms}</tbody></table></div>
<h3 class="sp-h3">Three things to say</h3><ul class="sp-say">{say}</ul>
<p class="sp-fine">These phrases are standard Mandarin that I wrote myself, not copied from a guide. Show them on your phone and check them in a translator app before you rely on them.</p>
<div class="sp-two"><div><h3 class="sp-h3">Chengdu or Chongqing first?</h3><p>China for Travelers describes Chongqing as the hotter style, with a beef tallow broth that concentrates heat and numbness, and Chengdu as lighter and moderate. On a trip that includes both, it suggests eating Chengdu first to calibrate, then Chongqing two or three days later. That is one source, but it matches the other guide's advice to start mild and work up.</p></div>
<div><h3 class="sp-h3">Vegetarian or avoiding beef?</h3><p>China for Travelers notes most Chongqing-style spicy broths use beef tallow, so vegetarians should order a pure mushroom broth.</p></div></div></section>
<section class="sp sp-safe" id="safety"><div class="sp-head"><span class="sp-k">Be sensible</span><h2>Safety: when to slow down</h2></div>
<p>Stop if it hurts or upsets your stomach, and do not treat a bigger burn as a win. If you get reflux, have ulcers or another stomach condition, ask your doctor before you start a spice plan. This is a food plan from a traveller, not medical advice.</p></section>
<h2>The five slides</h2><p>The same plan as a 5 slide carousel, to save for your trip. Tap a slide to open it larger.</p>{figs}'''

SP_INTRO='''<p>We are going to Chengdu and Chongqing in December, which means hotpot, and I wanted to be ready for it. The plan is simple: eat a little chilli, often, and raise the heat one step a week for six weeks. This guide explains why Sichuan and Chongqing food burns and numbs, what research says about tolerance, a 6 week plan, what actually cools the burn, and how to order mild in Chinese.</p>
<p>It is the written version of my Scratch &amp; Roam video and slides. The plan itself is mine. The facts were checked against the sources at the bottom on 26 October 2026, and where the evidence is thin I say so.</p>
<div class="sp-vid"><iframe src="https://www.youtube-nocookie.com/embed/c2Am9ktTUIM" title="Build spice tolerance before China in 6 weeks, a YouTube Short by Scratch and Roam" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe><p>The 47 second Short: <a href="https://youtube.com/shorts/c2Am9ktTUIM" rel="noopener">watch it on YouTube</a>.</p></div>
<h2 id="why">Why Sichuan and Chongqing food is hard on a first-timer</h2>
<p>The dish name <b>málà (麻辣)</b> joins two Chinese words for two different sensations: <b>má (麻), numbing</b>, and <b>là (辣), burning</b>. Your tongue has to cope with both at once, which is why training for only one of them is not enough.</p>
<p><b>The burn (là)</b> comes from capsaicin in chilli. It does not heat your mouth. It switches on a heat receptor, so your brain reads it as burning.</p>
<p><b>The numbness (má)</b> comes from Sichuan pepper. <i>The Takeout</i> (Dennis Lee, 18 January 2022) explains that its main compound, hydroxy-alpha-sanshool, causes a buzzing, tingling feeling, and cites a University College London study in which people matched the feeling on their lips to a vibration of about 50 Hz. The same article says the numbing can make the heat of the chillies easier to tolerate, which is part of why mala is so easy to keep eating.</p>
<h2 id="tolerance">Does spice tolerance really build?</h2>
<p>Yes, with repeated exposure, though the research is small. A 2023 study in <i>Physiology &amp; Behavior</i> (Nolden, Lenart, Spielman and Hayes) had volunteers rinse their mouths with a low dose of capsaicin twice a day for 14 days. Their perceived burn dropped by about 26 to 31 percent, while a control group did not change. A second group of 45 people had about 24 percent less burn after roughly 28 exposures.</p>
<p>Read that carefully. The participants were healthy adults aged 18 to 45 who rarely ate chilli, the study used a rinse and not meals, it did not test how long the effect lasts, and the authors suggest it may be better called reduced pain sensitivity than a changed taste. So the idea behind this plan, small and repeated exposure, has support. The exact six weeks and three times a week are my own plan, not a tested protocol. Treat it as a sensible build-up, not a promise.</p>'''

SP_FAQ=[("How do you build spice tolerance before China?","Eat a little chilli often and step up slowly: chilli flakes, then jalapeño or mild hot sauce, sriracha-level sauce, chilli oil, a pinch of Sichuan pepper, then a mild mala dish, about three times a week for six weeks. The steps below are my plan, based on research showing that repeated low-dose exposure reduces the burn."),
 ("How long does it take to build spice tolerance?","A 2023 study found about 26 to 31 percent less perceived burn after 14 days of twice-daily low-dose capsaicin rinses, and about 24 percent after roughly 28 exposures in a second group. That is a small study of healthy adults who rarely ate chilli, so six weeks here is a practical plan, not a guarantee."),
 ("What cools down spicy food best?","Dairy such as milk or yoghurt, starch such as rice or bread, and sugar or honey. Fat and oil also work, which is why Chongqing hotpot comes with a sesame oil dip and peanut milk. Cold water does not help because capsaicin is oil based."),
 ("Do lemon juice or vinegar help with spicy food?","Possibly a little, but the evidence is thin. Food Network says acids like vinegar, lemon and tomato may reduce the burn but it might take a lot, and one commercial spice blog says citrus does not meaningfully help. Try it, but keep dairy, rice or sugar nearby."),
 ("How do you order mild at a hotpot in China?","Say wēi là (微辣) for mild or bù là (不辣) for no spice, or order a split pot, yuānyāng guō (鸳鸯锅), with a mild half. Be careful: in Chongqing, 微辣 is roughly Chengdu's 中辣, so mild is not mild by Western standards."),
 ("Is Chongqing spicier than Chengdu?","According to China for Travelers, yes. Its Chongqing broth concentrates both heat and numbness, while Chengdu's is lighter. It suggests eating Chengdu first if you visit both cities.")]

SP_SOURCES=[("Nolden, Lenart, Spielman, Hayes: inducible desensitization to capsaicin with repeated low-dose exposure, Physiology &amp; Behavior, 2023","https://pmc.ncbi.nlm.nih.gov/articles/PMC10842799/",False),
 ("The Takeout, Dennis Lee: What's the buzz? Let's talk about numbing ingredients, 18 January 2022","https://thetakeout.com/foods-that-make-your-mouth-go-numb-sichuan-clove-buz-1848334167",False),
 ("China for Travelers: Chongqing vs Chengdu hot pot, foreigner's 2026 guide, updated 14 August 2026","https://chinafortravelers.com/guides/chongqing-vs-chengdu-hot-pot/",False),
 ("Baba goes China: foreigner's guide to hot pot, updated December 2024","https://www.babagoeschina.com/foreigners-guide-to-hot-pot/",False),
 ("Food Network: mouth on fire myths, what really cools your palate (undated)","https://www.foodnetwork.com/recipes/packages/spicy-foods/mouth-on-fire-myths--what-really-cools-your-palate-",False),
 ("Alibaba spice blog: does citrus help with spice? (commercial site, 13 January 2025)","https://spice.alibaba.com/spice-basics/does-citrus-help-with-spice",False)]

guide(SP_SLUG,"Build Spice Tolerance Before China: 6 Week Plan","How to build spice tolerance before China: a 6 week plan",
      "How to build spice tolerance before China: why mala burns and numbs, a 6 week plan, what actually cools the heat, and how to order mild in Chinese.",
      "build spice tolerance before china","c2Am9ktTUIM",SP_INTRO,
      SP_WEEKS,SP_FAQ,SP_SOURCES,SITE+"/og/build-spice-tolerance-before-china.jpg",
      related=[("/guides/china-dos-and-donts/","china-will-take-your-drone-15-dos-and-donts","15 RULES","China do's and don'ts: what not to bring, and what not to do"),
               ("/guides/first-time-in-china/","first-time-in-china-13-things-before-you-fly","GUIDE 13","First time in China: 13 things to set up before you fly"),
               ("/guides/china-before-you-fly-checklist/","china-before-you-fly-10-things-cover-16x9","10 THINGS","China first trip checklist: 10 things to sort before you fly")],
      checked="2026-10-26",published="2026-10-26",minutes="PT47S",upload="2026-10-26",shorts={"YouTube Short":"https://youtube.com/shorts/c2Am9ktTUIM"},steps_title="The 6 week spice plan",
      lift='<div class="bp-hero sp-hero"><img data-hero src="/img/build-spice-tolerance-before-china-cover-16x9.jpg" alt="" width="1280" height="720"></div>',
      extra=_sp_extra(),
      head='<style>@font-face{font-family:"SRInter";font-weight:600;font-display:swap;src:url(/fonts/sr-inter-600.woff2) format("woff2")}@font-face{font-family:"SRInter";font-weight:700;font-display:swap;src:url(/fonts/sr-inter-700.woff2) format("woff2")}@font-face{font-family:"SRInter";font-weight:800;font-display:swap;src:url(/fonts/sr-inter-800.woff2) format("woff2")}</style>')
