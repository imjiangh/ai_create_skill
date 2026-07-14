#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from PIL import Image

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("manifest"); ap.add_argument("--output-dir"); args=ap.parse_args()
    data=json.loads(Path(args.manifest).read_text(encoding="utf-8")); ids=[s["shot_id"] for s in data.get("shots",[])]; errors=[]; warns=[]
    if not ids: errors.append("manifest 无镜头")
    if len(ids)!=len(set(ids)): errors.append("镜号重复")
    for s in data.get("shots",[]):
        if not s.get("image"): warns.append(f'{s["shot_id"]}: 缺少图片')
        elif not Path(s["image"]).is_file(): errors.append(f'{s["shot_id"]}: 图片不存在')
    if args.output_dir:
        pages=sorted(Path(args.output_dir).glob("storyboard-page-*.png"))
        if not pages: errors.append("未生成页面 PNG")
        for p in pages:
            try: Image.open(p).verify()
            except Exception as e: errors.append(f"{p.name}: {e}")
        if not (Path(args.output_dir)/"storyboard-full.pdf").is_file(): errors.append("未生成 PDF")
    for w in warns: print("WARN",w)
    for e in errors: print("ERROR",e)
    if not errors: print(f"OK {len(ids)} 个镜头；{len(warns)} 个警告")
    raise SystemExit(1 if errors else 0)
if __name__=="__main__": main()
