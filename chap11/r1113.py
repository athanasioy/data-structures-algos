"""

The rules for a deletion in an AVL tree specifically require that when the
two subtrees of the node denoted as y have equal height, child x should be
chosen to be “aligned” with y (so that x and y are both left children or both
right children). To better understand this requirement, repeat Exercise R-
11.11 assuming we picked the misaligned choice of x. Why might there
be a problem in restoring the AVL property with that choice?

"""


"""
ANSWER:

Let z be the unbalanced node and y being the child
with the greater height. Let x and T1 be the children of
y which equal height.

Without loss of generality assume y is the right child
of z. Assume also that x is the right child of y.


Let z have height H(z) = h + 2
H(y) = h + 1 and H(x) = h, H(T1) = h

The fact that z in unbalanced directly implies that
H(T2) = h - 1

We do a rotation to restore the balance at z.

Instead of picking x to do a rotation on z<->y,
we pick T1 and do tri-noode restructuring.


After a trinode restucturing, we arrive at a
new subtree with T1 root, y as the right child
and z as the left child.

y has in turn as left child x and as right child
the left child of T1.

Let T1_left denote the left child of T1 and
T1_rgiht denote the right child of T1.

Since H(T1) = h => MAX(T1_left,T2_right) + 1 = h
=> (assuming subtree T1 is an AVL tree)
T1_left = h - 2 or T1_left = h - 1

If T1_left = h - 2 => subtree at y is imbalanced
since |H(T1_left) - H(x)| = |h - 2 - h| = 2

"""
