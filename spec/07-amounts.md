# 7. Amounts

An amount is written in braces at the head of an ingredient or reference span,
as in `@{200 g} flour@`, and is read from the `servings` and `yield` header
values as well.

## 7.1 The fence

A fence opens on `{` as the first character of a span's content and closes on
the first `}` that is not escaped. Every sigil is inert between the braces.

The content is trimmed. A fence holding nothing is an imprecise amount whose
text is empty.

## 7.2 The fixed marker

A leading `=` fixes the amount, holding it constant under
[Scaling](12-scaling.md). The marker and the whitespace after it are no part
of the text.

The marker is read in a fence only. A leading `=` in a header value is ordinary
text.

## 7.3 The three forms

| Form      | Written      | Holds                     |
| --------- | ------------ | ------------------------- |
| Precise   | `{200 g}`    | One quantity              |
| Range     | `{1-2 tbsp}` | A low and a high quantity |
| Imprecise | `{a pinch}`  | No usable number          |

Content whose first characters are not a usable number is imprecise, whatever
follows. An imprecise amount never moves under scaling.

## 7.4 Numbers

A number is written as a run of ASCII digits. Digits of other scripts are not
numbers here.

| Written | Read as                                        |
| ------- | ---------------------------------------------- |
| `200`   | A whole number                                 |
| `0.5`   | A decimal, whose point must lie between digits |
| `1/2`   | A fraction                                     |
| `1 1/2` | A whole number and a fraction, added           |

A single character whose Unicode numeric value is not whole, such as U+00BD,
vulgar fraction one half, is a fraction, and follows a whole number the way
`1/2` does. A character whose numeric value is whole, such as a superscript
digit, is not a number.

Only a whole number takes a mixed fraction, so `1.5 1/2` is one number followed
by separate text.

## 7.5 Ranges

A range is two numbers separated by `-`. Whitespace around the separator belongs
to neither number, so `1-2`, `1 - 2`, and `1- 2` read alike.

## 7.6 The unit

The unit is what follows the number, with the whitespace separating the two
removed. An amount whose number is followed by nothing has no unit.

A unit is text. Two spellings of one unit are two units, and nothing here
converts between them.

## 7.7 Defects

Text opening as a number and failing to finish one is read as imprecise and must
be reported as a warning.

| Written | Defect                                 |
| ------- | -------------------------------------- |
| `1,5 l` | A comma used as a decimal point        |
| `1. l`  | A decimal point with no digit after it |
| `1/ l`  | A fraction with no denominator         |
| `1/0 l` | A fraction whose denominator is zero   |
| `.5 l`  | A number opening with no digit         |
| `-5 l`  | A number opening with no digit         |

Text carrying no number at all, such as `a pinch`, is imprecise and is no
defect.

## 7.8 The text

An amount keeps the text it was written as, trimmed and without its braces or
marker. [Canonical form](13-canonical-form.md) writes that text back, so an
amount is not reconstructed from its number and unit.
