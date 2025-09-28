"""
Justify Table 8.2, summarizing the running time of the methods of a tree
represented with a linked structure,
by providing, for each method, a description of its implementation,
and an analysis of its running time

len, is empty O(1)
root, parent, is root, is leaf O(1)
children(p) O(cp +1)
depth(p) O(dp +1)
height O(n)

cp=> number of children at position p
dp => depth at position p
Answer:

len is O(1) because the class 'LinkedBinaryTree' explicitly
holds a self._size variable which is returned by the __len__
method.

Trivially, reading for a memory location is considered
O(1).


'is_empty' can also be trivially implemented by
comparing __len__ to 0.

root, parent are also O(1) because the _Node
class holds explicit references to both of them.
'is_root' can also be trivially implmemented in O(1)
by comparing object reference equality with the root node.

is_leaf can also be implemented in O(1) by comparing
the 'num_children' call to zero.The 'num_children'
is O(1), since all it does is read the memory locations
self._left and self._right and increment a counter.

children is O(cp) because we read (or yield)
all the children at position P and return
them to the caller.

depth at position P is O(dp) because we
make a recursive to the depth of the parent
until we reach the root.


height is O(N) beacuse to find the height
of a node N, we have to traverse all its children
recursively. If node N is the root, we have to traverse
all tree nodes.
"""
