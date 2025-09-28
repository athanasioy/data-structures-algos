"""
Answer the previous question for the case when T is a proper binary tree
with more than one node

Answer:
First Q:
Answer: No
Expl: for the same reason

Second Q:
Answer: No
Expl:
Consider the simplest proper binary tree, i.e.
a tree with 3 nodes.

A preorder traversal will visit root->left->right
A postorder traversal will visit left->right->root

These sequence is not reversed in the simplest case,
therefore all trees can not have preorder and postorder
traversals reversed, due to the fact that all tree
traversals will pass that particular segment of the
tree with a non-reversed order.

"""
