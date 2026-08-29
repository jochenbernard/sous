"""Reports every relative link resolving to no file, no heading, or split across lines.

A renamed heading breaks a citation silently, which is what this catches.
"""

import pathlib
import re

LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def slug(heading):
    """The anchor a heading is reachable by."""
    return re.sub(r"[^a-z0-9 -]", "", heading.lower()).replace(" ", "-")


def prose(text):
    """The text outside fenced code blocks and inline code spans.

    Fences are tracked by line, because a fenced block may itself hold a line
    carrying three backticks.
    """
    kept, fenced = [], False

    for line in text.split("\n"):
        if line.startswith("```"):
            fenced = not fenced
            continue
        if not fenced:
            kept.append(re.sub(r"`[^`]*`", "", line))

    return "\n".join(kept)


root = pathlib.Path(".").resolve()
docs = [f for f in pathlib.Path(".").rglob("*.md") if ".git" not in f.parts]
anchors = {
    str(f): {slug(m.group(1)) for m in re.finditer(r"^#+ (.*)", prose(f.read_text()), re.M)}
    for f in docs
}

for f in sorted(docs):
    raw = f.read_text()

    for match in LINK.finditer(prose(raw)):
        href = match.group(1)
        if href.startswith(("http://", "https://")):
            continue

        path, _, fragment = href.partition("#")
        target = (f.parent / path).resolve() if path else f.resolve()

        if not target.exists():
            print(f"{f}: {href} -> no such file")
        elif fragment and fragment not in anchors[str(target.relative_to(root))]:
            print(f"{f}: {href} -> no such anchor")

    for _ in re.finditer(r"\[[^\]]*\]\([^)]*\n[^)]*\)", raw):
        print(f"{f}: a link is broken across two lines")
