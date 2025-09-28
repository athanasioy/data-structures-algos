"""
What are the minimum and maximum number of internal and external
nodes in an improper binary tree with n nodes?

Answer:

A binary tree that is improper has at least one
tree node that has exactly one node, (either left or right).


External Nodes:
Minimun is 1 (irrelevant of height)
1<=nE

The maximum case is reached where only one of the
binary tree does not have a sibling, hence
nE<=2^h - 1
1<=nE<=2^h-1

Internal Nodes:
Minumun case is when only one node (for example, the left node)
is populated but not the right, hence
h-1<=nI

The maximum case is reached where only one of the
binary tree does not have a sibling, hence
nI<=2^0 + 2^1 + ... + 2^(h-1) = 2^h-1


Also, the number of nodes in a tree is a function of
its height.

Answer2:
The most "minimal" improper tree is a tree
which resembles a straight line (all nodes have
exactly one sibling except root node).

Thus, the minimum number of external nodes
is 1.
Also the minimum number of internal nodes
is also this case, thus h-1<=nI

"""
