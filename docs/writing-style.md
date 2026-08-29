# Writing style

This guide governs every Markdown file in this repository: the chapters under
`spec/`, the guidance under `docs/`, and every README. A good sentence gives
one rule, in one voice, at a length a reader absorbs in one pass. The failures
it exists to prevent are the sentence that argues for the rule, the sentence
that describes a program instead of the format, and the sentence that hedges;
each costs the reader more attention than it returns.

## Rule 1: the specification stands alone

Sous is defined here and nowhere else. A chapter names no parser, no library,
and no program. It gives what a document means, never what an implementation
does with it, and never what one already does.

Rejected:

```
SousKit keeps an unrecognized flag rather than dropping it.
```

The rule belongs to the format, and reads the same for every implementation:

```
A flag this specification does not name is part of the annotation carrying it.
```

The direction is fixed. An implementation may cite a chapter; a chapter cites
no implementation. A question the text leaves open is answered by deciding it
here, never by reading what some program happens to do.

The one exception is the Implementations section of the repository README,
which is marked there as no part of the specification.

## Rule 2: the normative vocabulary is fixed

Three words carry every requirement, and `spec/02-conformance.md` defines
them.

| Word     | Meaning                                                       |
| -------- | ------------------------------------------------------------- |
| must     | A requirement. Breaking it conforms to nothing.                |
| must not | A prohibition, read the same way.                             |
| may      | A permission. Both choices conform.                           |

Write them in lowercase. Uppercase adds emphasis the sentence already carries.

`should` is not used. A reader cannot separate a recommendation from a
requirement, and a rule needing one has not been decided.

## Rule 3: no anthropomorphism

A format does not state, ask, want, or know. Give what it does: a header
carries fields, an annotation opens a span, a marker holds an amount constant.

| Banned          | Write instead                |
| --------------- | ---------------------------- |
| states          | is, holds, contains, gives   |
| asks, asks for  | requires, takes              |
| wants, expects  | requires                     |
| knows, knows of | names, defines               |
| owes            | returns, provides            |
| which is what   | end the sentence             |
| nobody wrote    | name the actual condition    |
| of its own      | delete it                    |

`so the` and `rather than` are restricted: admissible when they carry
information, never as connective filler between clauses already clear without
them. To test one, delete the phrase along with the clause it introduces.
Losing a fact means keep it; losing only rhythm means it was filler.

## Rule 4: a paragraph must earn its place

Every paragraph after the one giving the rule faces one question: does it
change what a writer writes, or what an implementation does? If not, cut it.

- A rule gets its sentence plus at most one short paragraph, admissible only
  where the rule's boundary would otherwise surprise.
- The reasoning that produced a rule belongs in the commit message; failing
  that, it belongs nowhere. A reader comes to apply the rule, not to review the
  argument behind it.
- A table replaces a list of parallel one-line rules. Prose between the rows
  repeats them.

## Rule 5: examples are quoted, not invented

A fragment short enough to read inline, such as `@parsley@` or `{1-2 tbsp}`, is
written inline.

A whole recipe is quoted from a file under `examples/`, byte for byte, so the
chapters and the example files never drift. A chapter needing a case those
files do not cover adds it to one of them, and the recipe stays cookable.

## Mechanics

- ASCII only, in prose and code blocks alike. Where a chapter covers a
  character outside it, name the character, as in "U+00EA, latin small letter e
  with circumflex", and do not write it.
- No em-dash constructions: neither the character itself nor a double hyphen
  standing in for one.
- Lines fit in 80 characters. Tables, fenced code blocks, and a URL that
  cannot be broken are exempt.
- Reference another chapter with a relative link to its file, as in
  [Amounts](../spec/07-amounts.md).
- Tag a fenced block holding Sous source `sous`, and one holding a shell
  command `bash`. Lowercase, matching the file extension. A block holding
  neither, such as the rejected and accepted sentences under Rule 1, is
  tagged with nothing.
- Exempt from all of the above: `LICENSE`, which holds the Creative Commons
  legal code verbatim, and `.gitignore`, which is generated below its custom
  section.

## Checking

Run these from the repository root. Each is expected to print nothing.

```bash
# Non-ASCII anywhere, which also catches a literal em-dash
LC_ALL=C grep -rn '[^ -~]' spec docs examples README.md CLAUDE.md

# Double hyphen standing in for an em-dash
grep -rnE '[^-]-{2}[^-]' spec docs examples README.md CLAUDE.md

# Lines over 80 characters
find spec docs README.md CLAUDE.md -name '*.md' | xargs awk '
    FNR == 1 { fenced = 0 }
    /^```/ { fenced = !fenced; next }
    fenced || /^\|/ { next }
    length > 80 { print FILENAME ":" FNR ": " length }'

# Banned vocabulary, conjugations included. "State" as a noun is fine, as in
# "a document holds no state".
find spec docs README.md CLAUDE.md -name '*.md' | xargs awk '
    FNR == 1 { fenced = 0 }
    /^```/ { fenced = !fenced; next }
    fenced || /^\|/ { next }
    tolower(" " $0 " ") ~ /[^a-z](states|stating|stated|asks|asking|wants|expects|knows|owes|of its own|which is what|nobody wrote)[^a-z]/ {
        print FILENAME ":" FNR ": " $0
    }'

# "should", which Rule 2 replaces with must or may. This guide names the word
# to ban it, so it is not searched.
grep -rniE '\bshould\b' spec README.md CLAUDE.md
```

Each command skips tables and fenced code blocks where a rule exempts them, so
Rule 3's own table and the commands above do not report themselves.
