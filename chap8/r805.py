"""
Describe an algorithm, relying only on the BinaryTree operations, that
counts the number of leaves in a binary tree that are the left child of their
respective parent.

T.left(p) -> return left children of p
T.right(p) -> return right children of p
T.children(p) -> iterator for children of p
Answer:
I will iterate the children of root node. I will also
initialize an integer variable 'cnt' with the value
of zero.
I will check if the left node exists and has no children;if so, i will
increment cnt by one.
I will then recursively iterate the children of the left node
and the right node.
"""
