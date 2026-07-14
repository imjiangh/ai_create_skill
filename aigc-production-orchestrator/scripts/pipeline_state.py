#!/usr/bin/env python3
"""Create, validate, inspect, and update an AIGC production pipeline state file."""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import json
import os
import sys
import tempfile
from pathlib import Path


STAGES = ["S1_SCRIPT", "S2_ASSETS", "S3_STORYBOARD", "S4_VIDEO_PROMPTS"]
STAGE_STATUSES = {
    "not_started", "in_progress", "review", "locked",
    "needs_revision", "blocked", "not_applicable",
}
ARTIFACT_STATUSES = {
    "missing", "draft", "review", "locked", "needs_revision", "not_applicable",
}
ARTIFACT_STAGE = {
    "P01": "S1_SCRIPT", "S01": "S1_SCRIPT", "S02": "S1_SCRIPT",
    "A01": "S2_ASSETS", "A02": "S2_ASSETS", "A03": "S2_ASSETS",
    "A04": "S2_ASSETS", "A05": "S2_ASSETS",
    "B01": "S3_STORYBOARD", "B02": "S3_STORYBOARD", "B03": "S3_STORYBOARD",
    "V01": "S4_VIDEO_PROMPTS", "V02": "S4_VIDEO_PROMPTS", "V03": "S4_VIDEO_PROMPTS",
}
GATES = {
    "S1_SCRIPT": {"P01": {"locked"}, "S01": {"locked"}},
    "S2_ASSETS": {
        "A01": {"locked"},
        "A02": {"locked", "not_applicable"},
        "A03": {"locked", "not_applicable"},
        "A04": {"locked", "not_applicable"},
        "A05": {"locked", "not_applicable"},
    },
    "S3_STORYBOARD": {
        "B01": {"locked"}, "B02": {"locked"},
        "B03": {"locked", "not_applicable"},
    },
    "S4_VIDEO_PROMPTS": {
        "V01": {"locked"}, "V02": {"locked"}, "V03": {"locked"},
    },
}


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def new_state(project_id: str, title: str) -> dict:
    artifacts = {
        artifact_id: {"status": "missing", "version": "0.0", "path": "", "note": ""}
        for artifact_id in ARTIFACT_STAGE
    }
    return {
        "schema_version": "1.0",
        "project": {
            "id": project_id,
            "title": title,
            "format": "",
            "target_platform": "",
            "target_duration": "",
            "aspect_ratio": "",
            "authority": "LOCKED",
        },
        "current_stage": STAGES[0],
        "stages": {
            stage: {"status": "not_started", "revision": 0} for stage in STAGES
        },
        "artifacts": artifacts,
        "issues": [],
        "decisions": [],
        "change_log": [{"at": now(), "action": "initialized"}],
    }


