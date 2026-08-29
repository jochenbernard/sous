# 1. Introduction

Sous is a plain text format for recipes. One document carries one recipe: a
metadata header, then the steps written as prose, with the ingredients,
cookware, timers, and intermediates marked inline.

## 1.1 A recipe

[crepes.sous](../examples/crepes.sous), whole:

```sous
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

The header between the `---` fences carries what holds for the whole recipe. The
body carries the steps, one to a paragraph. Within a step a sigil opens a span
around the words naming an ingredient, a piece of cookware, a duration, or
something produced elsewhere in the file. The prose between those spans is read
as written.

## 1.2 What this specification defines

This specification defines the characters a document is made of, the constructs
written in it, and what each one means. It then defines three operations on a
recipe once read: validation, scaling, and writing the recipe back out.

## 1.3 What this specification leaves open

Sous marks spans in a recipe and reads the rest as written. The following are
outside it, and a document is free in all of them.

| Left open           | Consequence                                                              |
| ------------------- | ------------------------------------------------------------------------ |
| The prose of a step | Wording, order, and detail are the writer's. Only the spans are read.    |
| Units               | A unit is text. Two spellings of one unit are two units.                 |
| Names               | An ingredient, a cookware, and a group name are text.                    |
| Temperatures        | Nothing marks one. `bake at 190C` is prose.                              |
| Header keys         | A key [The metadata header](04-metadata.md) does not name is still read. |

Nothing here converts between units, resolves an ingredient to a database, or
gives a recipe a nutritional value.
