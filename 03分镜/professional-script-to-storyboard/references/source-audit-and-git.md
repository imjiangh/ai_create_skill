# 来源审计与 Git 维护规范

## 目录

1. 本地来源审计
2. 规则取舍
3. Git 工作流
4. 版本策略
5. 回归测试

## 1. 本地来源审计

本 Skill 基于当前目录六份既有文档重构：

| 来源 | 主要保留能力 | 已修正问题 |
|---|---|---|
| `05_0剧本转分镜.md` | 三级运镜、动作绑定、方向连续性 | 与 `05_1` 完全重复；运镜字段过重 |
| `05_1 分镜转宫格图.md` | 无新增能力 | 文件名声称宫格图但内容与 `05_0` 字节级相同；本 Skill 另建 GRID 规范 |
| `05_0剧本转分镜15秒组版.md` | 原文锁定、15 秒组、容量、五层连续性、AI 降级 | 把 15 秒从全局定律改为条件式制作容器 |
| `戏剧功能与三层衔接增强版 v1.2` | 镜头功能、表演字段、coverage、衔接三层 | 取消“台词镜/反应镜必须机械成对”；保留选择性 coverage |
| `SKILL5.0_Core` | 视听转译、演员/观众双视角、情绪锚点、主辅快切分工、默认值继承、镜头价值四问 | 去除固定情境 ID 与伪精确参数，避免平台耦合 |
| `SKILL5.0_ReferenceManual` | 构图词典、情绪/呼吸、动作六层、运镜与类型参考 | 重构为构图美学、表演动作和组合运镜模块；不把词表当强制模板 |

用户回归反馈显示初版对稳定性与连续性的约束强于动态摄影，容易输出“安全但平”的镜头。当前版本新增 `camera-movement-grammar.md`，把运镜从单一名称升级为运动强度、单镜组合、跨镜运动句法、动态视差、运动终点和 AI 降级系统。

第二轮回归反馈显示初版只要求“景别/角度/构图”单行字段，没有把注意力层级、视觉动线、光色、景深、负空间与跨镜构图弧线系统化。当前版本新增 `composition-and-visual-design.md` 与 `performance-action-and-validation.md`，补回两份“凡是皆可”文档中此前未充分吸收的精华。

## 2. 规则取舍

冲突时使用以下优先级：

1. 用户明确要求；
2. 原剧本事实和台词属性；
3. 可读的戏剧因果与空间连续性；
4. 可拍、可剪、可生成；
5. 项目风格；
6. 模板完整性。

不得为了填满字段、固定镜数、固定格数或固定时长破坏更高优先级。

## 3. Git 工作流

Skill 升级建议在独立 topic branch 完成：

```text
skill/pro-storyboard-<topic>
```

提交按单一意图拆分，推荐前缀：

- `feat:` 新能力；
- `fix:` 修正规则或脚本；
- `refactor:` 重组而不改变行为；
- `test:` 新增回归样例或验证；
- `docs:` 仅改参考说明。

提交前执行：

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py professional-script-to-storyboard
python3 professional-script-to-storyboard/scripts/validate_storyboard.py sample.md
git diff --check
git diff -- professional-script-to-storyboard
```

不自动提交、推送、建分支或打标签；只有用户明确要求时执行这些 Git 写操作。

## 4. 版本策略

使用语义化版本思路，但不在 `SKILL.md` frontmatter 添加非标准字段：

- PATCH：措辞修复、校验错误修复、不改变输出契约；
- MINOR：新增可选模式、字段或参考模块，保持旧用法可用；
- MAJOR：镜号、字段、默认模式或工作流发生不兼容变化。

正式发布使用 annotated tag，例如 `professional-script-to-storyboard-v1.0.0`。已发布标签不重写；修复后创建新版本标签。Git 官方文档说明 annotated tags 更适合 release：https://git-scm.com/docs/git-tag.html

GitHub 协作时用 topic branch 和 pull request 让差异可审查；GitHub 官方文档将 PR 定义为把分支变更合入目标分支的提案：https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests

## 5. 回归测试

每次影响行为的修改至少验证以下用例：

1. 双人室内对话：检查轴线、反应镜与台词属性；
2. 15 秒台词超载：不得改词，必须跨组或报告；
3. 多人动作：检查地理重建、动作相位与 AI 降级；
4. 情绪重场：抽象心理必须转成可见/可听事实；
5. 竖屏短剧：检查竖构图、钩子与信息可读性；
6. 宫格图：每格能追溯到稳定镜号；
7. 有意越轴/跳切：必须有目的与恢复锚点；
8. 长篇分批输出：镜号和状态账本跨批次连续。

不要把既有参考文档直接复制为测试答案；使用新剧本片段检查技能能否泛化。
