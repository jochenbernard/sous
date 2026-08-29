# 12. Scaling

Scaling multiplies a recipe. A request that cannot be met fails rather than
producing an approximation.

## 12.1 Scaling by a factor

A factor must be finite and must not be negative. Zero is a usable factor;
negative zero is not.

## 12.2 What moves

| Moves                    | Holds still                       |
| ------------------------ | --------------------------------- |
| A precise amount         | A fixed amount, written `{=10 g}` |
| A range, both quantities | An imprecise amount               |
| The `servings` value     | Every timer                       |
| Every `yield` item       | Every other header key            |

A header key other than `servings` and `yield` is text and is carried over as
written, whatever it holds.

## 12.3 Scaling to a number of servings

The factor is the target divided by the declared `servings`.

## 12.4 Scaling to an amount

The target must hold a single quantity. The factor is the target divided by the
declared yield carrying the same unit.

A unit is matched as written, trimmed, and is not normalized the way a group
name is. Case separates two units: `T` is a tablespoon where `t` is a teaspoon,
and `mg` is a milligram where `Mg` is a megagram. Nothing converts between
spellings.

## 12.5 The yield after scaling

Multiplying by a factor can land just off the target through rounding, so the
matching declared yield is rewritten to the target exactly rather than left as
the multiplication produced it.

## 12.6 The text after scaling

A scaled amount is written back from its quantities and its unit, and read again
to keep its text and its quantities in agreement.

Where reading the result back would not reproduce the quantities, they are
written with an explicit decimal point, which reads back unambiguously. That is
what keeps a scaled `1` from reading as the whole part of a mixed fraction.

## 12.7 Failures

| Failure             | Cause                                                                      |
| ------------------- | -------------------------------------------------------------------------- |
| Unusable factor     | The factor is negative or is not finite                                    |
| Unwritable quantity | A scaled quantity is no longer finite                                      |
| No matching yield   | The target holds no single quantity, or no declared yield carries its unit |
| Zero yield          | The matching yield is zero, so no factor reaches the target                |
| Conflicting yields  | Several declared yields carry the unit and give different quantities       |
