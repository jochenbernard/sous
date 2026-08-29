# 8. Timers

A timer is written between `~` sigils, as in `~1 min~`. It takes no amount fence
and no flags, so every character between the sigils is its content.

## 8.1 Components

A timer is read as a sequence of components, left to right. A component opens at
a usable number and runs to the whitespace before the next digit, or to the end
of the content.

Each component is read as an amount by [Amounts](07-amounts.md), where a
leading `=` is ordinary text.

`1 h 30 min` is two components, `1 h` and `30 min`. `8-10 min` is one.

Content opening with no usable number is a single imprecise component, whatever
it holds.

## 8.2 The four forms

A timer's form follows from its components.

| Components     | Form        | Written        |
| -------------- | ----------- | -------------- |
| One, precise   | Precise     | `~1 min~`      |
| One, a range   | Range       | `~8-10 min~`   |
| One, imprecise | Qualitative | `~overnight~`  |
| None           | Qualitative |                |
| More than one  | Compound    | `~1 h 30 min~` |

More than one component is compound whatever the parts hold, so `~1 h 20-30
min~` is compound rather than a range.

## 8.3 The text

A timer keeps its content as written, trimmed. [Scaling](12-scaling.md) never
moves a timer.
