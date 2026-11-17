#!/usr/bin/env python3
"""Parse 160-bai-code-thieu-nhi problems and sync to Codeforces Polygon."""

import argparse
import hashlib
import json
import os
import random
import re
import string
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK_DIR = ROOT / "work"
STATE_FILE = WORK_DIR / "state.json"
POLYGON_API_URL = "https://polygon.codeforces.com/api/"


def load_env(env_path: Path) -> None:
    if not env_path.is_file():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip())


def _escape_tt(text: str) -> str:
    """Escape LaTeX special chars inside \\t{...}."""
    for ch in ("\\", "{", "}", "$", "&", "#", "%", "_"):
        text = text.replace(ch, f"\\{ch}" if ch != "\\" else r"\textbackslash ")
    return text


def md_to_polygon_latex(text: str) -> str:
    """Convert Markdown prose + math into clean Polygon/Codeforces LaTeX."""
    if not text.strip():
        return ""

    parts = re.split(r"(\$\$.*?\$\$|\$.*?\$)", text, flags=re.DOTALL)
    converted_parts = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            part = part.replace(r"\_", "_").replace(r"\*", "*")
            converted_parts.append(part)
        else:
            part = re.sub(r"`([^`]+)`", lambda m: r"\t{" + _escape_tt(m.group(1)) + "}", part)
            part = re.sub(r"\*\*([^*]+)\*\*", r"\\textbf{\1}", part)
            part = re.sub(r"(?<!^)(?<!\n)\*([^*\n]+)\*", r"\\textit{\1}", part)
            part = re.sub(r'"([^"\n]+)"', r"``\1''", part)
            converted_parts.append(part)

    joined = "".join(converted_parts)

    out_lines = []
    in_list = False
    for line in joined.splitlines():
        m = re.match(r"^\s*[*-]\s+(.*)$", line)
        if m:
            if not in_list:
                out_lines.append(r"\begin{itemize}")
                in_list = True
            out_lines.append(rf"\item {m.group(1).strip()}")
        else:
            if in_list:
                out_lines.append(r"\end{itemize}")
                in_list = False
            out_lines.append(line)
    if in_list:
        out_lines.append(r"\end{itemize}")

    return "\n".join(out_lines).strip()


def parse_statement(md_text: str) -> dict:
    """Extract title, limits, Codeforces-formatted sections, and examples from statement_vi.md."""
    lines = md_text.splitlines()
    title = "Untitled"
    time_limit_ms = 1000
    memory_limit_mb = 256

    for line in lines:
        if line.startswith("# "):
            raw = line[2:].strip()
            title = raw.split(" - ", 1)[1].strip() if " - " in raw else raw
            break

    tl_match = re.search(r"\*\*(?:Time limit|Giới hạn thời gian):\*\*\s*([\d.]+)\s*s", md_text)
    if tl_match:
        time_limit_ms = int(float(tl_match.group(1)) * 1000)

    ml_match = re.search(r"\*\*(?:Memory limit|Giới hạn bộ nhớ):\*\*\s*(\d+)\s*MB", md_text)
    if ml_match:
        memory_limit_mb = int(ml_match.group(1))

    sections = {"legend": "", "input": "", "output": "", "constraints": ""}
    current = "legend"
    buf = []
    started = False
    example_start = len(lines)
    for idx, line in enumerate(lines):
        if not started:
            if line.startswith("# ") or line.startswith("* **"):
                continue
            if line.strip() == "":
                continue
            started = True

        s = line.strip()
        if s in ("# Input", "# Dữ liệu vào"):
            sections[current] = "\n".join(buf).strip()
            current, buf = "input", []
        elif s in ("# Output", "# Kết quả"):
            sections[current] = "\n".join(buf).strip()
            current, buf = "output", []
        elif s in ("# Constraints", "# Giới hạn"):
            sections[current] = "\n".join(buf).strip()
            current, buf = "constraints", []
        elif s.startswith("# Example") or s.startswith("# Ví dụ"):
            sections[current] = "\n".join(buf).strip()
            example_start = idx
            break
        else:
            buf.append(line)
    else:
        sections[current] = "\n".join(buf).strip()

    example_tail_lines = lines[example_start:]
    notes_start = len(example_tail_lines)
    for i, line in enumerate(example_tail_lines):
        if line.strip() in ("# Note", "# Notes", "# Giải thích", "# Ghi chú"):
            notes_start = i
            break

    example_only_tail = "\n".join(example_tail_lines[:notes_start])
    examples = re.findall(
        r"(?:Input|Dữ liệu vào):\s*```[^\n]*\n(.*?)```\s*(?:Output|Kết quả):\s*```[^\n]*\n(.*?)```",
        example_only_tail,
        flags=re.DOTALL,
    )
    examples = [(inp.strip("\n") + "\n", out.strip("\n") + "\n") for inp, out in examples]

    notes_raw = ""
    if notes_start < len(example_tail_lines):
        notes_raw = "\n".join(example_tail_lines[notes_start + 1:]).strip()
    else:
        expl_matches = re.findall(r"^(?:Explanation|Giải thích):\s*(.+)$", example_only_tail, flags=re.MULTILINE)
        if expl_matches:
            notes_raw = "\n\n".join(m.strip() for m in expl_matches)

    legend_tex = md_to_polygon_latex(sections["legend"])
    input_tex = md_to_polygon_latex(sections["input"])
    constraints_tex = md_to_polygon_latex(sections["constraints"])
    if constraints_tex:
        input_tex = f"{input_tex}\n\n{constraints_tex}".strip()
    output_tex = md_to_polygon_latex(sections["output"])
    notes_tex = md_to_polygon_latex(notes_raw)

    return {
        "title": title,
        "time_limit_ms": time_limit_ms,
        "memory_limit_mb": memory_limit_mb,
        "legend": legend_tex,
        "input": input_tex,
        "output": output_tex,
        "notes": notes_tex,
        "examples": examples,
    }


