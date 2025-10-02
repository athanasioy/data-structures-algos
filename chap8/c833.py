"""
Let T be a (possibly improper) binary tree with n nodes, and let D be the
sum of the depths of all the external nodes of T. Describe a configuration
for T such that D is Ω(n^2). Such a tree would be the worst case for the
asymptotic running time of method _height1 (Code Fragment 8.4).

def _height1(self): # works, but O(nˆ2) worst-case time
    return max(self.depth(p) for p in self.positions( ) if self.is leaf(p))

Answer:

Let T be a binary tree.
Tree T has the following property:
1. For every node n, every right node of n is an external node

This graphically means that the tree T "continues to grow"
from the left side,i.e. only the left nodes are allowed to have
children.

Let d be the maximum depth of tree T.

The computation of depth d of the external node at the greatest depth
completes by making n-1 computations, because it n-1 parent nodes
away from root.

The external node at the second greatest depth
computes by making n-2 computations.

The computation of the external node at depth
1 is completed by making 1 computation.

Thus, D making a total of (n-1) + (n-2) + ... + 2 + 1
calculations, which is equal to (n-1)*n/2, which is Ω(n^2).

"""
