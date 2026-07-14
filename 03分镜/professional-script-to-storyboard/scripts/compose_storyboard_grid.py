#!/usr/bin/env python3
"""Deterministically compose storyboard images into annotated PNG pages and PDF."""

import argparse, json, math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, JpegImagePlugin  # noqa: F401 - registers PDF raster encoder

def font(size, bold=False):
    roots = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for p in roots:
        if Path(p).exists():
            try: return ImageFont.truetype(p, size)
            except OSError: pass
    return ImageFont.load_default()

def fit(im, box, mode="contain"):
    w,h = box
    scale = max(w/im.width, h/im.height) if mode == "cover" else min(w/im.width, h/im.height)
    out = im.resize((max(1,int(im.width*scale)), max(1,int(im.height*scale))), Image.Resampling.LANCZOS)
    if mode == "cover":
        x=(out.width-w)//2; y=(out.height-h)//2; return out.crop((x,y,x+w,y+h))
    canvas=Image.new("RGB", box, "#eeeeee"); canvas.paste(out, ((w-out.width)//2,(h-out.height)//2)); return canvas

def arrow(draw, xy, dashed=False):
    x1,y1,x2,y2=xy
    if dashed:
        steps=8
        for i in range(0,steps,2):
            a=i/steps; b=(i+1)/steps
            draw.line((x1+(x2-x1)*a,y1+(y2-y1)*a,x1+(x2-x1)*b,y1+(y2-y1)*b),fill="black",width=4)
    else: draw.line(xy,fill="black",width=4)
    draw.polygon([(x2,y2),(x2-16,y2-9),(x2-16,y2+9)],fill="black")

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("manifest"); ap.add_argument("--preset",default="vertical-6")
    ap.add_argument("--out-dir",required=True); ap.add_argument("--fit",choices=["contain","cover"],default="contain")
    args=ap.parse_args(); data=json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    presets=json.loads((Path(__file__).parent.parent/"assets/storyboard-grid-presets.json").read_text())
    pr=presets[args.preset]; W,H=pr["page_size"]; cols,rows=pr["cols"],pr["rows"]; per=cols*rows
    margin,gap=pr["margin"],pr["gap"]; title_h=pr["title_h"]; cell_w=(W-2*margin-(cols-1)*gap)//cols; cell_h=(H-title_h-margin-(rows-1)*gap)//rows
    out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True); pages=[]
    for pi in range(math.ceil(len(data["shots"])/per)):
        page=Image.new("RGB",(W,H),"white"); d=ImageDraw.Draw(page); d.text((margin,18),data.get("title","Storyboard"),font=font(32,True),fill="black")
        for j,shot in enumerate(data["shots"][pi*per:(pi+1)*per]):
            c=j%cols; r=j//cols; x=margin+c*(cell_w+gap); y=title_h+r*(cell_h+gap)
            label_h=54; cap_h=86; img_h=cell_h-label_h-cap_h
            d.rectangle((x,y,x+cell_w,y+cell_h),outline="black",width=4)
            tc=shot.get("timecode","").replace("-","–"); d.text((x+12,y+10),f'{shot["display_id"]}  {tc}',font=font(22,True),fill="black")
            ip=Path(shot.get("image", ""))
            if ip.is_file(): im=fit(Image.open(ip).convert("RGB"),(cell_w-8,img_h),args.fit)
            else:
                im=Image.new("RGB",(cell_w-8,img_h),"#e8e8e8"); q=ImageDraw.Draw(im); q.text((20,img_h//2-14),f'MISSING: {shot["shot_id"]}',font=font(20,True),fill="#777777")
            page.paste(im,(x+4,y+label_h)); base=y+label_h+img_h
            action=shot.get("action","")[:90]; d.multiline_text((x+10,base+8),action,font=font(17),fill="black",spacing=4)
            if shot.get("character_direction") in {"left","right"}:
                if shot["character_direction"]=="right": arrow(d,(x+30,y+label_h+img_h-25,x+120,y+label_h+img_h-25))
                else: arrow(d,(x+120,y+label_h+img_h-25,x+30,y+label_h+img_h-25))
            if shot.get("camera_direction") in {"left","right"}:
                if shot["camera_direction"]=="right": arrow(d,(x+150,y+label_h+img_h-25,x+240,y+label_h+img_h-25),True)
                else: arrow(d,(x+240,y+label_h+img_h-25,x+150,y+label_h+img_h-25),True)
        d.text((W-margin-180,H-30),f"PAGE {pi+1}",font=font(16,True),fill="black")
        path=out/f"storyboard-page-{pi+1:02d}.png"; page.save(path); pages.append(page)
    if pages: pages[0].save(out/"storyboard-full.pdf",save_all=True,append_images=pages[1:],resolution=144)
    print(f"Wrote {len(pages)} pages and PDF to {out}")

if __name__=="__main__": main()
