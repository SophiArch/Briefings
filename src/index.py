"""Regenerate README.md by indexing all HTML briefings in the repo."""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
README_PATH = REPO_ROOT / "README.md"
FRONT_PATH = REPO_ROOT / "front.md"
BOTTOM_PATH = REPO_ROOT / "bottom.md"
PAGES_BASE_URL = "https://sophiarch.github.io/Briefings"

EXCLUDED_DIR_NAMES = {".venv", ".git", "node_modules", "Scripts"}


def find_html_files() -> list[Path]:
    html_files = []
    for path in REPO_ROOT.rglob("*.html"):
        relative_parts = path.relative_to(REPO_ROOT).parts
        if any(part in EXCLUDED_DIR_NAMES or part.startswith(".") for part in relative_parts):
            continue
        html_files.append(path)
    return sorted(html_files, key=lambda p: p.relative_to(REPO_ROOT).as_posix())


def build_readme(html_files: list[Path]) -> str:
    sections: dict[str, list[Path]] = {}
    for path in html_files:
        folder = path.relative_to(REPO_ROOT).parts[0]
        sections.setdefault(folder, []).append(path)

    lines = []
    for folder in sorted(sections):
        lines.append(f"## {folder}")
        for path in sections[folder]:
            relative_path = path.relative_to(REPO_ROOT).as_posix()
            lines.append(f"- [{path.name}]({PAGES_BASE_URL}/{relative_path})")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    html_files = find_html_files()
    front = FRONT_PATH.read_text().rstrip("\n")
    index = build_readme(html_files)
    bottom = BOTTOM_PATH.read_text().rstrip("\n")
    README_PATH.write_text(f"{front}\n\n{index}\n\n{bottom}\n")


if __name__ == "__main__":
    main()
