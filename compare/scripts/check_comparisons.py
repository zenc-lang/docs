#!/usr/bin/env python3
"""
Robust comparison checker for Zen C vs C comparison files.

For each file, extracts Zen C and C code blocks, then:
1. Compiles Zen C code with zc
2. Transpiles Zen C to C with zc
3. Compiles transpiled C with gcc
4. Compiles hand-written C code with gcc
5. Runs all three binaries and compares output against the
   expected output in the '## Output' section.

Usage:
    python3 compare/scripts/check_comparisons.py [files...]
"""

import os
import re
import sys
import subprocess
import tempfile
import glob

GCC_BIN = "gcc"


def find_zc():
    candidates = [
        "./zc", "../zc",
        "/usr/local/bin/zc",
        os.path.expanduser("~/zc"),
    ]
    for c in candidates:
        if os.path.isfile(c) and os.access(c, os.X_OK):
            return os.path.abspath(c)
    return "zc"


def extract_blocks(filepath):
    blocks = []
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    in_block, lang, code_lines = False, None, []
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith("```") and not in_block:
            lang = s[3:].strip()
            if lang in ("zc", "zenc", "c"):
                in_block, code_lines = True, []
        elif s.startswith("```") and in_block:
            code = "".join(code_lines).strip()
            if code:
                blocks.append((i + 2, lang, code))
            in_block, lang = False, None
        elif in_block:
            code_lines.append(line)
    return blocks


def compile_c(code, outfile):
    with tempfile.NamedTemporaryFile(suffix=".c", mode="w", delete=False) as f:
        f.write(code)
        tmpfile = f.name
    try:
        r = subprocess.run([GCC_BIN, "-std=c11", "-Wall", "-o", outfile, tmpfile],
                           capture_output=True, text=True, timeout=30)
        return (r.returncode == 0, r.stderr)
    finally:
        os.unlink(tmpfile)


def compile_zc(code, outfile):
    zc = find_zc()
    with tempfile.NamedTemporaryFile(suffix=".zc", mode="w", delete=False) as f:
        f.write(code)
        tmpfile = f.name
    try:
        r = subprocess.run([zc, "build", tmpfile, "-o", outfile],
                           capture_output=True, text=True, timeout=30)
        return (r.returncode == 0, r.stderr)
    finally:
        os.unlink(tmpfile)


def transpile_zc(code, out_c_file):
    zc = find_zc()
    with tempfile.NamedTemporaryFile(suffix=".zc", mode="w", delete=False) as f:
        f.write(code)
        tmpfile = f.name
    try:
        r = subprocess.run([zc, "transpile", tmpfile, "-o", out_c_file],
                           capture_output=True, text=True, timeout=30)
        return (r.returncode == 0, r.stderr)
    finally:
        os.unlink(tmpfile)


def run_binary(binary, timeout=10):
    try:
        r = subprocess.run([binary], capture_output=True, text=True, timeout=timeout)
        return (True, r.stdout, r.stderr)
    except subprocess.TimeoutExpired:
        return (False, "", "timeout")
    except OSError as e:
        return (False, "", str(e))


def normalize_output(text):
    """Strip trailing whitespace per line, remove trailing blank lines."""
    lines = text.split("\n")
    stripped = [l.rstrip() for l in lines]
    while stripped and stripped[-1] == "":
        stripped.pop()
    return "\n".join(stripped)


