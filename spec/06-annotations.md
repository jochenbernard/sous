# 6. Annotations

An annotation marks a span of a step. Four sigils open one, and each closes on
the same character.

## 6.1 The four sigils

| Sigil | Marks         | Takes an amount | Takes flags |
| ----- | ------------- | --------------- | ----------- |
| `@`   | An ingredient | Yes             | Yes         |
| `#`   | Cookware      | No              | No          |
| `~`   | A timer       | No              | No          |
| `>`   | A reference   | Yes             | Yes         |

An ingredient and a reference are read by [Amounts](07-amounts.md) and
[Flags](09-flags.md); a timer by [Timers](08-timers.md); a reference
target by [Groups and references](10-references.md).

## 6.2 Opening a span

A sigil opens a span only when a character follows it and that character is not
whitespace. A sigil ending a line, or followed by a space, is ordinary prose, so
`Bake @ 180C` opens no span.

## 6.3 Closing a span

A span closes on the first matching sigil that is not escaped, searched from the
start of the name. The search stops at a line break, so a span closes on the
line it opens on or not at all.

The name is what lies between the sigils, past any amount fence, with escapes
resolved and then trimmed.

## 6.4 Escapes

A backslash escapes the character after it when that character is one of:

```
@ # ~ > ? : { } \
```

The pair is read as the second character alone, so `Wait \~40 min here.` writes
a tilde opening no timer.

A backslash before any other character is ordinary text and is kept, and so is a
backslash ending a line. Within an amount fence the same set applies; within an
inline header list the set of [4.4](04-metadata.md#44-list-values) applies
instead.

## 6.5 Recovery

| Written                                            | Recovery                                        |
| -------------------------------------------------- | ----------------------------------------------- |
| A span that never closes                           | The opening sigil alone becomes prose           |
| A fence that never closes, in a span that does     | The span becomes prose, up to its closing sigil |
| A fence that never closes, in a span that does not | The opening sigil alone becomes prose           |
| A span whose name is empty                         | The whole span becomes prose                    |

Each must be reported as a warning. A span whose name is empty but which carries
an amount must be reported a second time, because the amount is discarded with
it.
