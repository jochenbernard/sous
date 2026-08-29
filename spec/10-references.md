# 10. Groups and references

A reference consumes what another group produces. This chapter gives how the two
are matched.

## 10.1 The normalized form

A name is normalized by lowercasing it, folding its accents away, and trimming
it. Normalizing an already normalized name returns it unchanged.

`Pastry`, `pastry`, and ` PASTRY ` normalize alike.

## 10.2 Matching a reference

A reference matches the first group whose name normalizes to the form its target
normalizes to. A group with no name matches nothing.

Reading a document does not match a reference. A reference matching no group is
read and kept, and [Validation](11-validation.md) reports it.

## 10.3 Dependencies

The dependencies of a group are the groups its references match, each appearing
once, in the order its first matching reference occurs. A reference matching no
group contributes none.

## 10.4 Names are not units

Only a group name is normalized. A unit is matched as written, and
[12.4](12-scaling.md#124-scaling-to-an-amount) gives why.
