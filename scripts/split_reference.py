import os
import re
import sys

SOURCE_DIR = "raw"
TARGET_DIR = "reference"

MAPPING = {
    "1.": "01-variables-constants.md",
    "2.": "02-primitive-types.md",
    "3.": "03-aggregate-types.md",
    "4.": "04-functions-lambdas.md",
    "5.": "05-control-flow.md",
    "6.": "06-operators.md",
    "7.": "07-printing-interpolation.md",
    "8.": "08-memory-management.md",
    "9.": "09-oop.md",
    "10.": "10-generics.md",
    "11.": "11-concurrency.md",
    "12.": "12-advanced.md",
    "13.": "14-interop.md",
    "14.": "15-unit-testing-framework.md",
    "15.": "16-diagnostics.md",
}

WEIGHTS = {
    "01-variables-constants.md": 1,
    "02-primitive-types.md": 2,
    "03-aggregate-types.md": 3,
    "04-functions-lambdas.md": 4,
    "05-control-flow.md": 5,
    "06-operators.md": 6,
    "07-printing-interpolation.md": 7,
    "08-memory-management.md": 8,
    "09-oop.md": 9,
    "10-generics.md": 10,
    "11-concurrency.md": 11,
    "12-advanced.md": 12,
    "13-comptime.md": 13,
    "14-interop.md": 14,
    "15-unit-testing-framework.md": 15,
    "16-diagnostics.md": 16,
    "17-misra-rules.md": 17,
}

LANG_MAP = {
    "README.md": "en",
    "README_DE.md": "de",
    "README_ES.md": "es",
    "README_IT.md": "it",
    "README_PT_BR.md": "pt",
    "README_RU.md": "ru",
    "README_ZH_CN.md": "zh-cn",
    "README_ZH_TW.md": "zh-tw",
}

GROUP_TITLES = {
    "12-advanced.md": {
        "en": "12. Advanced & Metaprogramming",
        "de": "12. Fortgeschrittenes & Metaprogrammierung",
        "es": "12. Avanzado y Metaprogramacion",
        "it": "12. Avanzate e Metaprogrammazione",
        "pt": "12. Avancado e Metaprogramacao",
        "ru": "12. Продвинутые темы и метапрограммирование",
        "zh-cn": "12. 高级与元编程",
        "zh-tw": "12. 高級與元編程",
    }
}

MANUAL_FILES = {
    "13-comptime.md",
    "17-misra-rules.md",
}

DESCRIPTIVE_ANCHORS = {
    "move-semantics--copy-safety": ("08-memory-management", "resource-semantics-move-by-default"),
    "resource-semantics-move-by-default": ("08-memory-management", "resource-semantics-move-by-default"),
    "semantica-de-recursos-move-por-padrao": ("08-memory-management", "semantica-de-recursos-move-by-default"),
    "semantiche-di-movimento--copia-sicura": ("08-memory-management", "semantiche-delle-risorse-move-by-default"),
    "semantiche-delle-risorse": ("08-memory-management", "semantiche-delle-risorse-move-by-default"),
    "ressourcen-semantik-move-by-default": ("08-memory-management", "ressourcen-semantik-move-by-default"),
    "semantica-de-recursos-movimiento-por-defecto": ("08-memory-management", "semantica-de-recursos-movimiento-por-defecto"),
    "семантика-ресурсов-move-по-умолчанию": ("08-memory-management", "semantika-resursov-move-po-umolchaniiu"),
    "资源语义-默认移动": ("08-memory-management", "zi-yuan-yu-yi-mo-ren-yi-dong"),
    "資源語義-默認移動": ("08-memory-management", "zi-yuan-yu-yi-mo-ren-yi-dong"),
}


def build_reverse_mapping():
    """Build {target_filename: raw_section_number} from MAPPING."""
    rev = {}
    for raw_num, target in MAPPING.items():
        rev[target] = raw_num.rstrip(".")
    return rev


RAW_SECTION_NUM = build_reverse_mapping()


def rewrite_numbered_anchor(anchor):
    """Given a numbered anchor like '15-diagnostic-system', rewrite the numeric prefix
    using MAPPING and WEIGHTS. Returns None if the anchor is not numbered."""
    m = re.match(r"^(\d+)-(.*)", anchor)
    if not m:
        return None
    raw_num = m.group(1)
    suffix = m.group(2)
    target = MAPPING.get(raw_num + ".")
    if not target:
        return None
    weight = WEIGHTS.get(target)
    if weight is None:
        return None
    return f"{weight}-{suffix}"


