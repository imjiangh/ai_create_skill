# GPT Image workflow

## Prompt behavior

- Write natural, explicit production instructions rather than tag clouds.
- State the deliverable and hierarchy early: one person, intended crop, background, and visual medium.
- Use spatial language: left/right, foreground/background, camera height, gaze direction, subject scale.
- Describe reference roles individually when multiple images are supplied.
- For editing, separate `preserve exactly` from `change only` instructions.
- Prefer observable traits over aesthetic buzzwords.

## Base prompt pattern

```text
Create [deliverable]. Default single-person asset: 9:16 vertical, one image, high-resolution, subject fills 88–94% of frame height.
Subject: [identity geometry, body, hair, expression].
Wardrobe: [construction, fit, fabric, color, accessories].
Composition: [crop, pose, camera angle, negative space, background].
Lighting and optics: [one shaped dominant key, controlled fill ratio, negative fill, highlight placement, lens behavior, focus].
Surface behavior: [skin microrelief and local color variation, controlled specular shape, hair grouping, cloth construction, hard materials at realistic scale].
Finish: [clean tonal transitions, restrained sharpening, coherent edges and color].
Exclude: [only likely, material failure modes].
```

## Reference pattern

```text
Use image 1 only for facial identity and hairline.
Use image 2 only for pose and framing.
Use image 3 only for garment construction and palette.
Do not inherit image 2's face or image 3's lighting.
```

## Targeted edit pattern

```text
Preserve exactly: face identity, expression, pose, crop, clothing design, lighting, background, and color balance.
Change only: [specific defect and desired visible correction].
Make the correction physically coherent with the existing perspective, light, material, and anatomy. Do not redesign unaffected areas.
```

## Practical rules

- Establish identity and large forms before micro-detail.
- For realistic skin, describe three separate layers: low-frequency facial form and color variation; mid-frequency pores, shallow lines, and follicle transitions; sparse high-frequency vellus hair and tiny imperfections. Keep each at anatomically plausible scale.
- Distribute detail by facial zone rather than globally: finer irregular cheek pores, slightly denser nose pores, lower-lid micro-creases and wet line, structured lip lines, sparse jaw/neck hair, and hairline baby hairs. Mention only zones visible at the requested crop.
- Keep pores subordinate to facial form. Do not request every pore sharp, uniform pore stamping, beauty-filter smoothing, frequency-separation wax, or global clarity.
- Specify controlled, non-clipped specular highlights: narrow and soft-edged on the forehead, nose bridge/tip, cupid's bow, and upper cheek only where the key light supports them. Avoid a continuous greasy sheen across the face.
- Preserve natural matte-to-satin variation: slightly more reflective T-zone, softer cheeks, subtly drier lip and eye contours. Do not make the entire face equally glossy.
- Use a shaped key 30–60 degrees off axis, restrained fill, and negative fill on the far cheek to retain bone structure. Avoid frontal two-sided fill that erases facial volume.
- For hair, request coherent masses, natural strand breakup at the silhouette, and believable root direction.
- For fabric, describe weight, drape, seam construction, tension points, and fold scale.
- If a result is too CG-like, correct lighting, skin specularity, edge uniformity, and material response before adding more texture.
- In 9:16 full-body work, keep the actor large in frame. Do not trade inspectability for empty negative space.
- Use a new full generation for global anatomy or composition failure; use editing for local, well-bounded defects.
