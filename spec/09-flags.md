# 9. Flags

A flag is written after an annotation's closing sigil, as in `@salt@:staple`.
Only an ingredient and a reference take flags.

## 9.1 Writing a flag

A flag is `:` followed by its name. Flags chain with nothing between them, as in
`@thyme@?:staple`.

`?` is a shorthand, equivalent to `:optional`, and takes no name.

A flag name runs while the characters are letters or `-`.

A `:` followed by anything but a letter or `-` is ordinary prose, so `@salt@: to
taste` carries no flag and the chain ends there.

## 9.2 The flags this specification names

| Written     | Meaning               |
| ----------- | --------------------- |
| `?`         | Optional              |
| `:optional` | Optional              |
| `:staple`   | Assumed to be on hand |
| `:non-food` | Not something eaten   |

## 9.3 Flags this specification does not name

A flag this specification does not name must be kept, in the order written, so
a document using a flag from a later version reads and writes back unchanged.

A name repeated within one chain is kept once.
