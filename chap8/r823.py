"""
Let T be an ordered tree with more than one node. Is it possible that the
preorder traversal of T visits the nodes in the same order as the postorder
traversal of T? If so, give an example; otherwise, explain why this cannot
occur. Likewise, is it possible that the preorder traversal of T visits the
nodes in the reverse order of the postorder traversal of T? If so, give an
example; otherwise, explain why this cannot occur.

Answer:
First Q: Is it possible that preorder and postorder traversals
visit tree nodes in the same order?

Answer: No
Expl:
It is enough to show that a part of tree can never be
traversed in the same order in preorder and postorder
traversals in order to prove that these orders
can never be the same.

Consider the simplest tree with more than one node,
i.e. a tree with two nodes.

A preorder traversal visits first the root, then the child.
A postorver traversal visits first the child, then the root.
Therefore, any tree with more than one node can never have
the same preorder and postorder order.

Second Q:
Is the possible that the preorder traveral of a tree T
visit the nodes in reverse order of the postorder traversal?
Answer: Yes
Expl:
To prove the above statement, it is enough to find that
a tree T with more than one node exists that satisfied the above
condition.

Consider a tree T with two nodes, the root and the child.

A preorder traversal visits first the root, then the child.
A postorver traversal visits first the child, then the root.
The visiting order is reversed, thereby proving the statement.
"""