class PolygonClient:
    def __init__(self, api_key: str, api_secret: str) -> None:
        self.api_key = api_key
        self.api_secret = api_secret

    def call(self, method: str, params: dict | None = None) -> dict:
        payload = dict(params or {})
        payload["apiKey"] = self.api_key
        payload["time"] = str(int(time.time()))

        rand = "".join(random.choices(string.ascii_lowercase + string.digits, k=6))
        sorted_items = sorted((str(k), str(v)) for k, v in payload.items())
        sig_query = "&".join(f"{k}={v}" for k, v in sorted_items)
        sig_base = f"{rand}/{method}?{sig_query}#{self.api_secret}"
        api_sig = rand + hashlib.sha512(sig_base.encode("utf-8")).hexdigest()
        payload["apiSig"] = api_sig

        data = urllib.parse.urlencode(payload).encode("utf-8")
        backoffs = [5, 10, 20, 40, 60]
        for attempt in range(len(backoffs) + 1):
            req = urllib.request.Request(POLYGON_API_URL + method, data=data, method="POST")
            try:
                with urllib.request.urlopen(req, timeout=60) as resp:
                    body = json.loads(resp.read().decode("utf-8"))
                break
            except urllib.error.HTTPError as exc:
                err_body = exc.read().decode("utf-8", errors="replace")
                if exc.code in (429, 502, 503, 504) and attempt < len(backoffs):
                    wait = backoffs[attempt]
                    print(f"    [WARN] HTTP {exc.code} on {method}; retrying in {wait}s...")
                    time.sleep(wait)
                    continue
                raise RuntimeError(f"Polygon HTTP {exc.code} on {method}: {err_body}") from exc

        if body.get("status") != "OK":
            raise RuntimeError(f"Polygon API error on {method}: {body.get('comment', body)}")
        time.sleep(1.0)
        return body.get("result", {})


def load_state() -> dict:
    if STATE_FILE.is_file():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {"problems": {}}


def save_state(state: dict) -> None:
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")


def extract_tests(prob_dir: Path) -> list[tuple[int, str, str]]:
    """Return sorted list of (index, input_text, output_text) from tests_*.zip or tests/."""
    tests = {}
    zips = list(prob_dir.glob("tests_*.zip"))
    if zips:
        with zipfile.ZipFile(zips[0], "r") as zf:
            for name in zf.namelist():
                base = Path(name).name
                m = re.fullmatch(r"(\d+)\.(in|out)", base)
                if not m:
                    continue
                idx = int(m.group(1))
                ext = m.group(2)
                tests.setdefault(idx, {})[ext] = zf.read(name).decode("utf-8", errors="replace")
    elif (prob_dir / "tests").is_dir():
        for f in (prob_dir / "tests").iterdir():
            m = re.fullmatch(r"(\d+)\.(in|out)", f.name)
            if m:
                idx = int(m.group(1))
                ext = m.group(2)
                tests.setdefault(idx, {})[ext] = f.read_text(encoding="utf-8", errors="replace")

    result = []
    for idx in sorted(tests):
        pair = tests[idx]
        if "in" in pair and "out" in pair:
            result.append((idx, pair["in"], pair["out"]))
    return result


def _norm_test(s: str) -> str:
    return "\n".join(line.rstrip() for line in s.replace("\r\n", "\n").strip().splitlines())


