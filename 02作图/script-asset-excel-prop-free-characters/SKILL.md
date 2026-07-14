---
name: script-asset-excel-prop-free-characters
description: Extract production-ready character, environment, prop, and VFX inventories from Chinese scripts and generate a four-sheet Excel workbook with Chinese image prompts and pure-English Midjourney prompts. Use when character assets must remain neutral and video-consistent by showing no worn, carried, held, or attached props; keep plot props in 道具 and transformations, magic, effects, and other non-physical visual systems in 特效, with all VFX definitions, prompts, asset types, presentation boards, and image deliverables governed by the project VFX V1.2 standard.
---

# Script Asset Excel — Prop-Free Characters

## Pipeline handoff

When invoked by `visual-asset-pipeline`, perform the S2 extraction and classification pass before any image generation. Treat `P01@locked` and `S01@locked` as source authority; return A01 plus A02–A05 definitions, stable asset IDs, source scenes, variants, and ambiguity notes. Do not silently rewrite the script, generate final stage-lock status, or merge removable plot objects into character imagery. The parent pipeline owns generation order, cross-asset review, and locking.

## Core rule

Generate a self-contained four-sheet asset workbook and enforce one non-negotiable rule: **人物资产图 must not wear, carry, hold, touch, or display any prop.** Apply this rule to individual characters, groups, every Chinese role-card view, and every English MJ character image.

Read the bundled [`references/schema.md`](references/schema.md) for the complete workbook columns and field rules. This skill and its bundled references are authoritative and self-contained.

For any task that identifies, summarizes, writes prompts for, generates images for, or delivers VFX assets, **read the complete bundled [`references/vfx_skill.md`](references/vfx_skill.md) before acting.** Treat this bundled reference as the sole authoritative VFX specification. Do not search for or depend on an external VFX standard file. If this skill, `references/schema.md`, an existing workbook, or an earlier prompt conflicts with `references/vfx_skill.md` on a VFX matter, `references/vfx_skill.md` wins.

## VFX authority contract

- Use this skill only to detect VFX instances, separate them from physical props and environments, estimate visible production-shot frequency, and route them into `特效`.
- Use the VFX V1.2 standard for system merging/splitting, V01–V12 classification, A–F asset levels, S0–S6 lifecycle, L0–L3 intensity, system cards, component layers, interaction, compositing, continuity, naming, prompts, negative prompts, and validation.
- Do not shorten a VFX definition to a generic effect description when the VFX V1.2 system-card fields can be completed from the script.
- Do not invent a separate VFX prompt template, background rule, board layout, image ratio, delivery sequence, or naming convention inside this skill.
- When generating the four-sheet production workbook, keep the overall sheet order `人物`, `场景`, `道具`, `特效`; populate `特效` as a project-level VFX system inventory using the VFX V1.2 field definitions. If a dedicated VFX workbook is requested, use the four dedicated VFX sheets defined in section 15 of VFX V1.2 instead.
- When generating VFX images, default to the fixed light-themed information-board template in sections 25–26 of VFX V1.2. For core systems, deliver the fixed information board first and add a shot-integration keyframe only when needed or requested.
- Preserve the VFX V1.2 file's exact prompt modules and final-output template behavior; adapt placeholders to the current script without weakening or silently omitting required sections.

## Workflow overrides

1. Extract characters, environments, props, and VFX systems. Create exactly four sheets in this order: `人物`, `场景`, `道具`, `特效`.
2. Record character-bound and plot-driving objects only in the `道具` sheet. Describe their owner, story use, hand/side placement, and state variations there.
3. In the `人物` sheet, retain costume, hair, makeup, body, and identity locks, but remove prop placement, handling, wearing, and attachment instructions.
4. Treat removable narrative objects as props, even when commonly worn: weapons, scabbards, fans, umbrellas, books, scrolls, tokens, seals, pouches, medicine kits, prayer beads, talismans, masks, detachable jewelry used as a clue, and similar items.
5. Allow only costume construction and non-removable styling: garments, shoes, belts as garment structure, buttons, closures, sewn trim, hairstyle, and makeup. If an item can be independently picked up, exchanged, lost, used, or tracked by continuity, classify it as a prop and exclude it from character imagery.
6. When classification is ambiguous, prefer excluding the item from the character image and documenting it in `道具`.

## VFX extraction and separation

