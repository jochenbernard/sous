# The Sous specification

Sous is a plain text format for recipes. This specification defines what a Sous
document is and what it means.

Read the chapters in order. Each builds on the ones before it, and
[Glossary](14-glossary.md) collects the terms all of them use.

No chapter is written yet. Each file below holds its scope until it is.

## Chapters

| Chapter                                          | Covers                                                                                    |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| [1. Introduction](01-introduction.md)            | What Sous is, what this specification defines, and what it leaves to the writer.           |
| [2. Conformance](02-conformance.md)              | The normative terms, a conforming document, and what becomes of text no rule describes.    |
| [3. The document](03-document.md)                | Encoding, lines, and the split into a header and a body.                                   |
| [4. The metadata header](04-metadata.md)         | The fields the header names, their types, and the keys it leaves open.                     |
| [5. The body](05-body.md)                        | Group headings, steps, and the prose segments between annotations.                         |
| [6. Annotations](06-annotations.md)              | The four sigils, the spans they open, and the backslash escape.                            |
| [7. Amounts](07-amounts.md)                      | Quantities, ranges, mixed fractions, imprecise text, and the fixed marker.                 |
| [8. Timers](08-timers.md)                        | A timer's components and the four forms they produce.                                      |
| [9. Flags](09-flags.md)                          | Optional, staple, and non-food, and flags this specification does not name.                |
| [10. Groups and references](10-references.md)    | Name normalization, matching a reference to a group, and the dependencies that follow.     |
| [11. Validation](11-validation.md)               | The rules a valid recipe satisfies beyond being well formed.                               |
| [12. Scaling](12-scaling.md)                     | What a scale factor moves, and what holds still.                                           |
| [13. Canonical form](13-canonical-form.md)       | Writing a recipe back out.                                                                 |
| [14. Glossary](14-glossary.md)                   | The terms this specification defines.                                                      |