def sync_tests(
    client: PolygonClient,
    polygon_id: int,
    tests: list[tuple[int, str, str]],
    examples: list[tuple[str, str]],
    updating: bool,
) -> None:
    num_samples = len(examples)
    existing_map: dict[int, tuple[str, bool]] = {}
    if updating:
        existing_list = client.call("problem.tests", {"problemId": polygon_id, "testset": "tests"})
        for t in existing_list:
            existing_map[int(t["index"])] = (_norm_test(t.get("input", "")), bool(t.get("useInStatements", False)))

    pending = {}
    for idx, inp, out in tests:
        use_sample = idx <= num_samples if num_samples > 0 else (idx == 1)
        norm_in = _norm_test(inp)
        if existing_map.get(idx) == (norm_in, use_sample):
            continue
        pending[idx] = (inp, out, norm_in, use_sample)

    # Save in collision-free order so testInput never coincides with another existing index
    while pending:
        progressed = False
        for idx in sorted(list(pending)):
            inp, out, norm_in, use_sample = pending[idx]
            collision = any(
                other_idx != idx and other_norm == norm_in
                for other_idx, (other_norm, _) in existing_map.items()
            )
            if collision:
                continue
            small_enough = (
                len(inp) <= 1000
                and len(out) <= 1000
                and inp.count("\n") <= 30
                and out.count("\n") <= 30
            )
            test_params = {
                "problemId": polygon_id,
                "testset": "tests",
                "testIndex": idx,
                "testInput": inp,
                "testUseInStatements": "true" if (use_sample and (small_enough or idx <= num_samples)) else "false",
            }
            if use_sample and not small_enough and idx <= num_samples:
                ex_in, ex_out = examples[idx - 1]
                test_params["testInputForStatements"] = ex_in
                test_params["testOutputForStatements"] = ex_out
            client.call("problem.saveTest", test_params)
            existing_map[idx] = (norm_in, use_sample)
            del pending[idx]
            progressed = True
        if not progressed:
            # Break swap cycle by temporarily putting a unique placeholder at the first pending index
            break_idx = sorted(pending)[0]
            tmp_in = f"__swap_tmp_{break_idx}_{random.randint(100000, 999999)}\n"
            client.call(
                "problem.saveTest",
                {
                    "problemId": polygon_id,
                    "testset": "tests",
                    "testIndex": break_idx,
                    "testInput": tmp_in,
                    "testUseInStatements": "false",
                },
            )
            existing_map[break_idx] = (_norm_test(tmp_in), False)


