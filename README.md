# Sous

The specification for Sous, a plain text format for recipes.

Sous writes a recipe the way a cook reads one: a metadata header, then steps as
prose, with the ingredients, cookware, timers, and intermediates marked inline.

```
---
title: Crepes
servings: 4
yield: [12 crepes]
prep-time: 10 min
cook-time: 25 min
tags: [dessert, classic, french]
allergens: [gluten, dairy, eggs]
---

Whisk @{200 g} flour@ into a batter with @{4} eggs@, @{500 ml} milk@,
@{50 g} melted butter@, and @{1/2 tsp} salt@:staple, then rest it ~1 h~.

Wipe a #crepe pan# with @{10 g} butter@ over medium heat, ladle in a thin layer,
and cook each crepe for ~1 min~ a side until lacy and gold.
```

## Status

Sous is pre-1.0, and the format may change between minor versions.

The specification is being written chapter by chapter. Every chapter file
exists; a chapter not yet written holds its scope and nothing else.

## The specification

[`spec/README.md`](spec/README.md) lists the chapters and what each covers.
[`examples/`](examples/) holds the ten recipes the chapters quote.

## Layout

| Path                       | Contents                                    |
| -------------------------- | ------------------------------------------- |
| [`spec/`](spec/)           | The specification, one chapter per file     |
| [`examples/`](examples/)   | The recipes the chapters quote              |
| [`docs/`](docs/)           | Guidance for writing the specification      |

## Implementations

This section is no part of the specification.

| Implementation                                       | Language |
| ---------------------------------------------------- | -------- |
| [SousKit](https://github.com/jochenbernard/souskit)  | Swift    |

## License

The specification and the example recipes are licensed under
[Creative Commons Attribution 4.0 International](LICENSE).

Copyright (c) 2026 Jochen Bernard.
