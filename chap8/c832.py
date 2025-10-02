"""
Let T be a (not necessarily proper) binary tree with n nodes, and let D be
the sum of the depths of all the external nodes of T. Show that if T has the
minimum number of external nodes possible, then D is O(n) and if T has
the maximum number of external nodes possible, then D is O(nlogn).

"Answer":

A Tree with the minimum number of external nodes (nE) is a
tree which is tall and thin and resembels a straight line.

This tree has only one external node, and the rest are internal.
Thus D is the calculation of the depth at the external position.

The calculation is a recursive call until we reach the root,
thus we make n-1 recursive calls, which is O(N). (Obviously,
every operation in the depth calculation is O(1), which
consist of reading values from memory locations.)


A Tree with the maximum external nodes is a binary tree
which is "bushy",i.e. has all heights filled except
the last height, which is filled up to the possible point
given the constraint
that the tree has (fixed) N number of nodes.

For n nodes, the maximum number of depth that
the tree can achieve is floor of log(n+1) -1, since the next
level of nodes requires double the amount of nodes.

Also, the number of external nodes in a bushy tree
is ceiling of n/2.

Let h the the maximum depth of tree T.
Let nEh-1 be the number of exteral nodes
that exist at h-1 and nEh be the number
of external nodes that exist in height h.

Then,
D becomes

D=nEh-1*(h-1) + nEh*h <= nEh-1*h + nEh*h - nEh-1 =nE*h -nEh-1 <= nE*h

Therefore, since:

1. h is O(log(n))
3. nE is O(n)
therefore D is O(nlogn)
"""
