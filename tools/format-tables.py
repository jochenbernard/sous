"""Reports Markdown tables whose columns are not padded to one width.

Pass --fix to rewrite them in place.
"""

import pathlib
import re
import sys


def cells(row):
    """The cells of a table row, trimmed."""
    return [cell.strip() for cell in row.strip().strip("|").split("|")]


def is_separator(row):
    """Whether the row is the dashed line under a table's header."""
    return all(re.fullmatch(r"-+", cell) for cell in cells(row))


def formatted(rows):
    """The rows with every column padded to the width of its widest cell."""
    parsed = [cells(row) for row in rows]
    columns = max(len(row) for row in parsed)
    widths = [
        max(len(row[i]) for row in parsed if not is_separator("|".join(row)) and i < len(row))
        for i in range(columns)
    ]

    written = []
    for row, source in zip(parsed, rows):
        if is_separator(source):
            written.append("| " + " | ".join("-" * width for width in widths) + " |")
        else:
            padded = [row[i].ljust(widths[i]) if i < len(row) else " " * widths[i] for i in range(columns)]
            written.append("| " + " | ".join(padded) + " |")

    return written


def tables(lines):
    """Each run of table lines lying outside a fenced code block, with where it starts."""
    fenced, run, start = False, [], None

    for index, line in enumerate(lines):
        if line.startswith("```"):
            fenced = not fenced
        if not fenced and line.startswith("|"):
            if start is None:
                start = index
            run.append(line)
            continue
        if run:
            yield start, run
        run, start = [], None

    if run:
        yield start, run


fix = "--fix" in sys.argv
reported = 0

for path in sorted(pathlib.Path(".").rglob("*.md")):
    if ".git" in path.parts:
        continue

    lines = path.read_text().split("\n")
    changed = False

    for start, rows in tables(lines):
        written = formatted(rows)
        if written == rows:
            continue
        if fix:
            lines[start:start + len(rows)] = written
            changed = True
        else:
            print(f"{path}:{start + 1}: table columns are not aligned")
            reported += 1

    if changed:
        path.write_text("\n".join(lines))
        print(f"formatted {path}")

sys.exit(0)
