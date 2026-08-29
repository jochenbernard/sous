"""Reports a section citation left as bare text, and a list item whose
continuation lines lost their indent.

A bare citation reads the same as a linked one in source, so nothing else
catches it.
"""

import pathlib
import re

CITATION = re.compile(r"(?<![\w.#/-])(\d+\.\d+)(?!\d)")


def sections():
    """Every section number the specification defines."""
    return {
        m.group(1)
        for f in pathlib.Path("spec").glob("*.md")
        for m in re.finditer(r"^## (\d+\.\d+)", f.read_text(), re.M)
    }


defined = sections()

for f in sorted(pathlib.Path(".").rglob("*.md")):
    if ".git" in f.parts:
        continue

    fenced, item = False, False

    for number, line in enumerate(f.read_text().split("\n"), start=1):
        if line.startswith("```"):
            fenced = not fenced
            continue
        if fenced:
            continue

        if not line.startswith("## "):
            bare = re.sub(r"\[[^\]]*\]\([^)]*\)", "", re.sub(r"`[^`]*`", "", line))
            for match in CITATION.finditer(bare):
                if match.group(1) in defined:
                    print(f"{f}:{number}: {match.group(1)} is cited as bare text")

        if line.lstrip().startswith("- "):
            item = True
        elif item:
            if not line.strip():
                item = False
            elif not line.startswith("  "):
                print(f"{f}:{number}: a list item's continuation line is not indented")
                item = False