def extract_expected(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    m = re.search(r"## Output\s*\n(.*?)(?:\n## |\n```|\Z)", content, re.DOTALL)
    if m and m.group(1).strip():
        return normalize_output(m.group(1).strip())
    return None


def check_file(filepath):
    relpath = os.path.relpath(filepath)
    expected = extract_expected(filepath)
    blocks = extract_blocks(filepath)

    zc_blocks = [(l, c) for l, lang, c in blocks if lang in ("zc", "zenc")]
    c_blocks = [(l, c) for l, lang, c in blocks if lang == "c"]

    if not zc_blocks:
        return ("skip", "no ZC blocks")

    errors = []

    with tempfile.TemporaryDirectory() as td:
        for lineno, zc_code in zc_blocks:
            if len(zc_code) > 3000:
                continue

            zc_out = os.path.join(td, "zc_out")
            transpile_c = os.path.join(td, "zc_t.c")
            transpile_out = os.path.join(td, "tc_out")

            ok, err = compile_zc(zc_code, zc_out)
            if not ok:
                errors.append(f"{relpath}:{lineno}: ZC compile failed\n{err[:300]}")
                continue

            ok, err = transpile_zc(zc_code, transpile_c)
            if not ok:
                errors.append(f"{relpath}:{lineno}: ZC transpile failed\n{err[:300]}")
                continue

            c_compiles = True
            try:
                with open(transpile_c) as f:
                    tc_code = f.read()
            except OSError:
                errors.append(f"{relpath}:{lineno}: could not read transpiled C")
                continue

            ok, err = compile_c(tc_code, transpile_out)
            if not ok:
                errors.append(f"{relpath}:{lineno}: transpiled C compile failed\n{err[:300]}")
                c_compiles = False

            ok, stdout_zc, stderr = run_binary(zc_out)
            if not ok:
                errors.append(f"{relpath}:{lineno}: ZC binary failed: {stderr}")
                continue
            zc_out_norm = normalize_output(stdout_zc)

            if c_compiles:
                ok, stdout_tc, stderr = run_binary(transpile_out)
                if not ok:
                    errors.append(f"{relpath}:{lineno}: transpiled C run failed: {stderr}")
                else:
                    tc_out_norm = normalize_output(stdout_tc)
                    if zc_out_norm != tc_out_norm:
                        errors.append(
                            f"{relpath}:{lineno}: ZC vs transpiled C output differ\n"
                            f"  ZC:  {zc_out_norm!r}\n"
                            f"  TC:  {tc_out_norm!r}"
                        )

            if expected is not None and zc_out_norm != expected:
                errors.append(
                    f"{relpath}:{lineno}: output != expected\n"
                    f"  Expected: {expected!r}\n"
                    f"  Got:      {zc_out_norm!r}"
                )

            for clineno, c_code in c_blocks:
                if len(c_code) > 3000:
                    continue
                if "main" not in c_code:
                    continue

                c_out = os.path.join(td, "c_out")
                ok, err = compile_c(c_code, c_out)
                if not ok:
                    errors.append(f"{relpath}:{clineno}: C compile failed\n{err[:300]}")
                    continue

                ok, stdout_c, stderr = run_binary(c_out)
                if not ok:
                    errors.append(f"{relpath}:{clineno}: C binary failed: {stderr}")
                    continue
                c_out_norm = normalize_output(stdout_c)

                if expected is not None and c_out_norm != expected:
                    errors.append(
                        f"{relpath}:{clineno}: C output != expected\n"
                        f"  Expected: {expected!r}\n"
                        f"  Got:      {c_out_norm!r}"
                    )

    failed = len(errors)
    for err in errors:
        print(f"::error::{err}")

    if failed > 0:
        return ("fail", errors[0][:200] if errors else "?")
    return ("pass", "")


def main():
    files = sys.argv[1:]
    if not files:
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        files = glob.glob(os.path.join(base, "language", "*.md")) + glob.glob(
            os.path.join(base, "stdlib", "*.md")
        )
        files.sort()

    if not files:
        print("No comparison files found.")
        sys.exit(0)

    total, passed, failed, skipped = 0, 0, 0, 0

    for filepath in files:
        if not os.path.isfile(filepath):
            continue
        total += 1
        status, detail = check_file(filepath)
        if status == "pass":
            passed += 1
        elif status == "fail":
            failed += 1
            print(f"FAIL {os.path.basename(filepath)}: {detail[:120]}")
        else:
            skipped += 1

    print(f"\n{passed} passed, {failed} failed, {skipped} skipped (total {total})")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
