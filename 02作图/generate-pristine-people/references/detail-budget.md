# Detail budget and corrective controls

## Detail allocation

Treat detail as a finite visual budget.

- Choose one primary high-detail zone: usually eyes/face, a key garment feature, or one held object.
- Allow at most one secondary detail zone.
- Keep non-focal skin, broad fabric panels, and background at lower microcontrast.
- Use large, medium, and small forms. Do not replace large construction with dense surface texture.
- Increase an important element's frame occupancy before expanding its prompt description.

For a full-body person asset, prioritize face, hairline, hands, neckline, closures, and garment construction. Do not demand beauty-close-up pore visibility over the entire body.

## Numeric constraints

Prefer measurable constraints when they materially reduce ambiguity:

- aspect ratio;
- subject height in frame;
- number and location of accessories;
- camera angle or approximate focal-length behavior;
- one dominant key direction and a deliberate fill ratio;
- one primary and at most one secondary detail zone.

Do not add fake precision. Use numbers only for quantities the model can perceive.

## Material separation

Define each important material by four properties:

1. scale and structure: weave, grain, pores, strands, seams;
2. roughness and highlight shape;
3. deformation: drape, compression, tension, bending, impact;
4. wear location: edges, folds, contact points, recesses, or exposed planes.

Avoid describing material only through color. Skin, cloth, leather, metal, glass, and stone must differ in physical response.

## Localized weathering

Use one wear anchor per material and specify its distribution. Examples:

- leather polish only at repeated hand-contact points;
- oxidation collected in metal recesses while raised planes remain cleaner;
- fraying limited to cloth hems and stressed seams;
- dust settled on upward-facing surfaces and inside folds.

Never spread “weathered,” “aged,” “dirty,” “worn,” and “grimy” uniformly across the whole image.

## Symptom repair

### Noise or dirty film

- reduce uniform microtexture and global clarity;
- restore smooth low-frequency gradients;
- retain intentional pores, fibers, wear, and grain only where physically justified;
- correct muddy midtones rather than erasing all texture.

### Oily or plastic skin

- shrink and localize highlights;
- restore matte-to-satin variation by facial zone;
- reduce frontal fill and preserve far-cheek modeling;
- keep pores subordinate to low-frequency form;
- never solve oiliness by making skin uniformly matte or blurred.

### Flat image

- choose one dominant light direction;
- introduce controlled negative fill;
- restore shadow gradients across eye socket, nose sidewall, cheek, jaw, neck, and garment folds;
- separate subject from background through tone and focus, not synthetic rim glow.

### Overdecorated or crunchy

- confine decoration to named panels, seams, jewelry, or focal objects;
- restore broad quiet surfaces;
- reduce stylization and sharpening before removing real construction detail.

### Muddy materials

- rewrite each material using structure, roughness, deformation, and wear location;
- fix reflections and edge behavior before adding texture words;
- preserve a single focal sharpness hierarchy.

## Exclusions

Do not use the following as substitutes for control:

- `8K`, `masterpiece`, `ultra detailed`, or repeated realism labels;
- “micro-wet skin” or global dewy/glass-skin language unless expressly requested;
- uniform butterfly light or equal bilateral fill for inspectable dimensional portraits;
- long universal cleanup paragraphs repeated after an already precise prompt;
- film grain, lens flaws, fog, or cinematic artifacts in neutral asset images unless requested.
