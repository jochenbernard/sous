# 2. Conformance

## 2.1 Normative terms

`must` gives a requirement. `must not` gives a prohibition. `may` gives a
permission, and both choices conform.

The terms are written in lowercase. Every other word in this specification is
prose and carries no requirement. This specification does not use `should`.

## 2.2 A conforming document

Every sequence of characters is a Sous document. No document is rejected.

A document is well formed when every construct written in it closes as the
chapter defining that construct requires. A document that is not well formed is
still a document, and still has a meaning, given by 2.4.

## 2.3 A conforming implementation

An implementation must read every document, and must produce for it the recipe
this specification describes together with one report for every construct
recovered under 2.4.

An implementation must not reject a document. It may offer operations this
specification does not define.

## 2.4 Recovery

Reading must succeed and must produce a recipe.

Each chapter gives the recovery for the constructs it defines. Two rules hold
across all of them:

- A construct that is not well formed is read as the literal characters it is
written with, and the text around it is read as written.
- Every recovery must be reported.

## 2.5 Reports

A report carries a severity.

| Severity | Reach                                                                         |
| -------- | ----------------------------------------------------------------------------- |
| warning  | One construct, which is preserved. The rest of the document reads as written. |
| error    | The whole recipe. What was read is not what the document describes.           |

A report produced while reading carries the range of source it covers. A report
produced by [Validation](11-validation.md) carries none, because validation
reads a recipe rather than a document.
