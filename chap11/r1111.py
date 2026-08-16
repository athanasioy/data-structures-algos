"""
Give a schematic figure, in the style of Figure 11.13, showing the heights
of subtrees during a deletion operation in an AVL tree that triggers a tri-
node restructuring for the case in which the two children of the node de-
noted as y start with equal heights. What is the net effect of the height of
the rebalanced subtree due to the deletion operation?
"""


"""
Assume subtree rooted at x with H(x) = h + 2.

Let y be right child of x and let T1 be the
left subtree of y and z the right node of y.

Let y have children of equal length, i.e.
H(T2) = h, H(z) = h.
=> H(y) = h + 1

Assume T1 has new height H(T1) = h - 1 after
a deletion operation.

Now the node x becomes unbalanced because
H(y) - H(T1) = h + 1 - (h - 1) = 2.

A restructure operation is initiated to restore
balance at x.

y becomes the new root left child x and right
child z.

Let y' denote the new subtree root.
new height of subtree rooted at y' is
H(y') = MAX(H(x), H(z)) + 1

[
the restructure operation swifted T2 to be the
right child of x.
]
H(x) = MAX(H(T1), H(T2)) + 1 = MAX(h-1, h) = h + 1
H(z) = h
=>
H(y') = MAX(h, h+1) + 1 = h + 2

Thus the delta is H(y) - H(y') = h + 2 - (h + 2)= 0

"""
