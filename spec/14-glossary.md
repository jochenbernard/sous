# 14. Glossary

| Term            | Meaning                                                                | Defined in                                                                     |
| --------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Amount          | A quantity, a range, or text with no usable number, written in a fence | [7](07-amounts.md)                                                             |
| Annotation      | A span of a step marked by a sigil                                     | [6](06-annotations.md)                                                         |
| Blank line      | A line that is empty or holds only whitespace                          | [3.2](03-document.md#32-lines)                                                 |
| Body            | The lines of a document after the header                               | [3.3](03-document.md#33-the-header-and-the-body)                               |
| Component       | One of the amounts a timer is written as                               | [8.1](08-timers.md#81-components)                                              |
| Compound        | A timer of more than one component                                     | [8.2](08-timers.md#82-the-four-forms)                                          |
| Cookware        | An annotation marked by `#`                                            | [6.1](06-annotations.md#61-the-four-sigils)                                    |
| Cycle           | A group consuming an intermediate that depends on it                   | [11.3](11-validation.md#113-group-names-and-cycles)                            |
| Declared yield  | A yield the header gives, from `servings` or a `yield` item            | [11.2](11-validation.md#112-declared-yields)                                   |
| Dependency      | A group another group consumes through a reference                     | [10.3](10-references.md#103-dependencies)                                      |
| Fence           | The braces an amount is written in, or a `---` header line             | [7.1](07-amounts.md#71-the-fence), [3.2](03-document.md#32-lines)              |
| Fixed           | An amount written with `=`, which scaling never moves                  | [7.2](07-amounts.md#72-the-fixed-marker)                                       |
| Flag            | A word written after an annotation's closing sigil                     | [9](09-flags.md)                                                               |
| Group           | A named run of steps, opened by a `##` heading                         | [5.1](05-body.md#51-groups)                                                    |
| Header          | The lines of a document between its `---` fences                       | [3.3](03-document.md#33-the-header-and-the-body)                               |
| Imprecise       | An amount opening with no usable number                                | [7.3](07-amounts.md#73-the-three-forms)                                        |
| Ingredient      | An annotation marked by `@`                                            | [6.1](06-annotations.md#61-the-four-sigils)                                    |
| Normalized form | A name lowercased, accent-folded, and trimmed                          | [10.1](10-references.md#101-the-normalized-form)                               |
| Precise         | An amount of one quantity, or a timer of one such component            | [7.3](07-amounts.md#73-the-three-forms), [8.2](08-timers.md#82-the-four-forms) |
| Prose           | The text of a step lying outside its annotations                       | [5.4](05-body.md#54-segments)                                                  |
| Qualitative     | A timer of no component, or of one imprecise component                 | [8.2](08-timers.md#82-the-four-forms)                                          |
| Quantity        | A number read from an amount                                           | [7.4](07-amounts.md#74-numbers)                                                |
| Range           | An amount of a low and a high quantity                                 | [7.3](07-amounts.md#73-the-three-forms)                                        |
| Recovery        | What a construct that is not well formed is read as                    | [2.4](02-conformance.md#24-recovery)                                           |
| Reference       | An annotation marked by `>`                                            | [6.1](06-annotations.md#61-the-four-sigils)                                    |
| Report          | A problem found while reading or validating                            | [2.5](02-conformance.md#25-reports)                                            |
| Segment         | One piece of a step: a run of prose, or an annotation                  | [5.4](05-body.md#54-segments)                                                  |
| Sigil           | A character opening and closing an annotation                          | [6.1](06-annotations.md#61-the-four-sigils)                                    |
| Span            | The characters an annotation's sigils enclose                          | [6.3](06-annotations.md#63-closing-a-span)                                     |
| Staple          | A flag marking an ingredient assumed to be on hand                     | [9.2](09-flags.md#92-the-flags-this-specification-names)                       |
| Step            | One paragraph of a group                                               | [5.3](05-body.md#53-steps)                                                     |
| Timer           | An annotation marked by `~`                                            | [6.1](06-annotations.md#61-the-four-sigils)                                    |
| Unit            | The text following a quantity in an amount                             | [7.6](07-amounts.md#76-the-unit)                                               |
| Well formed     | Every construct in a document closes as its chapter requires           | [2.2](02-conformance.md#22-a-conforming-document)                              |
