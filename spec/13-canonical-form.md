# 13. Canonical form

Writing a recipe back out produces a document. Content is preserved and
incidental layout is normalized, so reading the result produces the same recipe.

## 13.1 Layout

A header is written when it holds at least one entry, between `---` fences, one
line per entry in document order.

Groups follow, separated by a blank line, and the header is separated from them
by a blank line. Within a group the heading comes first, then the steps,
separated by blank lines. A group producing no text is not written.

A run of several blank lines in a document therefore comes back as one.

## 13.2 Header entries

| Entry                                               | Written as                                      |
| --------------------------------------------------- | ----------------------------------------------- |
| A text value                                        | `key: value`, or `key:` when the value is empty |
| A list value                                        | `key: [a, b]`, or `key:` when it holds no items |
| A line kept under [4.6](04-metadata.md#46-recovery) | Verbatim, as it was read                        |

A list item carrying `,`, `[`, `]`, or a backslash is written with those
characters escaped, so the list reads back item for item.

## 13.3 Annotations

An annotation is written with its sigils, its amount fence when it has one, and
then its flags. An amount keeps the text it was read as, with its `=` marker
restored when it is fixed.

Flags are written as words first, in the order this specification names them,
then the flags it does not name in the order they were read, then the
shorthands. `@thyme@?:staple` therefore comes back as `@thyme@:staple?`, which
reads the same.

## 13.4 Escaping

Every character that would otherwise read back as something other than itself is
escaped:

- a sigil in prose that would open a span;
- a backslash that would escape the character after it;
- a `{` opening the name of a span that takes an amount, which would
  otherwise open a fence;
- a `}` inside a fence, which would otherwise close it early;
- the start of a line that would open a heading;
- the start of prose following a flag chain, which the chain would
  otherwise swallow.

## 13.5 A body that would open a header

A recipe with no header whose body would open with a fence is written with an
empty header in front, because the fence would otherwise be read as one.

A body opening with a byte order mark is written after a line break, because
[3.1](03-document.md#31-characters) would otherwise drop the mark.
