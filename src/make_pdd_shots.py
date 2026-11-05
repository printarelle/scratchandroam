# Draws the red "press here" markers on my own Pinduoduo screenshots used in the Pinduoduo guide.
# Source frames (src/shots_src/pdd-*.jpg) are from my phone screen recording on 4 Nov 2026; the app is in Chinese,
# the English you see in the app is my phone's translation, the red boxes, numbers and labels are mine.
# Run: python3 src/make_pdd_shots.py   (build.py does not need to run it, the output is committed in docs/img/)
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
FONT='/usr/share/fonts/opentype/inter/Inter-Bold.otf'
SRC='src/shots_src/pdd-'; OUT='docs/img/'
RED=(239,75,35); INK=(17,17,17)
# (output name, source, [boxes (n,(x0,y0,x1,y1))], [pills (n,text,cx,cy)])  coordinates are in the 576x1252 frame
SHOTS=[
 ("pinduoduo-wechat-discover-tab-and-mini-programs-row-marked","wechat-discover",
   [(1,(285,1085,440,1192)),(2,(6,598,570,692))],[(1,"Tap Discover",150,1010),(2,"Then Mini Programs",300,770)]),
 ("pinduoduo-wechat-mini-programs-recently-used-marked","mp-list",
   [(1,(46,282,142,402)),(2,(8,143,568,202))],[(1,"Tap Pinduoduo",330,252)]),
 ("pinduoduo-wechat-search-pindu-result-marked","search-results",
   [(1,(8,138,568,238)),(2,(40,68,372,128))],[]),
 ("pinduoduo-mini-program-home-search-bar-marked","home",
   [(1,(15,76,412,126)),(2,(446,1092,576,1190))],[]),
 ("pinduoduo-search-type-in-english-field-and-search-button-marked","search-type",
   [(1,(12,138,498,202)),(2,(498,140,574,200))],[]),
 ("pinduoduo-product-page-saved-heart-marked","product-heart",
   [(1,(66,1100,152,1178))],[(1,"Tap the heart",420,1034)]),
 ("pinduoduo-home-personal-center-tab-marked","home-personal",
   [(1,(446,1092,576,1190))],[(1,"Personal Center",330,1064)]),
 ("pinduoduo-personal-center-product-favorites-marked","personal-center",
   [(1,(118,545,232,650))],[(1,"Product Favorites",430,150)]),
 ("pinduoduo-product-options-colour-capacity-and-confirm-marked","options",
   [(1,(18,622,562,710)),(2,(18,790,556,908)),(3,(0,1106,576,1182))],[]),
 ("pinduoduo-favorites-tick-items-and-proceed-to-checkout-marked","tick-checkout",
   [(1,(10,432,56,488)),(0,(10,676,56,730)),(2,(364,1104,576,1180))],[]),
 ("pinduoduo-checkout-weixin-pay-and-pay-immediately-marked","pay",
   [(1,(4,898,572,948)),(2,(378,1104,576,1182))],[]),
 ("pinduoduo-personal-center-my-orders-row-marked","orders",
   [(1,(6,333,570,500))],[]),
 ("pinduoduo-mini-program-three-dots-top-right-marked","translate-dots",
   [(1,(410,76,532,134))],[(1,"Tap the three dots",300,200)]),
 ("pinduoduo-mini-program-menu-translation-button-marked","translate-menu",
   [(1,(498,930,576,1080))],[(1,"Tap Translation",290,750)]),
 ("pinduoduo-store-page-established-store-genuine-and-flagship-marked","store-page",
   [(1,(100,282,400,322)),(2,(10,402,350,452)),(3,(8,474,340,526))],[]),
]
def box(im,b):
    n,(x0,y0,x1,y1)=b
    ov=Image.new('RGBA',im.size,(0,0,0,0)); d=ImageDraw.Draw(ov)
    d.rounded_rectangle((x0,y0,x1,y1),radius=16,fill=RED+(34,))
    d.rounded_rectangle((x0,y0,x1,y1),radius=16,outline=(255,255,255,235),width=12)
    d.rounded_rectangle((x0,y0,x1,y1),radius=16,outline=RED+(255,),width=6)
    im.alpha_composite(ov)
def badge(im,n,x,y,r=24):
    if not n: return
    d=ImageDraw.Draw(im,'RGBA'); f=ImageFont.truetype(FONT,30)
    d.ellipse((x-r-4,y-r-4,x+r+4,y+r+4),fill=(255,255,255,255))
    d.ellipse((x-r,y-r,x+r,y+r),fill=RED+(255,))
    d.text((x,y+1),str(n),font=f,fill=(255,255,255,255),anchor='mm')
def pill(im,n,text,cx,cy,fs=26):
    f=ImageFont.truetype(FONT,fs); d=ImageDraw.Draw(im,'RGBA')
    l,t,r,b=d.textbbox((0,0),text,font=f)
    pad=14; bw=46
    w=bw+(r-l)+2*pad; h=int(fs*1.25)+14
    left=max(8,min(cx-w/2,im.width-w-8)); top=cy-h/2
    sh=Image.new('RGBA',im.size,(0,0,0,0)); sd=ImageDraw.Draw(sh)
    sd.rounded_rectangle((left,top+5,left+w,top+h+5),radius=12,fill=(0,0,0,100)); sh=sh.filter(ImageFilter.GaussianBlur(7)); im.alpha_composite(sh)
    d=ImageDraw.Draw(im,'RGBA')
    d.rounded_rectangle((left,top,left+w,top+h),radius=12,fill=INK+(255,))
    d.rounded_rectangle((left,top,left+bw,top+h),radius=12,fill=RED+(255,)); d.rectangle((left+bw-12,top,left+bw,top+h),fill=RED+(255,))
    d.text((left+bw/2,top+h/2+1),str(n),font=ImageFont.truetype(FONT,fs+2),fill=(255,255,255,255),anchor='mm')
    d.text((left+bw+pad,top+h/2+1),text,font=f,fill=(255,255,255,255),anchor='lm')
for name,src,boxes,pills in SHOTS:
    im=Image.open(SRC+src+'.jpg').convert('RGBA')
    for b in boxes: box(im,b)
    for n,(x0,y0,x1,y1) in boxes: badge(im,n,max(28,x0+4),max(28,y0-2))
    for n,t,cx,cy in pills: pill(im,n,t,cx,cy)
    im=im.convert('RGB').resize((600,1305),Image.LANCZOS)
    im.save(OUT+name+'.jpg',quality=84,optimize=True,progressive=True)
    print(name,os.path.getsize(OUT+name+'.jpg')//1024,'KB')
