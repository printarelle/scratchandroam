# Draws the English labels on the real Taobao screenshots used in the guide.
# Source screenshots (src/shots_src/*.jpg) come from my own phone; the app is in Chinese, the labels are mine.
# Run: python3 src/make_shots.py   (build.py does not need to run it, the output is committed in docs/img/)
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
FONT='/usr/share/fonts/opentype/inter/Inter-Bold.otf'
F=ImageFont.truetype(FONT,44)
SRC='src/shots_src/'; OUT='docs/img/'
K=(17,17,17); SO=(239,75,35)
# (output name, source, [(x,y,text,mode)])  coordinates are in the 392x850 space used in the video, x2 here
SHOTS=[
 ("taobao-app-my-taobao-tab-and-settings-gear-english-labels","my",[(385,780,"My Taobao","r"),(385,135,"Settings","r")]),
 ("taobao-settings-country-language-currency-english-label","settings",[(28,319,"Country / Language / Currency","l")]),
 ("taobao-settings-delivery-address-english-label","settings",[(200,165,"Delivery address","l")]),
 ("taobao-language-country-currency-page-english-labels","lang",[(100,114,"Country / region","l"),(75,156,"Language","l"),(105,199,"Currency","l")]),
 ("taobao-currency-list-pick-euro-english-label","curr",[(215,204,"Pick EUR","l")]),
 ("taobao-euro-estimate-under-every-price-english-label","my2",[(60,724,"Euro estimate under every price","l")]),
 ("taobao-search-bar-english-label","srch1",[(40,105,"Search bar","l")]),
 ("taobao-search-type-in-english-labels","srch2",[(40,105,"Type it in English","l"),(352,105,"Search","r")]),
 ("taobao-add-new-address-button-english-label","addr",[(196,505,"Add new address","c")]),
 ("taobao-address-form-full-address-and-door-number-english-label","form",[(105,297,"Full address + door number","l")]),
 ("taobao-address-form-recipient-name-and-phone-english-labels","form",[(105,366,"Recipient name","l"),(140,441,"Phone number","l")]),
 ("taobao-product-options-phone-model-colour-add-to-cart-english-labels","opt",[(125,245,"Phone model","l"),(125,377,"Colour","l"),(196,745,"Add to cart","c")]),
 ("taobao-product-page-favourite-star-english-label","prod",[(118,745,"Favourite (star)","c")]),
 ("taobao-cart-tick-items-and-checkout-english-labels","cart",[(60,205,"Tick your items","l"),(300,780,"Checkout","c")]),
 ("taobao-checkout-popup-set-delivery-address-first-english-label","pop",[(196,250,"Set your delivery address first","c")]),
 ("taobao-my-orders-to-pay-to-ship-to-receive-refunds-english-labels","my2",[(95,261,"My orders","l"),(50,352,"To pay","c"),(125,392,"To ship","c"),(200,352,"To receive","c"),(325,392,"Refunds","c")]),
]
def tag(im,x,y,text,mode,fs=44):
    global F
    F=ImageFont.truetype(FONT,fs)
    x*=2;y*=2
    px=int(fs*.62);py=int(fs*.34);bw=int(fs*.24)
    d=ImageDraw.Draw(im,'RGBA')
    l,t,r,b=d.textbbox((0,0),text,font=F)
    w=(r-l)+2*px+bw; h=int(fs*.78)+2*py
    left={'l':x,'r':x-w,'c':x-w/2}[mode]; top=y-h/2
    left=max(10,min(left,im.width-w-10))
    sh=Image.new('RGBA',im.size,(0,0,0,0)); sd=ImageDraw.Draw(sh)
    sd.rounded_rectangle((left,top+6,left+w,top+h+6),radius=12,fill=(0,0,0,90)); sh=sh.filter(ImageFilter.GaussianBlur(8)); im.alpha_composite(sh)
    d=ImageDraw.Draw(im,'RGBA')
    d.rounded_rectangle((left,top,left+w,top+h),radius=12,fill=K+(255,))
    d.rounded_rectangle((left,top,left+bw+10,top+h),radius=12,fill=SO+(255,)); d.rectangle((left+bw,top,left+bw+14,top+h),fill=K+(255,))
    d.text((left+bw+px,top+py-l*0-t+ (h-2*py-(b-t))/2-2),text,font=F,fill=(255,255,255,255))
for name,src,tags in SHOTS:
    im=Image.open(SRC+src+'.jpg').convert('RGBA')
    for x,y,t,m in tags: tag(im,x,y,t,m,34 if len(tags)>=4 else 44)
    im=im.convert('RGB').resize((600,1301),Image.LANCZOS)
    im.save(OUT+name+'.jpg',quality=82,optimize=True,progressive=True)
    print(name, os.path.getsize(OUT+name+'.jpg')//1024,'KB')
