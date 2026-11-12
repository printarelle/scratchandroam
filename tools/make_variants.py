"""Make small WebP copies of every site image (run locally, then commit docs/img/*-w480.webp, -w640, -w800 and -w960).
The widths here must match VARIANT_W in build.py. 800 is the one a phone picks for a full-width photo (about 400 px wide at 2x).
build.py adds a srcset for each image that has these files. Needs Pillow."""
import glob, os
from PIL import Image
W=(480,640,800,960)
n=0
for f in sorted(glob.glob('docs/img/**/*.jpg',recursive=True)+glob.glob('docs/img/**/*.png',recursive=True)):
    stem,_=os.path.splitext(f)
    if stem.endswith(tuple(f'-w{w}' for w in W)): continue
    im=Image.open(f)
    for w in W:
        out=f'{stem}-w{w}.webp'
        if im.width<=w+40 or (os.path.exists(out) and os.path.getmtime(out)>=os.path.getmtime(f)): continue
        h=round(im.height*w/im.width)
        im.convert('RGB').resize((w,h),Image.LANCZOS).save(out,'WEBP',quality=70,method=6); n+=1
print('made',n)
