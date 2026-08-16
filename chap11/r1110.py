"""
Explain why performing a rotation in an n-node binary tree when using
the array-based representation of Section 8.3.2 takes Ω(n) time.
"""


"""
Array-based represention of node position in a binary tree
is as follows:
f(p) =0, when p is root
f(p) = 2f(q) + 1, when p is left child of q
f(p) = 2f(q) + 2, when p q is right child of q

rotating positions x,y where x is child of y involves:
    1. changing the pos of x
    2. changing the pos of y
    3. changing the position of all nodes right x to be the left subtree of y
    4. changing the position of the left subtree of x, since x has now moved
    up the tree, thereby all children of x children's need to be calculated
    again
    5. Same argument holds of the right subtree of y

if y is root, then that means all positions indexes need to be
recalcuated in an array based implementation, which is Ω(n).

"""