- Put non-physical visual systems in `特效`, including transformations or manifestations, magic and skills, energy fields, auras, light effects, particles, smoke generated by abilities, portals, shields, holograms, supernatural weather, environmental anomalies, disappearance or teleportation, healing, damage, and state-transition effects.
- Do not put VFX systems in `道具`, even when the script describes them with object-like nouns such as 光球, 光幕, 能量链, 法阵, or 虚影.
- Keep a physical emitter, weapon, talisman, machine, device, or other touchable carrier in `道具`; put the light, energy, projection, transformation, or phenomenon it produces in `特效`. Cross-reference the two rows without merging them.
- Keep ordinary practical atmosphere in `场景` when it is a stable part of the location. Move it to `特效` when it appears, changes, reacts, or disappears as a timed plot event.
- Split one effect into state variants when production must distinguish stages such as 起势, 形成, 爆发, 命中, 消散, or pre-change/post-change appearance.
- Merge repeated manifestations of the same effect and count estimated production shots, not textual mentions. Apply the production-shot counting rules below and sort `特效` by numeric frequency descending.
- After extraction, hand every VFX row to the VFX V1.2 workflow; do not treat the short extraction description as its final visual definition.

## Production-shot frequency

Interpret every sheet's `出现频次` as **estimated actual production-shot count**, not word, dialogue, paragraph, scene, or episode frequency.

- Count 1 when the script explicitly requires the asset or effect to be visible in a shot, including action lines, subjective views, inserts, reaction reveals with the asset visible, and clearly specified state changes shown on screen.
- Do not count dialogue, O.S., V.O., narration, synopsis, character biography, or explanatory references when the asset/effect is only mentioned and not shown.
- Count a continuous shot or uninterrupted visual beat as 1 even when it contains several sequential stages, such as gathering→activation→impact→dissipation. Record those stages in the state/timeline field instead of inflating frequency.
- Count again after an explicit shot cut, scene change, time jump, location change, viewpoint reset, or a later independent reappearance that requires a new setup or composite.
- Count separate simultaneous assets individually when each needs its own design, practical setup, animation, or compositing layer; do not multiply one asset merely because several characters observe it.
- For recurring background environments, count distinct scripted scene uses that require that environment setup. For characters and props, count visible shot uses rather than name mentions, while merging consecutive coverage that belongs to one continuous production beat when the script does not specify separate shots.
- When shot boundaries are ambiguous, estimate conservatively from explicit `△画面`, `画面切换`, inserts, entrances/reveals, and scene headings. Prefer a defensible lower count and note the uncertainty in the relevant production field.
- Before delivery, spot-check every frequency against the source script and ensure the number can be traced to visible production beats.

## Prompt rules

### Chinese character prompts

- Keep the locked pure-white 1×4 horizontal role card: left complete frontal head close-up; right front/side/back body-and-costume views.
- Replace `【核心道具与位置锁定】` with `【无道具锁定】`.
- State explicitly: 人物不佩戴、不手持、不携带、不背负、不触碰任何道具；双手自然放松且保持空手；腰间、背部、肩部、手腕和服装外侧不得悬挂或固定独立物件；画面内不得陈列角色专属道具。
- Add negative restrictions for weapons, scabbards, handheld objects, bags, pouches, books, scrolls, fans, umbrellas, tokens, talismans, masks, detachable jewelry, and unexplained accessories.

### English MJ character prompts

- Keep a single front-facing full-body 9:16 casting image on a clean white background.
- Require: `empty hands, relaxed natural arms, no worn props, no carried objects, no attached equipment, no character-specific objects in frame`.
- Include strong exclusions: `--no weapon, sword, scabbard, fan, umbrella, book, scroll, bag, pouch, token, talisman, mask, detachable jewelry, handheld object, carried object, attached equipment, prop display`.
- Keep all English prompts fully English and retain `--ar 9:16 --style raw --s 100`.

## Validation

Before delivery, inspect every row in `人物`:

- No prop appears in positive wording.
- Hands are explicitly empty.
- No independent object is attached to the waist, back, shoulder, wrist, or costume exterior.
- Chinese and English negative prompts both forbid props.
- Any removed narrative object exists in `道具` when production still needs it.
- Scene and prop prompts follow the bundled schema and the prompt rules in this skill.
- Every transformation, magic, skill visualization, energy phenomenon, and timed VFX event is present in `特效`, not `道具`.
- Physical carriers and their generated effects are split into linked `道具` and `特效` rows.
- `出现频次` counts visible production shots only; no row inflates frequency with dialogue or narrative mentions.
- Every VFX row satisfies the complete VFX V1.2 system definition and points to VFX V1.2-compliant prompt and recommended image assets.
- Every generated VFX image uses the VFX V1.2 fixed information-board template unless the user explicitly requests another template.

Create exactly `人物`, `场景`, `道具`, and `特效` in that order, sort every sheet by numeric frequency descending, save under `outputs/`, and visually verify the workbook.
