"""
We can define a binary tree representation T for an ordered general tree
T as follows (see Figure 8.23):
• For each position p of T, there is an associated position p of T' .

• If p is a leaf of T, then p in T' does not have a left child; otherwise
the left child of p is q , where q is the first child of p in T.

• If p has a sibling q ordered immediately after it in T, then q is the
right child of p in T'; otherwise p does not have a right child.

Given such a representation T of a general ordered tree T, answer each
of the following questions:

a. Is a preorder traversal of T equivalent to a preorder traversal of T?
b. Is a postorder traversal of T equivalent to a postorder traversal of T?
c. Is an inorder traversal of T equivalent to one of the standard traversals of T? If so, which one?

Answer:

a. On the preorder traversal of T, we visit the node and then its children.
Thus, for a preorder traversal of T and its corresponding T', we have the following cases:
1. A node is visited with no-children (a leaf node)
2. A node is visited with exactly one children
3. A Node is visited with more than one children

For case 1, the preorder traversal is the same (no children), we visit the the node at position p.
For case 2, the preorder traversal is also the same:
    For T, we visit p then p1
    For T', we visit p' and then the left node of p', which is the first child of p
For case 3, we the preorder traversal is also the same:
    For T, we visit p, then p1, then p2, then p3 etc
    For T', we visit p, then left node, which is the p1, and then p2', which is the right child of p1', and then p3'
    which is the right child of p2'.

b.
For a post order traversal, the node's children are visited first, then the node at position p.
Let us consider a case when we have 3 nodes, the last of which has exactly one child.
The postorder traversal looks like this:
p1->p2->child->p3->Parent
The postorder traversal of T' is this:
p1->child->p3->p2->Parent

The postorder traversal order is not the same, therefore T and T' do not have the same postorder

c.
In an inorder traversal of a binary tree, we visit first the position at the left(if it exists) of p,
then the position p, then the right of p.

The first child at position p always exist to the left of p', so an inorder traversal
first visits the children, then the parent node. If position p has more than one children,
the inorder traversal of the binary tree T' will first visit the first children c' (which is the left node), then
all the other children of, which are the right children of its previous sibling.

Thus, the inorder traversal of T' is the postorder traversal of T.

"""
