"""

Let T be an n-node binary tree that may be improper. Describe how to
represent T by means of a proper binary tree T with O(n) nodes.

Answer:

A proper Binary Tree is a tree that has the following property:
1. Every Node has either zero or 2 childs.

Furthermore, a tree that is not proper is improper, i.e. has
at least one node with 1 children instead of two or zero.

In the worst case, every tree node in a binary tree has exactly one
Node (except the leaf node).

Let T' be such a (worst case) tree with N nodes. To make T' a proper tree,
I will create a dummy note for each node. Thus, I will traverse every
node in the tree, check which one is empty node,
and create a copy of its sibling.

This will effectively double the nodes of tree T', and the
algorithm will be O(2N), which is still O(N).


"""
