"""
Give a justification of Proposition 8.4

Proposition 8.4: The height of a nonempty tree T is equal to the maximum of
the depths of its leaf positions.

Answer:
The height of a non empty tree T of node p is zero if
it a leaf node, otherwise is the maximum height of p's
children plus one. This recursive definition has a
base case when we reach a leaf node, at which point
it reaches its highest value.

Thus the height of the root is defined by the node
that has maximum depth, i.e. is the deepest in the
tree.
"""