def load_state(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def atomic_write(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(data, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        os.replace(temp_name, path)
    except Exception:
        try:
            os.unlink(temp_name)
        except OSError:
            pass
        raise


def validate(data: dict) -> list[str]:
    errors: list[str] = []
    if data.get("schema_version") != "1.0":
        errors.append("schema_version must be 1.0")
    project = data.get("project")
    if not isinstance(project, dict) or not project.get("id") or not project.get("title"):
        errors.append("project.id and project.title are required")
    stages = data.get("stages")
    if not isinstance(stages, dict):
        errors.append("stages must be an object")
        stages = {}
    active = 0
    for stage in STAGES:
        entry = stages.get(stage)
        if not isinstance(entry, dict):
            errors.append(f"missing stage {stage}")
            continue
        status = entry.get("status")
        if status not in STAGE_STATUSES:
            errors.append(f"invalid status for {stage}: {status}")
        if status == "in_progress":
            active += 1
    if active > 1:
        errors.append("only one stage may be in_progress")
    if data.get("current_stage") not in STAGES:
        errors.append("current_stage is invalid")
    artifacts = data.get("artifacts")
    if not isinstance(artifacts, dict):
        errors.append("artifacts must be an object")
        artifacts = {}
    for artifact_id in ARTIFACT_STAGE:
        entry = artifacts.get(artifact_id)
        if not isinstance(entry, dict):
            errors.append(f"missing artifact {artifact_id}")
            continue
        status = entry.get("status")
        if status not in ARTIFACT_STATUSES:
            errors.append(f"invalid status for {artifact_id}: {status}")
        if status == "locked" and not entry.get("path"):
            errors.append(f"locked artifact {artifact_id} must have a path")
    for stage in STAGES:
        if stages.get(stage, {}).get("status") == "locked":
            for upstream in STAGES[:STAGES.index(stage)]:
                upstream_status = stages.get(upstream, {}).get("status")
                if upstream_status not in {"locked", "not_applicable"}:
                    errors.append(
                        f"{stage} cannot be locked while upstream {upstream} is {upstream_status}"
                    )
            for artifact_id, allowed in GATES[stage].items():
                actual = artifacts.get(artifact_id, {}).get("status")
                if actual not in allowed:
                    errors.append(
                        f"{stage} cannot be locked: {artifact_id} is {actual}, expected {sorted(allowed)}"
                    )
    return errors


def gate_failures(data: dict, stage: str) -> list[str]:
    failures = []
    for artifact_id, allowed in GATES[stage].items():
        actual = data["artifacts"][artifact_id]["status"]
        if actual not in allowed:
            failures.append(f"{artifact_id}={actual} (need {'/'.join(sorted(allowed))})")
    return failures


def downstream_of(stage: str) -> list[str]:
    return STAGES[STAGES.index(stage) + 1:]


def first_unfinished_stage(data: dict):
    for stage in STAGES:
        if data["stages"][stage]["status"] not in {"locked", "not_applicable"}:
            return stage
    return None


def invalidate_downstream(data: dict, owner_stage: str, reason: str) -> None:
    for stage in downstream_of(owner_stage):
        if data["stages"][stage]["status"] not in {"not_started", "not_applicable"}:
            data["stages"][stage]["status"] = "needs_revision"
        for artifact_id, artifact_stage in ARTIFACT_STAGE.items():
            if artifact_stage == stage and data["artifacts"][artifact_id]["status"] == "locked":
                data["artifacts"][artifact_id]["status"] = "needs_revision"
                data["artifacts"][artifact_id]["note"] = reason


def cmd_init(args: argparse.Namespace) -> int:
    path = Path(args.output)
    if path.exists() and not args.force:
        print(f"ERROR: {path} already exists; use --force to replace", file=sys.stderr)
        return 2
    state = new_state(args.project_id, args.title)
    atomic_write(path, state)
    print(path)
    return 0


def cmd_check(args: argparse.Namespace) -> int:
    errors = validate(load_state(Path(args.state)))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("OK")
    return 0


def cmd_summary(args: argparse.Namespace) -> int:
    data = load_state(Path(args.state))
    errors = validate(data)
    project = data.get("project", {})
    print(f"{project.get('id', '?')} | {project.get('title', '?')}")
    print(f"current_stage: {data.get('current_stage')}")
    for stage in STAGES:
        entry = data.get("stages", {}).get(stage, {})
        failures = gate_failures(data, stage) if not errors else []
        suffix = "" if not failures else f" | gate: {', '.join(failures)}"
        print(f"{stage}: {entry.get('status')} r{entry.get('revision', 0)}{suffix}")
    open_issues = [i for i in data.get("issues", []) if i.get("status", "open") == "open"]
    print(f"open_issues: {len(open_issues)}")
    if errors:
        print(f"validation_errors: {len(errors)}")
        return 1
    return 0


def cmd_next(args: argparse.Namespace) -> int:
    data = load_state(Path(args.state))
    errors = validate(data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    for stage in STAGES:
        status = data["stages"][stage]["status"]
        if status not in {"locked", "not_applicable"}:
            failures = gate_failures(data, stage)
            print(stage)
            if failures:
                print("gate_missing: " + ", ".join(failures))
            return 0
    print("COMPLETE")
    return 0


def cmd_set_stage(args: argparse.Namespace) -> int:
    path = Path(args.state)
    data = load_state(path)
    if args.status == "locked":
        upstream_failures = [
            f"{stage}={data['stages'][stage]['status']}"
            for stage in STAGES[:STAGES.index(args.stage)]
            if data["stages"][stage]["status"] not in {"locked", "not_applicable"}
        ]
        if upstream_failures:
            print("ERROR: upstream not locked: " + ", ".join(upstream_failures), file=sys.stderr)
            return 2
        failures = gate_failures(data, args.stage)
        if failures:
            print("ERROR: gate failed: " + ", ".join(failures), file=sys.stderr)
            return 2
    before = copy.deepcopy(data["stages"][args.stage])
    if args.status == "in_progress":
        for stage in STAGES:
            if stage != args.stage and data["stages"][stage]["status"] == "in_progress":
                data["stages"][stage]["status"] = "review"
        data["current_stage"] = args.stage
    data["stages"][args.stage]["status"] = args.status
    data["stages"][args.stage]["revision"] = before.get("revision", 0) + 1
    if args.status in {"locked", "not_applicable"}:
        data["current_stage"] = first_unfinished_stage(data) or args.stage
    data["change_log"].append({
        "at": now(), "action": "set_stage", "stage": args.stage,
        "from": before.get("status"), "to": args.status,
    })
    errors = validate(data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 2
    atomic_write(path, data)
    print(f"{args.stage}={args.status}")
    return 0


def cmd_set_artifact(args: argparse.Namespace) -> int:
    path = Path(args.state)
    data = load_state(path)
    artifact = data["artifacts"][args.artifact]
    before = copy.deepcopy(artifact)
    artifact["status"] = args.status
    if args.version is not None:
        artifact["version"] = args.version
    if args.path is not None:
        artifact["path"] = args.path
    if args.note is not None:
        artifact["note"] = args.note
    owner_stage = ARTIFACT_STAGE[args.artifact]
    locked_content_changed = (
        before.get("status") == "locked"
        and (
            args.status != "locked"
            or (args.version is not None and args.version != before.get("version"))
            or (args.path is not None and args.path != before.get("path"))
        )
    )
    if before.get("status") == "locked" and args.status != "locked":
        if data["stages"][owner_stage]["status"] == "locked":
            data["stages"][owner_stage]["status"] = "needs_revision"
    if locked_content_changed:
        invalidate_downstream(data, owner_stage, f"{args.artifact} changed: {args.note or 'no note'}")
        data["current_stage"] = owner_stage
    data["change_log"].append({
        "at": now(), "action": "set_artifact", "artifact": args.artifact,
        "from": before.get("status"), "to": args.status,
    })
    errors = validate(data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 2
    atomic_write(path, data)
    print(f"{args.artifact}={args.status}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init")
    init.add_argument("--project-id", required=True)
    init.add_argument("--title", required=True)
    init.add_argument("--output", required=True)
    init.add_argument("--force", action="store_true")
    init.set_defaults(func=cmd_init)

    for name, func in (("check", cmd_check), ("summary", cmd_summary), ("next", cmd_next)):
        command = sub.add_parser(name)
        command.add_argument("state")
        command.set_defaults(func=func)

    set_stage = sub.add_parser("set-stage")
    set_stage.add_argument("state")
    set_stage.add_argument("stage", choices=STAGES)
    set_stage.add_argument("status", choices=sorted(STAGE_STATUSES))
    set_stage.set_defaults(func=cmd_set_stage)

    set_artifact = sub.add_parser("set-artifact")
    set_artifact.add_argument("state")
    set_artifact.add_argument("artifact", choices=sorted(ARTIFACT_STAGE))
    set_artifact.add_argument("status", choices=sorted(ARTIFACT_STATUSES))
    set_artifact.add_argument("--version")
    set_artifact.add_argument("--path")
    set_artifact.add_argument("--note")
    set_artifact.set_defaults(func=cmd_set_artifact)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
