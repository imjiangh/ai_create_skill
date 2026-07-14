#!/usr/bin/env python3
"""Parse professional storyboard Markdown into a grid-compositor manifest."""

import argparse, json, re
from pathlib import Path

CUT = re.compile(r"^###\s+(S\d{2,}-B\d{2,}-C\d{2,}(?:-[a-z])?)\s*$", re.M)

def field(block, name, default=""):
    m = re.search(rf"^{re.escape(name)}：\s*(.*)$", block, re.M)
    return m.group(1).strip() if m else default

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("storyboard")
    ap.add_argument("--image-dir", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    text = Path(args.storyboard).read_text(encoding="utf-8")
    matches = list(CUT.finditer(text)); shots = []
    image_dir = Path(args.image_dir)
    for i, m in enumerate(matches):
        sid = m.group(1); block = text[m.end():matches[i+1].start() if i+1 < len(matches) else len(text)]
        tc = field(block, "成片时码")
        short = f"C{i + 1:02d}"
        candidates = [image_dir / f"{sid}{ext}" for ext in (".png", ".jpg", ".jpeg", ".webp")]
        image = next((str(p) for p in candidates if p.exists()), "")
        shots.append({
            "shot_id": sid, "display_id": short, "timecode": tc, "image": image,
            "action": field(block, "可见动作"), "sound": field(block, "台词/声音"),
            "movement": field(block, "运镜", field(block, "运动路径")),
            "character_direction": "", "camera_direction": ""
        })
    out = {"title": Path(args.storyboard).stem, "shots": shots}
    Path(args.out).write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(shots)} shots to {args.out}")

if __name__ == "__main__": main()
