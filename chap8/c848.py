"""
Given a proper binary tree T, define the reflection of T to be the binary
tree T such that each node v in T is also in T, but the left child of v in T
is v’s right child in T and the right child of v in T is v’s left child in T.
Show that a preorder traversal of a proper binary tree T is the same as the
postorder traversal of T’s reflection, but in reverse order.

Answer:
A proper binary is a tree that each node has two or zero
children.

T' is a reflection of T, that is that each node n in T is
also in T', and that each left child of node n in T
is the right child of n is T'.

We need to show that a preorder traversal of T is
the postorder travel T' in reverse order. It it enough
to show this holds in arbitrary node n of tree T.

Assume node n that exists in some position in tree T
with children n1 (left) and n2 (right).
Preorder traversals first visit the parent node and then
then children from left to right. Thus, the nodes are visited in the following
order:
n[parent] -> n1[left child] ->[children of n1] -> n2[right child] ->[children of n2]

Postorder traversals first visit the children (from left to right) and then the
parent,thus the postorder traversal of T' at the same node n is as follows:

[children of n2] -> n2[left child in T'] -> [children of n1] -> n1[right child in T'] -> n[parent]

Observe that the preorder traversal of T is the reversed postorder traversal
of T'.


"""
