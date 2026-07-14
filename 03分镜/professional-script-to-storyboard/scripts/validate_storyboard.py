#!/usr/bin/env python3
"""Validate a Markdown storyboard against the skill's minimum delivery contract."""

from __future__ import annotations

import argparse
import re
import statistics
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Tuple


CUT_HEADING = re.compile(r"^###\s+(S\d{2,}-B\d{2,}-C\d{2,}(?:-[a-z])?)\s*$", re.M)
BEAT_HEADING = re.compile(r"^###\s+(S\d{2,}-B\d{2,})(?:｜.*)?\s*$", re.M)
TIMECODE = re.compile(
    r"^成片时码：\s*(\d{2}):(\d{2})[.:](\d{3})\s*-\s*(\d{2}):(\d{2})[.:](\d{3})\s*$",
    re.M,
)
DURATION = re.compile(r"^成片时长：\s*(\d+(?:\.\d+)?)s\s*$", re.M)
LONG_SHOT_AUTH = re.compile(r"^长镜授权：\s*USER-REQUESTED\s*$", re.M)
REQUIRED_FIELDS = (
    "成片时码",
    "成片时长",
    "镜头功能",
    "镜头职责",
    "画面主体",
    "可见动作",
    "景别/角度/画幅构图",
    "第一视觉点",
    "第二视觉点",
    "构图设计",
    "视觉动线",
    "光色/景深",
    "台词/声音",
    "剪辑点",
    "承接",
    "连续性",
)
MOVEMENT_FIELDS = (
    "运镜强度",
    "运镜组合",
    "起点构图",
    "运动路径",
    "速度曲线",
    "运动终点",
    "主体运动关系",
    "运镜动机",
)


@dataclass
class Finding:
    severity: str
    location: str
    message: str


def ms(hh: str, mm: str, milli: str) -> int:
    return (int(hh) * 60 + int(mm)) * 1000 + int(milli)


def blocks(text: str) -> list[tuple[str, str]]:
    matches = list(CUT_HEADING.finditer(text))
    return [
        (match.group(1), text[match.end() : matches[i + 1].start() if i + 1 < len(matches) else len(text)])
        for i, match in enumerate(matches)
    ]


def beat_blocks(text: str) -> dict[str, str]:
    matches = list(BEAT_HEADING.finditer(text))
    return {
        match.group(1): text[match.end() : matches[i + 1].start() if i + 1 < len(matches) else len(text)]
        for i, match in enumerate(matches)
    }


def meaningful_field(block: str, field: str) -> Optional[str]:
    match = re.search(rf"^{re.escape(field)}：\s*(.*)$", block, re.M)
    if not match:
        return None
    value = match.group(1).strip()
    if value in {"", "无", "—", "-"}:
        return None
    return value


