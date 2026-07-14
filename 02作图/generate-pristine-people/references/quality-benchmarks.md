# Quality benchmark set

## Purpose

Use these images as perceptual quality targets for photographic people. They define fidelity, skin credibility, local detail, and material separation. They do **not** define identity, attractiveness, body type, costume, genre, camera angle, or color palette.

Benchmark files:

- `assets/quality-benchmarks/benchmark-01-soft-natural-skin.jpeg`
- `assets/quality-benchmarks/benchmark-02-hardlight-material-detail.jpeg`
- `assets/quality-benchmarks/benchmark-03-mixed-material-clarity.jpeg`
- `assets/quality-benchmarks/benchmark-04-local-skin-zones.jpeg`
- `assets/quality-benchmarks/benchmark-05-whole-face-structure.jpeg`

Inspect the relevant file visually when judging an output. Do not infer the standard from filenames alone.

Benchmarks 04 and 05 are phone screenshots. Inspect only their embedded skin/detail imagery; ignore all interface chrome, typography, borders, layout, and screenshot compression. Never pass them to a generation model as undifferentiated style references.

## Benchmark 01 — soft natural skin

Use for soft-light portraits, historical people, beauty, and restrained cinematic realism.

Required qualities:

- smooth tonal transitions preserve forehead, eye socket, nose, cheek, lips, and jaw volume;
- skin reads as living tissue rather than wax, porcelain, plastic, or a pore texture overlay;
- local variation remains visible around eyes, nose, lips, and cheeks without dirty color noise;
- eyes, lips, hairline, and small flyaways are crisp enough to feel photographed while cheeks remain naturally softer;
- background softness does not create a cutout edge around the face or hair.

Do not mistake its restrained microtexture for blur or beauty-filter smoothing.

## Benchmark 02 — directional light and material detail

Use for outdoor portraits, fantasy characters, action-oriented people, exposed skin, weathered wardrobe, and strong sunlight.

Required qualities:

- directional light reveals facial and body microrelief without connecting highlights into a greasy film;
- pores, fine lines, sparse vellus hair, dust, sweat, or small imperfections appear irregularly and at plausible scale;
- hair resolves into large masses, smaller locks, and selective strands rather than a uniform fiber cloud;
- cloth fraying, seams, leather wear, metal edges, and skin each retain distinct material response;
- fine detail supports form and story of use; it is not simulated by uniform sharpening or noise.

## Benchmark 03 — mixed-material clarity

Use for close portraits with equipment, science fiction, eyewear, metal, glass, fabric, straps, and layered accessories.

Required qualities:

- facial skin remains credible beside highly detailed hard surfaces and is not sharpened to the same microcontrast;
- metal has stable geometry and controlled edge highlights; glass has thickness, reflection, dirt, and transparency appropriate to its angle;
- fabric and webbing show weave, compression, seams, abrasion, and load-bearing behavior;
- focus is selective: eyes/face and key equipment dominate, near and far objects fall off naturally;
- complex detail remains organized into readable large, medium, and small forms.

## Benchmark 04 — local facial zones

Use as a localized skin-detail checklist, not as a request for uniformly visible pores.

Required qualities by zone:

- **eyes:** wet tear line, fine lower-lid creases, individual lashes with irregular spacing, soft under-eye transition, and a coherent catchlight;
- **nose:** denser but restrained pore visibility around the sidewall and tip, soft-edged highlight shaped by the nose plane, no clipped oily stripe;
- **cheeks:** fine irregular pores that become subtler away from the focus/light, faint natural redness and tonal mottling without dirty noise;
- **lips:** individual vertical lip lines, moist inner lip and softer drier outer boundary, non-uniform color, no plastic gloss coating;
- **hairline and sideburns:** a large hair mass transitioning into fine baby hairs and a few flyaways, with believable root direction;
- **jaw and neck:** smooth form transition with sparse fine hair and subtle color change, not the same pore density as the nose or cheeks.

Do not list every zone at maximum intensity in one full-body prompt. Select details appropriate to subject scale and focus.

## Benchmark 05 — whole-face structure

Use to ensure local skin detail remains subordinate to a believable whole face.

Required qualities:

- facial planes remain readable before pores are noticed;
- natural light produces continuous gradients across forehead, eye sockets, nose, cheeks, lips, jaw, and neck;
- skin includes slight hue and value variation rather than one uniform beige layer;
- a small number of loose hairs cross or frame the face without becoming a tangled fiber overlay;
- shallow depth of field remains optical and progressive, with eyes and nearby facial planes carrying the strongest information;
- natural asymmetry and small imperfections remain; retouching is invisible rather than absent or excessive.

## Comparative acceptance test

Before delivering, answer these internally:

1. At normal viewing size, does the person have more presence and dimensionality than a generic AI portrait?
2. At face-detail size, is skin structured in low, mid, and high spatial frequencies without wax, oil mask, pore stamping, or sandpaper clarity?
3. Are highlights shaped by geometry and light direction rather than painted uniformly across the skin?
4. Are hair, skin, cloth, leather, metal, and glass distinguishable by physical response rather than color alone?
5. Does sharpness follow the focus plane and hierarchy, or is everything equally crisp?
6. Would the image remain convincing if generic quality words were removed from its prompt?
7. Does each facial zone have its own plausible texture and reflectance, rather than one global skin treatment?

Fail delivery if answers 2, 3, 4, or 7 are no. Repair or regenerate according to the review rubric.

## Prompt translation

Translate the benchmark into observable controls, for example:

- `natural low-frequency facial color and form`
- `irregular anatomically scaled pores and follicle transitions`
- `sparse vellus hair visible only where light catches it`
- `small shaped non-clipped specular highlights`
- `large hair masses, grouped locks, selective flyaways`
- `distinct skin, cloth, leather, glass, and metal response`
- `selective focus and restrained local sharpening`

Never write “match benchmark quality” as the only instruction. Models need the visible properties spelled out.
