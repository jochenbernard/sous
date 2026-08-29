# 11. Validation

Validation reads a recipe and reports what reading a document cannot: problems
visible only once the whole recipe is in hand.

Validation is separate from reading. A document that is well formed may still
fail every rule here, and a recipe that fails them is still a recipe.

## 11.1 The rules

| Rule                                              | Reported                      |
| ------------------------------------------------- | ----------------------------- |
| A unit declares at most one yield                 | Once, at the first occurrence |
| No declared yield is zero                         | Once per zero yield           |
| No two group headings carry one name              | Once, at the first occurrence |
| Every reference matches a group                   | Once per target               |
| No group consumes an intermediate depending on it | Once per cycle                |

## 11.2 Declared yields

The yields a recipe declares are the `servings` value and every `yield` item,
counted together. `servings` declares its yield under the unit `servings`, and a
`yield` item under its own unit, trimmed.

A value carrying no usable number declares no yield, and is no concern of the
first two rules.

## 11.3 Group names and cycles

Names are compared normalized by
[10.1](10-references.md#101-the-normalized-form), so two headings differing
only in case collide.

A group consuming an intermediate that depends on it forms a cycle. Every group
in a cycle reaches itself, so one report covers the whole cycle rather than one
per member.

## 11.4 Reports

A report from validation carries no source range, because validation reads a
recipe rather than a document.

A failed scaling request is no concern of validation.
[Scaling](12-scaling.md) fails at the request instead.
