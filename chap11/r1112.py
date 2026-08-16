"""
Repeat the previous problem, considering the case in which y’s children
start with different heights.

"""


"""
ANSWER:
Assume subtree rooted at x with H(x) = h + 2.

Let y be right child of x and let T1 be the
left subtree of y and z the right node of y.

Let y have children of not equal length, i.e.
[T2 is the left subtree of y]
H(T2) = h-1
H(z) = h.
=> H(y) = MAX(H(T2), H(z)) + 1 = MAX(h-1, h) + 1 = h + 1


Assume T1 has new height H(T1) = h - 1 after
a deletion operation.

Now the node x becomes unbalanced because
H(y) - H(T1) = h + 1 - (h - 1) = 2.

A restructure operation is initiated to restore
balance at x.

y becomes the new root with left child x and right
child z.

Let y' denote the new subtree root.
new height of subtree rooted at y' is
H(y') = MAX(H(x), H(z)) + 1

[
the restructure operation swifted T2 to be the
right child of x.
]
H(x) = MAX(H(T1), H(T2)) + 1 = MAX(h-1, h - 1) + 1 = h
H(z) = h
=>
H(y') = MAX(h, h) + 1 = h + 1

Thus the delta is H(y) - H(y') = h + 2 - (h + 1)= - 1 => ABS(delta) = 1


the tree losses 1 height after restructure operation
"""
