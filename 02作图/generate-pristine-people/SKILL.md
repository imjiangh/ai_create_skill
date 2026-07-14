---
name: generate-pristine-people
description: Generate, prompt, art-direct, critique, and iteratively repair high-fidelity AI images of people with pristine rendering, believable anatomy, clean materials, controlled detail, and native-looking finish. Use for portraits, fashion/editorial people, full-body characters, realistic or stylized human imagery, prompt conversion for GPT Image or Midjourney, reference-image reconstruction, image quality diagnosis, and targeted regeneration. Do not use for environment-only imagery, narrative breakdowns, video prompts, generic asset sheets, or merely adding empty quality buzzwords.
---

# Generate Pristine People

Create high-fidelity human images through an art-direction loop: define, prompt, generate, inspect, repair, and deliver. Optimize for structural truth, visual cleanliness, material credibility, and intentional detail—not maximum texture density.

## Pipeline handoff

When invoked by `visual-asset-pipeline`, act only on the assigned `C###` asset IDs. Treat `P01`, `S01`, `A01`, approved references, identity locks, body proportions, costume version, and aspect ratio as authoritative inputs. Return the generated/repaired asset paths, prompt version, inspection result, and unresolved identity risks to A02. Do not add independent props, rename assets, change story facts, or declare the S2 stage locked.

## Core standard

Treat “pristine” as all of the following:

- correct face, hands, anatomy, garment construction, gravity, and contact;
- clean tonal separation, controlled highlights, readable darks, and coherent color;
- real material response without plastic skin, crunchy pores, wiry hair, or embossed fabric;
- detail concentrated at the focal hierarchy, with quiet supporting areas;
- no accidental text, borders, collage layout, duplicated features, halos, dirty noise, or AI residue;
- a finished image that looks intentionally photographed, illustrated, or rendered in its declared medium.

Never equate fidelity with `8K`, `masterpiece`, indiscriminate sharpness, or long adjective chains.

For a single-person asset image, default to a **9:16 vertical, high-resolution, single-frame image** with the person large enough to inspect. Use 16:9 only when the user asks for horizontal composition. Never default to a wide canvas with a small full-body subject.

## Route the request

1. Identify the operation:
   - create from text;
   - create from reference image(s);
   - reverse-engineer a reference into a prompt;
   - critique an existing image;
   - repair or regenerate an existing image;
   - translate a prompt between GPT Image and Midjourney.
2. Identify the intended medium: photographic realism, polished commercial realism, painterly, illustration, 3D, or hybrid.
3. Identify framing: face close-up, portrait, half-body, three-quarter, full-body, group, or editorial composition.
4. Identify purpose before aesthetics:
   - **asset image:** neutral, inspectable, reusable, complete anatomy and wardrobe, no narrative atmosphere by default;
   - **narrative still:** emotional distance, motivated environment, selective occlusion, and story lighting are allowed;
   - **editorial image:** styling, graphic negative space, and deliberate pose may override neutral asset conventions.
5. Ask only for missing information that materially changes the result. Otherwise state compact assumptions and proceed.
6. Select model rules:
   - Read [references/gpt-image.md](references/gpt-image.md) for GPT Image generation or editing.
   - Read [references/midjourney.md](references/midjourney.md) for Midjourney prompts and parameters.
7. For critique or any second pass, read [references/review-rubric.md](references/review-rubric.md).
8. For every photographic person generation, critique, or repair, read [references/quality-benchmarks.md](references/quality-benchmarks.md) and compare against the bundled benchmark images. Treat them as quality references only, never as identity, wardrobe, content, pose, or composition references unless the user explicitly requests that.
9. For composition, detail allocation, materials, weathering, or symptom repair, read [references/detail-budget.md](references/detail-budget.md).

## Build the visual brief

Before writing the final prompt, resolve these layers:

1. **Identity:** age band, ancestry only when relevant, facial geometry, distinguishing traits, hair, body build, posture, expression.
2. **Wardrobe:** silhouette, construction, fit, layering, fabric, color, wear state, accessories.
3. **Composition:** subject count, crop, camera height, angle, pose, gaze, negative space, background separation.
4. **Lighting:** motivated source, size, direction, softness, contrast ratio, highlight behavior, background exposure.
5. **Optics or medium:** focal-length behavior, focus plane, depth of field, motion behavior, or illustration/render language.
6. **Material response:** skin translucency, natural tonal variation, hair grouping, fabric weave at appropriate scale, metal/wood/leather response.
7. **Finish:** clean color, restrained sharpening, intact edges, quiet non-focal regions.

Answer the lighting triad before prompting: What is the dominant light? From which direction and height does it arrive? Which facial and body regions form the continuous light and shadow masses? If these are unresolved, the lighting brief is incomplete.

Allocate detail as a limited budget. Name one primary high-detail zone and at most one secondary zone. Give important materials enough frame area to resolve; wording cannot recover detail from a tiny subject. Keep broad skin, cloth, and background regions quiet enough for local detail to read.

For full-body asset images, target 88–94% subject height while preserving the entire hair silhouette and footwear. Keep face size sufficient for inspection; if full-body framing makes the face too small, generate a separate portrait instead of a collage.

Do not invent identity-sensitive details when a supplied reference should control them. Distinguish reference roles explicitly: identity, pose, wardrobe, lighting, composition, or style.

## Write the prompt

Use positive, concrete instructions in this order:

`deliverable + subject identity + wardrobe + pose/action + composition + light + optics/medium + materials + finish + exclusions`

Keep each clause functional. Replace vague labels with visible evidence. For example, replace “luxurious” with the exact tailoring, textile, finish, palette, and lighting that make it luxurious.

Preserve three priority tiers:

