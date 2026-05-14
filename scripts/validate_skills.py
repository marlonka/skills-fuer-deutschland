from pathlib import Path
import re
import sys


REQUIRED_SECTIONS = [
    "## Arbeitsstandard",
    "## Quellen und Prüfstandard",
    "## Was Top-Arbeit von Standardarbeit unterscheidet",
    "## Fachspezifische Top-Practices",
    "## Arbeitsablauf",
    "## Ausgabe",
    "## Qualitätskontrolle",
]

NAME_RE = re.compile(r"^[a-z0-9-]{1,64}$")


def fail(errors, path, message):
    errors.append(f"{path}: {message}")


def parse_frontmatter(path, text, errors):
    if not text.startswith("---\n"):
        fail(errors, path, "missing YAML frontmatter")
        return {}

    try:
        _, frontmatter, _ = text.split("---\n", 2)
    except ValueError:
        fail(errors, path, "frontmatter is not closed")
        return {}

    data = {}
    for line in frontmatter.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(errors, path, f"invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def validate_skill(path, errors):
    text = path.read_text(encoding="utf-8")
    data = parse_frontmatter(path, text, errors)

    name = data.get("name")
    description = data.get("description")
    allowed_keys = {"name", "description"}

    extra_keys = set(data) - allowed_keys
    if extra_keys:
        fail(errors, path, f"frontmatter has unsupported keys: {', '.join(sorted(extra_keys))}")

    if not name:
        fail(errors, path, "missing frontmatter name")
    elif not NAME_RE.fullmatch(name):
        fail(errors, path, "name must be lowercase hyphen-case and max 64 characters")
    elif path.parent.name != name:
        fail(errors, path, f"folder name must match frontmatter name '{name}'")

    if not description:
        fail(errors, path, "missing frontmatter description")
    elif len(description) < 80:
        fail(errors, path, "description is too short to trigger reliably")

    files = [item for item in path.parent.iterdir() if item.is_file()]
    if files != [path]:
        fail(errors, path.parent, "skill folder must contain exactly one SKILL.md file")

    for section in REQUIRED_SECTIONS:
        if text.count(section) != 1:
            fail(errors, path, f"missing or duplicate section: {section}")


def main():
    root = Path("recht")
    if not root.exists():
        print("No recht/ directory found", file=sys.stderr)
        return 1

    skills = sorted(root.glob("**/SKILL.md"))
    errors = []

    if not skills:
        errors.append("No SKILL.md files found under recht/")

    for skill in skills:
        validate_skill(skill, errors)

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(f"Validated {len(skills)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
