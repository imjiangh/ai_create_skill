# Human-image review rubric

Use this order. A later-stage strength cannot compensate for an earlier-stage failure.

## 1. Structural integrity — gate

- one coherent skull and face plane;
- aligned eyes with intentional natural asymmetry;
- plausible neck, shoulders, rib cage, pelvis, limb length, joints, hands, and feet;
- correct occlusion, weight bearing, contact, gravity, and perspective;
- garment seams, closures, layers, hems, tension, and folds make constructional sense.

If this gate fails materially, regenerate or make a structural edit before polishing.

## 2. Identity stability — 25%

- facial proportions and distinctive traits;
- apparent age, body build, skin tone, hairline, hairstyle;
- stable wardrobe and accessories when references require them.

## 3. Composition and hierarchy — 20%

- crop and pose feel intentional;
- face/hands do not collide with frame or props accidentally;
- focal subject separates cleanly from background;
- detail and contrast decrease away from the focal area.

## 4. Lighting and optics — 20%

- coherent source direction and shadow logic;
- believable highlight rolloff and readable darks;
- depth of field follows a plausible focus plane;
- no cutout halo, synthetic rim light, fake bloom, or mismatched bokeh.
- the key-to-fill ratio preserves cheek, nose, eye-socket, and jaw volume; the face is not evenly flooded;
- forehead, nose, upper lip, and cheek highlights are localized, soft-edged, and not clipped or connected into a greasy mask.

## 5. Material credibility — 20%

- skin is neither waxy nor sandpaper-sharp;
- skin contains coherent low-frequency form and color, restrained mid-frequency texture, and sparse high-frequency detail at plausible scale;
- T-zone, cheeks, lips, and eye contours do not share one uniform gloss or texture treatment;
- pores and reflectance vary coherently by facial zone: nose, cheeks, eyelids, lips, jaw, and neck must not look stamped from one texture map;
- hair has volume, grouping, root direction, and controlled flyaways;
- textiles show weight, weave scale, drape, seams, and wear appropriate to the garment;
- jewelry and hard surfaces have stable geometry and physically plausible reflections.

## 6. Clean finish — 15%

- no duplicated anatomy, melted microforms, accidental text, watermark-like marks, borders, or collage residue;
- smooth gradients without dirty noise or banding;
- no excessive clarity, oversharpen halos, chromatic fringe, or uniform microcontrast;
- background is resolved but quieter than the subject.

## Decision labels

- **Deliver:** no structural failure; only invisible or stylistic minor issues.
- **Local repair:** one or two bounded defects; identity and composition already correct.
- **Regenerate:** anatomy, perspective, identity, pose, garment construction, or overall light is fundamentally wrong.
- **Change strategy:** the same defect survives two attempts or references conflict.

## Automatic rejection conditions

Reject rather than deliver when any of these is obvious:

- wrong aspect ratio for the requested asset or the person is too small to inspect;
- broad oily facial sheen, clipped forehead/nose highlights, or beauty-filter wax skin;
- flat frontal illumination that removes facial planes;
- generic smooth clothing without seams, weight, weave scale, or controlled folds;
- detail is created mainly by sharpening, noise, embossed texture, or indiscriminate microcontrast.

## Critique output

Return:

1. verdict: Deliver / Local repair / Regenerate / Change strategy;
2. the three highest-impact observations in priority order;
3. a causal repair instruction that preserves correct areas;
4. the revised model-ready prompt or edit instruction.

## Generation-loop iteration record

Before the single automatic correction pass, record each item in this format:

```text
Observed failure: [visible defect and location]
Benchmark gap: [which perceptual quality is missing]
Causal correction: [light, texture scale, roughness, focus, anatomy, construction, or composition change]
Preserve: [all currently correct regions and immutable requirements]
```

Rank observed defects, then select only the highest-impact one or two root causes for the correction prompt. Keep all lower-priority observations out of that pass. Never write vague items such as “make it more realistic,” “increase quality,” or “add more detail.”