def convert_alerts(content):
    def replace_alert(match):
        alert_type = match.group(1).lower()
        body = match.group(2)
        body_clean = re.sub(r"^>\s?", "", body, flags=re.MULTILINE)
        return f'{{% alert(type="{alert_type}") %}}\n{body_clean}{{% end %}}\n'

    pattern = r">\s*\[!(NOTE|TIP|WARNING|IMPORTANT|CAUTION)\]\s*\n((?:>.*\n?)+)"
    return re.sub(pattern, replace_alert, content)


def fix_links(content, lang):
    def replacer(match):
        text = match.group(1)
        anchor = match.group(2).lstrip("#")

        target_base = None
        new_anchor = None

        desc = DESCRIPTIVE_ANCHORS.get(anchor)
        if desc:
            target_base, new_anchor = desc
        else:
            new_anchor = rewrite_numbered_anchor(anchor)
            if new_anchor is None:
                return match.group(0)
            m = re.match(r"^(\d+)-", anchor)
            raw_num = m.group(1)
            target_base = MAPPING.get(raw_num + ".")

        if not target_base:
            return match.group(0)

        base_no_ext = target_base.replace(".md", "")
        if lang == "en":
            ext = ".md"
        else:
            ext = f".{lang}.md"
        anchor_part = f"#{new_anchor}" if new_anchor else ""
        return f"[{text}](@/tour/{base_no_ext}{ext}{anchor_part})"

    return re.sub(r"\[([^\]]+)\]\(#([^\)]+)\)", replacer, content)


def make_title(raw_num, raw_title, target_filename):
    """Replace the raw section number with the weight-based number."""
    weight = WEIGHTS.get(target_filename, 100)
    return f"{weight}. {raw_title}"


def process_file(filename, force=False):
    lang = LANG_MAP.get(filename)
    if not lang:
        return

    filepath = os.path.join(SOURCE_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        full_content = f.read()

    sections = re.split(r"\n###\s+(\d+\.)\s+(.*?)\n", full_content)

    file_contents = {}

    for i in range(1, len(sections), 3):
        raw_num = sections[i]
        raw_title = sections[i + 1]
        body = sections[i + 2]

        target_filename = MAPPING.get(raw_num)
        if not target_filename:
            continue

        if target_filename not in file_contents:
            file_contents[target_filename] = []

        renumbered_title = make_title(raw_num.rstrip("."), raw_title, target_filename)
        file_contents[target_filename].append((renumbered_title, body))

    for target_filename, parts in file_contents.items():
        if lang == "en":
            out_name = target_filename
        else:
            out_name = target_filename.replace(".md", f".{lang}.md")

        out_path = os.path.join(TARGET_DIR, out_name)

        if target_filename in MANUAL_FILES:
            print(f"  Skipping {out_name} -- manual file, never generated")
            continue

        if os.path.exists(out_path) and not force:
            print(f"  Skipping {out_name} -- already exists (use --force to regenerate)")
            continue

        main_title = parts[0][0]
        combined_body = ""

        if target_filename in GROUP_TITLES:
            main_title = GROUP_TITLES[target_filename].get(lang, parts[0][0])
            for title, body in parts:
                sub_title = title.split(". ", 1)[1]
                combined_body += f"\n### {sub_title}\n{body}"
        else:
            combined_body = parts[0][1]

        combined_body = convert_alerts(combined_body)
        combined_body = fix_links(combined_body, lang)

        weight = WEIGHTS.get(target_filename, 100)
        final_content = (
            f"+++\ntitle = \"{main_title}\"\n"
            f"weight = {weight}\n"
            f"+++\n\n"
            f"# {main_title}\n\n"
            f"{combined_body}"
        )

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(final_content)
        print(f"  Wrote {out_name}")


if __name__ == "__main__":
    force = "--force" in sys.argv

    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)

    for filename in sorted(os.listdir(SOURCE_DIR)):
        if filename.startswith("README"):
            print(f"Processing {filename}...")
            process_file(filename, force=force)