def sync_problem(
    prob_dir: Path,
    client: PolygonClient | None,
    state: dict,
    dry_run: bool,
    force_update: bool = False,
    target_rev: int = 0,
) -> None:
    prob_id_str = prob_dir.name.split("_", 1)[0]
    stmt_file = prob_dir / "statement_vi.md"
    stmt_lang = "vietnamese"
    if not stmt_file.is_file():
        stmt_file = prob_dir / "statement_en.md"
        stmt_lang = "english"
    if not stmt_file.is_file():
        print(f"  [SKIP] {prob_dir.name}: missing statement_vi.md / statement_en.md")
        return

    parsed = parse_statement(stmt_file.read_text(encoding="utf-8"))
    tests = extract_tests(prob_dir)
    has_checker = (prob_dir / "checker.cpp").is_file()
    has_solution = (prob_dir / "solution.cpp").is_file()

    slug = f"bctn-{prob_id_str}"
    print(
        f"  [{slug}] {parsed['title']} | TL={parsed['time_limit_ms']}ms "
        f"ML={parsed['memory_limit_mb']}MB | samples={len(parsed['examples'])} tests={len(tests)} "
        f"notes={'yes' if parsed['notes'] else 'no'} "
        f"checker={'custom' if has_checker else 'std::wcmp.cpp'} "
        f"sol={'yes' if has_solution else 'no'}"
    )

    if dry_run:
        return

    assert client is not None
    prob_state = state["problems"].get(prob_id_str, {})
    already_synced = prob_state.get("synced")
    cur_rev = prob_state.get("rev", 1)
    if already_synced and not force_update and (target_rev == 0 or cur_rev >= target_rev):
        print(f"    -> Already synced (Polygon ID {prob_state.get('polygon_id')}, rev={cur_rev}), skipping.")
        return

    polygon_id = prob_state.get("polygon_id")
    updating = bool(polygon_id)
    if not polygon_id:
        res = client.call("problem.create", {"name": slug})
        polygon_id = res["id"]
        prob_state["polygon_id"] = polygon_id
        state["problems"][prob_id_str] = prob_state
        save_state(state)
        print(f"    -> Created Polygon problem ID {polygon_id}")

    client.call(
        "problem.updateInfo",
        {
            "problemId": polygon_id,
            "timeLimit": parsed["time_limit_ms"],
            "memoryLimit": parsed["memory_limit_mb"],
        },
    )

    client.call(
        "problem.saveStatement",
        {
            "problemId": polygon_id,
            "lang": stmt_lang,
            "name": parsed["title"],
            "legend": parsed["legend"],
            "input": parsed["input"],
            "output": parsed["output"],
            "notes": parsed["notes"],
        },
    )

    if has_checker:
        checker_src = (prob_dir / "checker.cpp").read_text(encoding="utf-8")
        client.call(
            "problem.saveFile",
            {
                "problemId": polygon_id,
                "type": "source",
                "name": "checker.cpp",
                "file": checker_src,
            },
        )
        client.call("problem.setChecker", {"problemId": polygon_id, "checker": "checker.cpp"})
    else:
        client.call("problem.setChecker", {"problemId": polygon_id, "checker": "std::wcmp.cpp"})

    if has_solution:
        sol_src = (prob_dir / "solution.cpp").read_text(encoding="utf-8")
        client.call(
            "problem.saveSolution",
            {
                "problemId": polygon_id,
                "name": "solution.cpp",
                "file": sol_src,
                "sourceType": "cpp.g++17",
                "tag": "MA",
            },
        )

    if tests:
        sync_tests(client, polygon_id, tests, parsed["examples"], updating)
    elif parsed["examples"]:
        for idx, (ex_in, ex_out) in enumerate(parsed["examples"], start=1):
            client.call(
                "problem.saveTest",
                {
                    "problemId": polygon_id,
                    "testset": "tests",
                    "testIndex": idx,
                    "testInput": ex_in,
                    "testUseInStatements": "true",
                },
            )

    client.call(
        "problem.setAccess",
        {"problemId": polygon_id, "login": "codeforces", "accessType": "READ"},
    )
    client.call(
        "problem.commitChanges",
        {"problemId": polygon_id, "minorChanges": "true", "message": "Update improved statements, samples, notes, and tests"},
    )
    client.call("problem.buildPackage", {"problemId": polygon_id, "full": "true", "verify": "true"})

    prob_state["synced"] = True
    if target_rev > 0:
        prob_state["rev"] = target_rev
    state["problems"][prob_id_str] = prob_state
    save_state(state)
    print(f"    -> Synced (Polygon ID {polygon_id})")


def main() -> int:
    load_env(ROOT / ".env")

    parser = argparse.ArgumentParser(description="Sync 160-bai-code-thieu-nhi problems to Codeforces Polygon.")
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--category", help='Category folder name, e.g. "01_Basic_Problems"')
    target.add_argument("--all", action="store_true", help="Sync all 10 categories (all 160 problems)")
    parser.add_argument("--problem", help="Optional 3-digit problem ID prefix, e.g. 001")
    parser.add_argument("--update", action="store_true", help="Re-upload/update already synced problems")
    parser.add_argument("--rev", type=int, default=0, help="Target revision; updates problems with rev < N")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", default=True, help="Preview without calling Polygon (default)")
    mode.add_argument("--upload", action="store_true", help="Actually upload to Polygon")
    args = parser.parse_args()

    dry_run = not args.upload
    repo_dir = Path(os.environ.get("REPO_DIR", ROOT / "problems"))
    if args.all:
        cat_dirs = sorted(p for p in repo_dir.iterdir() if p.is_dir() and not p.name.startswith("."))
    else:
        cat_dir = repo_dir / args.category
        if not cat_dir.is_dir():
            print(f"Category not found: {cat_dir}")
            return 1
        cat_dirs = [cat_dir]

    client = None
    if not dry_run:
        key = os.environ.get("POLYGON_API_KEY", "")
        secret = os.environ.get("POLYGON_API_SECRET", "")
        if not key or not secret or "your_api_" in key:
            print("Set POLYGON_API_KEY and POLYGON_API_SECRET in .env before using --upload.")
            return 1
        client = PolygonClient(key, secret)

    state = load_state()
    for cat_dir in cat_dirs:
        probs = sorted(p for p in cat_dir.iterdir() if p.is_dir() and "_" in p.name)
        if args.problem:
            probs = [p for p in probs if p.name.startswith(f"{args.problem}_")]
        if not probs:
            continue
        print(f"Category: {cat_dir.name} ({len(probs)} problems) | mode={'DRY-RUN' if dry_run else 'UPLOAD'}")
        for prob_dir in probs:
            sync_problem(prob_dir, client, state, dry_run, force_update=args.update, target_rev=args.rev)

    return 0


if __name__ == "__main__":
    sys.exit(main())