def validate(text: str) -> list[Finding]:
    findings: list[Finding] = []
    is_vertical = bool(re.search(r"^(?:-\s*)?画幅：\s*9\s*:\s*16(?:\s*竖屏)?\s*$", text, re.M))
    fast_commercial = bool(re.search(r"^(?:-\s*)?节奏风格：\s*COMMERCIAL_FAST\s*$", text, re.M))
    strict_short_form = is_vertical
    cut_blocks = blocks(text)
    if not cut_blocks:
        return [Finding("ERROR", "document", "未找到形如 S01-B01-C01 的三级镜号标题")]

    ids = [cut_id for cut_id, _ in cut_blocks]
    for cut_id in sorted(set(ids)):
        if ids.count(cut_id) > 1:
            findings.append(Finding("ERROR", cut_id, "镜号重复"))

    previous_end: Optional[int] = None
    total_declared = 0.0
    fixed_streak = 0
    fast_long_streak = 0
    fast_durations: list[float] = []
    fast_roles: list[str] = []
    previous_fast_signature: Optional[Tuple[str, str]] = None
    beat_cut_counts: Counter[str] = Counter()
    for cut_id, block in cut_blocks:
        beat_cut_counts[cut_id.rsplit("-C", 1)[0]] += 1
        for field in REQUIRED_FIELDS:
            match = re.search(rf"^{re.escape(field)}：\s*(.*)$", block, re.M)
            if not match:
                findings.append(Finding("ERROR", cut_id, f"缺少字段：{field}"))
            elif not match.group(1).strip():
                findings.append(Finding("ERROR", cut_id, f"字段为空：{field}"))

        role = re.search(r"^镜头职责：\s*(MASTER|SUPPORT|ACCENT|TRANSITION)\s*$", block, re.M)
        if not role:
            findings.append(Finding("ERROR", cut_id, "镜头职责必须使用 MASTER/SUPPORT/ACCENT/TRANSITION"))
        elif fast_commercial:
            fast_roles.append(role.group(1))

        if fast_commercial:
            function = meaningful_field(block, "镜头功能")
            contribution = meaningful_field(block, "节奏贡献")
            if contribution is None:
                findings.append(Finding("ERROR", cut_id, "COMMERCIAL_FAST 必须填写节奏贡献"))
            if function and contribution:
                signature = (function, contribution)
                if previous_fast_signature == signature:
                    findings.append(
                        Finding("WARN", cut_id, "与上一镜的镜头功能和节奏贡献完全相同；合并或说明新增强度/后果")
                    )
                previous_fast_signature = signature

        composition = re.search(r"^构图设计：\s*(.*)$", block, re.M)
        if composition and composition.group(1).strip() in {"三分法", "黄金分割", "中心构图", "对称", "好看"}:
            findings.append(Finding("WARN", cut_id, "构图描述过弱；补充重心、前中后景、线条/框架或留白功能"))

        eye_path = re.search(r"^视觉动线：\s*(.*)$", block, re.M)
        if eye_path and "→" not in eye_path.group(1):
            findings.append(Finding("WARN", cut_id, "视觉动线应写成第一视觉点 → 第二视觉点 → 切出方向"))

        legacy_movement = re.search(r"^运镜：\s*(.*)$", block, re.M)
        movement_values = {
            field: re.search(rf"^{re.escape(field)}：\s*(.*)$", block, re.M) for field in MOVEMENT_FIELDS
        }
        expanded_present = any(match for match in movement_values.values())
        if expanded_present:
            for field, match in movement_values.items():
                if not match:
                    findings.append(Finding("ERROR", cut_id, f"结构化运镜缺少字段：{field}"))
                elif not match.group(1).strip():
                    findings.append(Finding("ERROR", cut_id, f"结构化运镜字段为空：{field}"))
        elif not legacy_movement:
            findings.append(Finding("ERROR", cut_id, "缺少结构化运镜字段或兼容字段：运镜"))
        elif not legacy_movement.group(1).strip():
            findings.append(Finding("ERROR", cut_id, "字段为空：运镜"))
        elif legacy_movement.group(1).strip() in {"固定", "缓推", "跟拍", "摇摄", "横移", "手持"}:
            findings.append(Finding("WARN", cut_id, "运镜描述过弱；补充强度、组合、路径、速度、终点与动机"))

        movement_level = re.search(r"^运镜强度：\s*(M[0-4])\b", block, re.M)
        if expanded_present and not movement_level:
            findings.append(Finding("ERROR", cut_id, "运镜强度必须使用 M0-M4"))

        movement_text = legacy_movement.group(1).strip() if legacy_movement else ""
        is_fixed = bool((movement_level and movement_level.group(1) == "M0") or "固定" in movement_text or "M0" in movement_text)
        fixed_streak = fixed_streak + 1 if is_fixed else 0
        if fixed_streak == 3:
            findings.append(Finding("WARN", cut_id, "连续 3 个固定镜头；需说明节奏目的或增加有叙事动机的运动节点"))

        tc = TIMECODE.search(block)
        duration = DURATION.search(block)
        if tc:
            start = ms(*tc.groups()[:3])
            end = ms(*tc.groups()[3:])
            if end <= start:
                findings.append(Finding("ERROR", cut_id, "成片时码结束点必须晚于开始点"))
            if previous_end is not None and start < previous_end:
                findings.append(Finding("ERROR", cut_id, "成片时码与上一镜重叠或倒退"))
            elif previous_end is not None and start > previous_end:
                findings.append(Finding("WARN", cut_id, f"与上一镜存在 {(start - previous_end) / 1000:.3f}s 时码空隙"))
            previous_end = end
            if duration:
                declared = float(duration.group(1))
                total_declared += declared
                if fast_commercial:
                    fast_durations.append(declared)
                    fast_long_streak = fast_long_streak + 1 if declared >= 4.0 else 0
                    if fast_long_streak == 3:
                        findings.append(
                            Finding("WARN", cut_id, "COMMERCIAL_FAST 连续 3 镜均达到 4s；检查是否仍有等待已知结果")
                        )
                    if declared >= 6.0 and meaningful_field(block, "节奏豁免") is None:
                        findings.append(
                            Finding("ERROR", cut_id, f"COMMERCIAL_FAST 单镜 {declared:g}s 达到 6s；必须填写节奏豁免")
                        )
                if strict_short_form and declared >= 8.0:
                    if LONG_SHOT_AUTH.search(block):
                        findings.append(
                            Finding("WARN", cut_id, f"单镜 {declared:g}s 达到或超过 8s；已记录用户明确长镜授权")
                        )
                    else:
                        findings.append(
                            Finding(
                                "ERROR",
                                cut_id,
                                f"竖屏商业短剧单镜 {declared:g}s 达到或超过 8s；必须拆镜，除非长镜授权为 USER-REQUESTED",
                            )
                        )
                elif strict_short_form and declared >= 7.0:
                    findings.append(Finding("WARN", cut_id, f"竖屏商业短剧单镜 {declared:g}s；允许但必须复核节奏与 coverage"))
                elif declared > 8.0:
                    findings.append(Finding("WARN", cut_id, f"单镜 {declared:g}s 超过 8s；检查内部变化、长镜意图或拆分对白 coverage"))
                actual = (end - start) / 1000
                if abs(declared - actual) > 0.02:
                    findings.append(
                        Finding("ERROR", cut_id, f"声明时长 {declared:g}s 与时码时长 {actual:g}s 不一致")
                    )

        risk = re.search(r"^AI风险：\s*(L[1-4])\b(.*)$", block, re.M)
        fallback = re.search(r"^降级方案：\s*(.*)$", block, re.M)
        if risk and risk.group(1) in {"L3", "L4"}:
            if not fallback or fallback.group(1).strip() in {"", "无", "—", "-"}:
                findings.append(Finding("ERROR", cut_id, f"{risk.group(1)} 镜头必须提供降级方案"))
        if movement_level and movement_level.group(1) in {"M3", "M4"}:
            if risk and (not fallback or fallback.group(1).strip() in {"", "无", "—", "-"}):
                findings.append(Finding("ERROR", cut_id, f"{movement_level.group(1)} 组合运镜必须提供降级方案"))

    fixed_groups = re.finditer(r"^【G\d+｜固定\s*15(?:\.0)?s】(?P<body>.*?)(?=^【G\d+｜|\Z)", text, re.M | re.S)
    for group in fixed_groups:
        declared = re.search(r"^时长合计：\s*(\d+(?:\.\d+)?)s", group.group("body"), re.M)
        if not declared:
            findings.append(Finding("ERROR", group.group(0).splitlines()[0], "固定组缺少时长合计"))
        elif abs(float(declared.group(1)) - 15.0) > 0.02:
            findings.append(Finding("ERROR", group.group(0).splitlines()[0], "固定组时长必须为 15.0s"))

    if fast_commercial:
        beats = beat_blocks(text)
        for beat_id, cut_count in beat_cut_counts.items():
            beat = beats.get(beat_id)
            if beat is None:
                findings.append(Finding("ERROR", beat_id, "COMMERCIAL_FAST 缺少 Beat 卡"))
                continue
            if meaningful_field(beat, "镜头预算") is None:
                findings.append(Finding("ERROR", beat_id, "COMMERCIAL_FAST Beat 卡必须填写镜头预算"))
            if cut_count > 3 and meaningful_field(beat, "超预算理由") is None:
                findings.append(
                    Finding("ERROR", beat_id, f"COMMERCIAL_FAST 本 Beat 有 {cut_count} 镜；超过 3 镜必须填写超预算理由")
                )

        if fast_durations:
            average = sum(fast_durations) / len(fast_durations)
            median = statistics.median(fast_durations)
            if average > 3.5:
                findings.append(Finding("WARN", "document", f"COMMERCIAL_FAST 平均镜长 {average:.2f}s；建议复核信息密度"))
            if median > 3.5:
                findings.append(Finding("WARN", "document", f"COMMERCIAL_FAST 中位镜长 {median:.2f}s；多数镜头可能停留偏久"))
        if fast_roles:
            support_ratio = fast_roles.count("SUPPORT") / len(fast_roles)
            if support_ratio > 0.45:
                findings.append(
                    Finding("WARN", "document", f"COMMERCIAL_FAST SUPPORT 占比 {support_ratio:.0%}；检查反应、插入和建立镜是否过量")
                )

    if not any(f.severity == "ERROR" for f in findings):
        pace = ""
        if fast_commercial and fast_durations:
            pace = f"；平均镜长 {sum(fast_durations) / len(fast_durations):.2f}s，中位镜长 {statistics.median(fast_durations):.2f}s"
        findings.append(Finding("OK", "document", f"{len(cut_blocks)} 个镜头通过最低契约校验；声明总时长 {total_declared:g}s{pace}"))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("storyboard", type=Path, help="Markdown storyboard path")
    args = parser.parse_args()
    if not args.storyboard.is_file():
        print(f"ERROR document 文件不存在：{args.storyboard}")
        return 2
    findings = validate(args.storyboard.read_text(encoding="utf-8"))
    for finding in findings:
        print(f"{finding.severity} {finding.location} {finding.message}")
    return 1 if any(f.severity == "ERROR" for f in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
