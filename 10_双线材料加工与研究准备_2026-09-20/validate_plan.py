#!/usr/bin/env python3
"""Read-only structural validation for the two-day planning package."""
from __future__ import annotations

import csv
from collections import defaultdict, deque
import json
from pathlib import Path
import re


BASE = Path(__file__).resolve().parent
REPO = BASE.parent


def read_tsv(name: str) -> tuple[list[str], list[list[str]]]:
    with (BASE / name).open(encoding="utf-8", newline="") as source:
        rows = list(csv.reader(source, delimiter="\t"))
    if not rows or not all(len(row) == len(rows[0]) for row in rows):
        raise AssertionError(f"{name}: inconsistent column count")
    for line_no, row in enumerate(rows, 1):
        for value in row:
            if value != value.strip():
                raise AssertionError(f"{name}:{line_no}: leading/trailing whitespace")
    return rows[0], rows[1:]


def unique_ids(label: str, rows: list[list[str]]) -> None:
    values = [row[0] for row in rows]
    if len(values) != len(set(values)):
        raise AssertionError(f"{label}: duplicate ID")


def dependency_order(tasks: list[list[str]]) -> list[str]:
    ids = {row[0] for row in tasks}
    graph: dict[str, list[str]] = defaultdict(list)
    indegree = {task_id: 0 for task_id in ids}
    for row in tasks:
        for dependency in [] if row[3] == "NONE" else row[3].split(";"):
            if dependency not in ids:
                raise AssertionError(f"{row[0]}: missing dependency {dependency}")
            graph[dependency].append(row[0])
            indegree[row[0]] += 1
    queue = deque(sorted(task_id for task_id, count in indegree.items() if count == 0))
    order: list[str] = []
    while queue:
        current = queue.popleft()
        order.append(current)
        for dependent in graph[current]:
            indegree[dependent] -= 1
            if indegree[dependent] == 0:
                queue.append(dependent)
    if len(order) != len(ids):
        raise AssertionError(f"dependency cycle: {sorted(ids - set(order))}")
    return order


def local_link_errors() -> list[tuple[str, str]]:
    errors: list[tuple[str, str]] = []
    for document in BASE.glob("*.md"):
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", document.read_text(encoding="utf-8")):
            target = target.split("#", 1)[0]
            if target and "://" not in target and not (document.parent / target).exists():
                errors.append((document.name, target))
    return errors


def main() -> None:
    task_header, tasks = read_tsv("03_两天任务看板.tsv")
    check_header, checks = read_tsv("04_验收检查表.tsv")
    source_header, sources = read_tsv("资料输入清单.tsv")
    if (len(tasks), len(checks), len(sources)) != (18, 25, 11):
        raise AssertionError("expected 18 tasks, 25 checks, and 11 sources")
    for label, rows in (("task", tasks), ("check", checks), ("source", sources)):
        unique_ids(label, rows)
    if [row[0] for row in checks] != [f"QC{number:02}" for number in range(1, 26)]:
        raise AssertionError("QC IDs must be contiguous QC01..QC25")
    if {row[9] for row in tasks} != {"PLANNED"}:
        raise AssertionError("every task must remain PLANNED before execution")
    if {row[6] for row in checks} != {"NOT_RUN"}:
        raise AssertionError("every check must remain NOT_RUN before execution")
    if {row[4] for row in sources} != {"FILES_FOUND"}:
        raise AssertionError("input manifest status changed")

    order = dependency_order(tasks)
    minutes = sum(int(row[7]) for row in tasks)
    if minutes != 1340:
        raise AssertionError(f"task budget changed: {minutes} != 1340")
    by_lane: dict[str, int] = defaultdict(int)
    for row in tasks:
        by_lane[row[1]] += int(row[7])

    missing_sources = [
        row[index]
        for row in sources
        for index in (2, 3)
        if not (REPO / row[index]).is_file()
    ]
    if missing_sources:
        raise AssertionError(f"missing source paths: {missing_sources}")
    broken_links = local_link_errors()
    if broken_links:
        raise AssertionError(f"broken local Markdown links: {broken_links}")

    contract = (BASE / "01_两天执行合同.md").read_text(encoding="utf-8")
    for acceptance_id in [f"AC{number:02}" for number in range(11)]:
        if acceptance_id not in contract:
            raise AssertionError(f"missing contract check {acceptance_id}")
    for check_id in [f"QC{number:02}" for number in range(1, 26)]:
        if not any(check_id in row[8] for row in tasks):
            raise AssertionError(f"task board does not reference {check_id}")
    learner_minutes = {
        day: sum(map(int, re.findall(rf"\| {day} 第\d块 (\d+)分钟", contract)))
        for day in ("D1", "D2")
    }
    if learner_minutes != {"D1": 260, "D2": 260}:
        raise AssertionError(f"learner schedule changed: {learner_minutes}")

    print(json.dumps({
        "result": "PLAN_STRUCTURE_PASS",
        "tsv_columns": {
            "tasks": len(task_header), "checks": len(check_header), "sources": len(source_header)
        },
        "counts": {
            "tasks": len(tasks), "checks": len(checks), "sources": len(sources),
            "source_paths_existing": len(sources) * 2,
        },
        "dependencies": "ACYCLIC",
        "topological_order": order,
        "task_minutes": minutes,
        "task_hours": round(minutes / 60, 2),
        "minutes_by_lane": dict(by_lane),
        "learner_minutes": {**learner_minutes, "total": sum(learner_minutes.values())},
        "states": {"tasks": "PLANNED", "checks": "NOT_RUN", "inputs": "FILES_FOUND"},
        "markdown_links": "PASS",
        "acceptance_references": "PASS",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