- **Immutable:** identity, anatomy, subject count, required wardrobe, aspect ratio.
- **Directed:** pose, composition, light, palette, material behavior.
- **Flexible:** minor background detail and nonessential accents.

When the user wants a prompt, return:

1. final model-ready prompt;
2. reference-image instructions if applicable;
3. model parameters only when they add control;
4. a short negative/exclusion block only where the model benefits from it.

Do not expose internal deliberation or pad the response with prompt theory unless requested.

## Generate

When the user asks for an image, use the available image-generation tool. Include all supplied target images through the supported reference mechanism. Generate without reconfirmation unless a required reference is missing.

For a first generation, prioritize a stable base image over simultaneous extremes. Lock identity, anatomy, silhouette, light, and composition before demanding microscopic texture.

Treat the first generation as the intended deliverable, subject to the benchmark gate below. Do not generate a second image merely for incremental polish.

For photographic people, enforce a skin-lighting plan before generation:

- use one dominant shaped key, controlled fill, and negative fill or flags to preserve facial volume;
- keep forehead, nose, upper lip, and cheek highlights small, shaped, and below clipping;
- preserve cheek and jaw tonal gradients rather than flooding the face with frontal fill;
- request natural local color variation and subsurface softness, not uniformly glossy or uniformly matte skin;
- reject flat omnidirectional studio light, broad greasy shine, synthetic beauty-filter skin, and identical sharpness across every plane.

## Inspect and repair

Inspect the actual output, not merely the prompt. Evaluate at full image and local-detail scale using the review rubric.

Run the three-condition benchmark check before delivery:

- soft-light skin must retain believable facial form and local texture;
- directional or hard light must reveal microtexture without greasy clipping or crunchy sharpening;
- mixed materials must remain separately readable with a clear focal hierarchy.

Do not require every output to look like all three benchmark images. Require it to meet the relevant physical and perceptual qualities demonstrated by them.

### Conditional failure-repair loop

For every photographic person image:

1. Generate candidate 1.
2. Inspect the actual pixels at whole-image scale and face-detail scale. Compare only image-quality properties against all relevant bundled benchmarks; do not compare identity, styling, subject matter, or composition.
3. Decide whether candidate 1 passes or has a **hard failure**. Hard failures are limited to:
   - clearly broken face, hands, anatomy, perspective, or garment construction;
   - obvious identity, age, subject-count, framing, aspect-ratio, or required-content mismatch;
   - strongly oily, waxy, plastic, melted, or otherwise implausible skin/material rendering;
   - severe blur, focus failure, clipping, artifacting, or loss of the primary focal subject;
   - a core mismatch that makes the image unusable for the user's stated purpose.
4. If there is no hard failure, deliver candidate 1. Mild softness, slightly imperfect microtexture, small accessory defects, or opportunities for better color/detail are not grounds for automatic regeneration; mention them only when the response format permits critique.
5. If there is a hard failure, write a compact iteration list with observable failures and causal fixes. Cover only failed items, for example:
   - skin-zone texture distribution;
   - highlight size and oiliness;
   - facial-plane depth and key/fill balance;
   - focal sharpness and detail hierarchy;
   - hair, cloth, leather, metal, or glass separation;
   - anatomy or garment construction.
6. Rank failures by impact on the user's stated goal. Select only the top **one or two root causes** for the automatic correction. Record lower-priority issues but defer them; do not put them into the correction prompt.
7. Perform exactly one automatic targeted correction. Preserve every correct area and put only the selected one or two iteration points directly into the edit/regeneration instruction.
8. Inspect candidate 2 again. Deliver candidate 2 when it improves the selected criteria without damaging immutable requirements. If it regresses materially or merely changes exposure/color without solving the selected root causes, deliver the stronger candidate and state briefly that the automatic correction did not improve the result.

Default to one generation. Do not ask the user to approve a correction pass when a hard failure is present. Do not use a blind retry: every change must correspond to a selected iteration point. Never place more than two corrective goals in one automatic pass. Do not treat subject beauty, costume taste, minor polish opportunities, or style preference as a hard failure unless the user specified them as immutable requirements.

Classify each flaw by cause:

- **structural:** anatomy, perspective, pose, garment construction;
- **identity:** face drift, age drift, body drift, hair/accessory drift;
- **optical:** impossible focus, fake bokeh, mixed light, clipped highlights;
- **material:** plastic skin, metallic cloth, melted jewelry, wiry hair;
- **finish:** halos, oversharpening, dirty gradients, noise, compression-like residue;
- **design:** weak hierarchy, clutter, accidental tangencies, generic styling.

Repair by symptom before adding generic quality language:

- noisy or dirty: remove uniform high-frequency detail and correct shadow/color transitions;
- oily or plastic: correct specular size, distribution, roughness, and fill light;
- flat: reshape key/fill ratio and restore continuous facial-plane gradients;
- overdecorated: confine ornament or wear to named locations and restore clean large surfaces;
- muddy material: separate scale, roughness, edge behavior, and wear pattern by material.

Repair the smallest causal layer. Preserve everything already correct. For edits, explicitly list what must remain unchanged and what may change. Do not regenerate the entire concept to fix one local defect unless the defect is structural.

Never use blind retries. After a conditional single targeted correction, stop automatic iteration. If the same defect persists, report the remaining gap and recommend a changed control strategy: simplify the pose, alter crop, strengthen a reference, split identity and wardrobe passes, or switch model.

## Deliver

For generation, return only the generated image as required by the image tool. For prompt or critique work, lead with the usable result, followed by concise production notes. Mention uncertainty when a reference is too small, occluded, compressed, or visually contradictory.

Do not introduce story, lore, character sheets, turnarounds, labels, multi-panel layouts, film grain, fog, glow, or cinematic color grading unless requested or visually justified.
