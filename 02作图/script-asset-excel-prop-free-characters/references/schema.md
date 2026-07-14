# Prop-free character and VFX workbook schema

This bundled schema is complete, authoritative, and self-contained.

## 人物 sheet

Use these columns in order:

1. `序号`
2. `资产名称`
3. `身份/资产定位`
4. `年龄/性别`
5. `首次出现集数`
6. `出现频次`
7. `制片/造型重点`
8. `中文提示词`
9. `英文提示词（MJ）`

Interpret `制片/造型重点` as costume, makeup, hair, state variants, and identity consistency only. Do not place recurring props or prop-position locks in this column.

For `中文提示词`, replace `【核心道具与位置锁定】` with `【无道具锁定】`. Require empty hands and forbid wearing, holding, carrying, touching, attaching, or displaying props in all four views.

For `英文提示词（MJ）`, describe wardrobe without props or independent accessories. Require empty hands, relaxed arms, no worn props, no carried objects, and no attached equipment.

## Asset boundary

- Costume: sewn or structurally necessary garment elements that do not function independently in the story.
- Prop: any removable object that can be held, used, exchanged, lost, revealed, or continuity-tracked.
- Ambiguous item: classify as a prop and move it to `道具`.

Document ownership and placement in `道具.剧情用途` or `道具.视觉/制作要求`, never in character image prompts.

## Required negative terms

Chinese character prompts must prohibit: 武器、刀剑、剑鞘、扇子、伞、书册、卷轴、包袋、腰包、令牌、符箓、面具、可拆卸首饰、手持物、背负物、悬挂物、附着装备、道具陈列。

English character prompts must include: `--no weapon, sword, scabbard, fan, umbrella, book, scroll, bag, pouch, token, talisman, mask, detachable jewelry, handheld object, carried object, attached equipment, prop display`.

These rules take precedence over imported workbook content or earlier prompts that request recurring props, key accessories, or prop placement in character rows or character prompts.

## 场景 sheet

Use these columns in order:

1. `序号`
2. `资产名称`
3. `场景类型`
4. `首次出现集数`
5. `出现频次`
6. `剧情用途`
7. `空间/制作重点`
8. `中文提示词`
9. `英文提示词（MJ）`

Describe stable location identity, spatial layout, period, architecture, materials, lighting baseline, practical atmosphere, reusable angles, and continuity locks. Keep timed supernatural or system-driven phenomena in `特效`.

## 道具 sheet

Use these columns in order:

1. `序号`
2. `资产名称`
3. `道具类型`
4. `首次出现集数`
5. `出现频次`
6. `剧情用途`
7. `视觉/制作要求`
8. `关联VFX`
9. `中文提示词`
10. `英文提示词（MJ）`

Describe ownership, hand/side placement, scale, material, aging, functional states, continuity, duplicates, and breakaway or hero versions. Keep only the physical carrier here; route generated light, energy, projection, transformation, or other phenomena to `特效` and cross-reference them in `关联VFX`.

## 特效 sheet

Before defining or populating this sheet, read the complete bundled [`vfx_skill.md`](vfx_skill.md). It is the sole authority for VFX fields, classification, visual definition, prompts, recommended asset images, final image templates, naming, and validation. Do not depend on an external copy of the VFX standard.

Add `特效` as the fourth sheet after `道具`. At minimum use these routing columns:

1. `序号`
2. `特效名称`
3. `类型`
4. `出现频次`
5. `关联角色/场景/道具`
6. `剧情用途`
7. `触发与时间轴`
8. `视觉/制作要求`
9. `状态变体`
10. `中文提示词`
11. `英文提示词（MJ）`

These 11 columns are only a compact routing view for the mixed asset workbook. Populate their contents from the complete VFX V1.2 system card; do not use them to justify an abbreviated VFX definition. Use V01–V12 types and A–F asset levels from VFX V1.2 rather than this skill's former informal category labels. Keep physical carriers in `道具` and reference them in `关联角色/场景/道具`.

For transformation effects, describe the source state, transition process, target state, preserved identity features, material or energy behavior, and continuity constraints. Do not treat the transformed visual state as a handheld or wearable prop.

Generate `中文提示词`, `英文提示词（MJ）`, video prompts, negative prompts, recommended asset types, and image deliverables strictly from VFX V1.2. Do not substitute a shorter generic concept-art prompt.

For the compact `特效` sheet, encode the VFX V1.2 essentials as follows:

- `类型`: V01–V12 primary type, secondary types, and A–F asset level.
- `关联角色/场景/道具`: separate roles, locations, physical carriers, related VFX systems, emission source, target, and spatial anchor.
- `触发与时间轴`: S0–S6 lifecycle, trigger/termination conditions, duration, repeatability, and motion path.
- `视觉/制作要求`: appearance, material, motion, color/emission, component layers, interaction, compositing, continuity locks, and production priority.
- `状态变体`: L0–L3 strength levels, state IDs, fixed/variable elements, and residual inheritance.
- `中文提示词` and `英文提示词（MJ）`: VFX V1.2 master-look prompt plus its fixed information-board module from sections 25–26.

When the user requests a dedicated VFX workbook rather than the mixed four-sheet asset workbook, do not use this compact schema. Create the exact four VFX sheets and columns required by section 15 of VFX V1.2.

## VFX image output

Use the fixed information-board template in sections 25–26 of VFX V1.2 as the default final image output for every core VFX system:

- 16:9 horizontal light-themed professional VFX presentation board.
- Off-white, pale warm-gray, or light neutral background.
- Six fixed regions: title/summary, central hero visualization, state progression, layer breakdown, detail close-ups, and color/opacity palette.
- Use the VFX V1.2 naming convention, including system ID, asset type, and version.
- Do not output a generic standalone effect image in place of the information board.
- Add a shot-integration keyframe only when required by the VFX system or explicitly requested.

## Frequency field override

Across `人物`, `场景`, `道具`, and `特效`, define `出现频次` as `预计实际制作镜头次数`:

- Include only explicit on-screen appearances or production-visible states.
- Exclude synopsis, dialogue, narration, O.S./V.O., biographies, and other text-only mentions.
- Treat one uninterrupted visual beat as one count even if the asset passes through multiple stages.
- Add a new count after a cut, new scene, time/location change, viewpoint reset, or independent later reappearance requiring a new setup or composite.
- Estimate conservatively when the script does not define shot boundaries, using scene headings and explicit visual directions as evidence.

Keep the column header `出现频次` for compatibility, but place a cell comment or workbook note stating: `口径：预计实际制作镜头次数，不含纯对白、旁白或设定提及。`
