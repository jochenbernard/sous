# 4. The metadata header

The header carries what holds for the whole recipe.
[The document](03-document.md) gives which lines are the header's; this
chapter reads them.

## 4.1 Entries

The header is a sequence of entries, one per line that is not blank, in the
order written. A blank line contributes no entry.

## 4.2 The key and the value

A line splits into a key and a value at the first colon followed by whitespace
or ending the line. Both are trimmed.

A colon followed by anything else does not split the line, so a value may hold
one: `source: https://example.com/gratin-dauphinois` has the key `source`.

## 4.3 The keys this specification names

| Key        | Read as  |
| ---------- | -------- |
| `title`    | Text     |
| `language` | Text     |
| `version`  | Text     |
| `source`   | Text     |
| `servings` | A number |
| `yield`    | A list   |
| `tags`     | A list   |

A key this specification does not name is read as text and must be kept. Its
value is reachable the way a named text key's is.

`servings` and every item of `yield` are read as amounts by
[Amounts](07-amounts.md), where a leading `=` is ordinary text rather than
the marker. `servings` is the leading number of its value, absent when the value
opens with none.

## 4.4 List values

A value is an inline list when it opens with `[` and its last character is an
unescaped `]`. Its items are what lies between the brackets, split on unescaped
commas and trimmed; an empty item is dropped.

Any other value of a list key is a single item, and an empty value is no items.

Within an inline list a backslash escapes `,`, `[`, `]`, and itself. It escapes
nothing else, and a backslash before any other character is kept.

## 4.5 Repeated keys

A repeated key must be reported as a warning, and must be kept.

| Kind of key | Result                                             |
| ----------- | -------------------------------------------------- |
| A list key  | The items of every entry, merged in document order |
| Any other   | The value of the last entry carrying that key      |

## 4.6 Recovery

| Line                                                     | Recovery                                           |
| -------------------------------------------------------- | -------------------------------------------------- |
| Opens with whitespace                                    | Kept verbatim under an empty key, with a warning   |
| Holds no colon that splits it                            | Kept verbatim under an empty key, with a warning   |
| Holds a value under an empty key                         | Kept, with a warning                               |
| Carries a defective quantity under `servings` or `yield` | Kept, with a warning from [Amounts](07-amounts.md) |

A line kept verbatim holds its leading whitespace, so nothing written in the
header is lost.
