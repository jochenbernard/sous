# 3. The document

## 3.1 Characters

A document is a sequence of Unicode characters. This specification places no
requirement on the encoding a document is stored in, and none on the file
extension, which is conventionally `.sous`.

A byte order mark (U+FEFF) written as the first character is no part of the
document and must be dropped before anything else is read. Written anywhere
else it is an ordinary character.

## 3.2 Lines

A document is a sequence of lines. A line ends at any character Unicode breaks
a line on:

| Character | Name                |
| --------- | ------------------- |
| U+000A    | line feed           |
| U+000B    | line tabulation     |
| U+000C    | form feed           |
| U+000D    | carriage return     |
| U+0085    | next line           |
| U+2028    | line separator      |
| U+2029    | paragraph separator |

A carriage return followed immediately by a line feed ends one line, not two.

The text between two line breaks is a line even when it is empty, and the text
after the last line break is a line, empty when the document ends with a break.

A line is blank when it is empty or holds only whitespace. A line is a fence
when it is `---` and nothing else, ignoring whitespace at its end. Whitespace
at the start disqualifies a line, so an indented `---` is ordinary content.

## 3.3 The header and the body

A document is a metadata header followed by a body. The header opens on the
first line that is not blank, and only when that line is a fence, so a document
may begin with blank lines.

| First line that is not blank | Header                          | Body                        |
| ---------------------------- | ------------------------------- | --------------------------- |
| A fence, later closed        | The lines between the two fences | The lines after the closing fence |
| A fence, never closed        | The lines after it              | Empty                       |
| Anything else                | Empty                           | The whole document          |
| None, the document is blank  | Empty                           | The whole document          |

The header closes on the first fence after the one opening it. A header holding
no lines is well formed, and so is a document that is only a header.

A document whose header never closes is not well formed. Its recovery gives the
rest of the document to the header and leaves no body, and must be reported as
a warning.

[The metadata header](04-metadata.md) reads the header's lines, and [The
body](05-body.md) reads the body's.
