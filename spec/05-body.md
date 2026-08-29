# 5. The body

The body is the recipe itself: groups of steps.
[The document](03-document.md) gives which lines are the body's.

## 5.1 Groups

A `##` heading opens a group and names it. Steps written before any heading form
a group with no name.

A group with a name but no step is a group. A run of lines holding neither a
heading nor a step forms none, so a body of only blank lines has no groups.

## 5.2 Headings

A line opens a heading when it begins with `##`, the character after the `##` is
whitespace, and at least one character after that is not. `##` alone is a step,
not a heading.

A heading is recognized only on a line beginning a paragraph. `## text` on the
second line of a step continues that step.

The name is what follows the `##`, with escapes resolved by
[6.4](06-annotations.md#64-escapes) and then trimmed.

## 5.3 Steps

A step is one paragraph. Paragraphs are separated by blank lines, and a run of
several blank lines separates no more than a single one.

The lines of a paragraph are joined with a line feed, and the result is the
step's text. [Annotations](06-annotations.md) reads it.

## 5.4 Segments

A step is a sequence of segments, in the order written: runs of prose, and
annotations. A run of prose carries its escapes resolved. Two annotations
written with nothing between them produce no empty run between their segments.
