"""
Let T be a tree with n positions. Define the lowest common ancestor
(LCA) between two positions p and q as the lowest position in T that has
both p and q as descendants (where we allow a position to be a descendant
of itself ). Given two positions p and q, describe an efficient algorithm for
finding the LCA of p and q. What is the running time of your algorithm?


Answer:

Given two positions p, q in a tree, we need to find the lowest common
ancenctor.
Worst case, this ancenstor is root.

First, start off by choosing a position. let that position be p.

we append into a list all of p's ancenstors, including p it self,
in ascending oder.

then we choose position q. For each q's ancenctor, including q itself,
we scan the list p's ancestors. If we find a match,that match is the
lowest common ancenstor and we end the algorithm.

Complexity of the algorthim:

Since we are given a tree T, the worst case of the first tasks (
collecting p's ancenstors) is O(n), where n is the number of nodes.


The second task which is comparing each ancenstor with every element
in p's ancenstor chain is executed at most N times for a list
with at most n elements, so worst case this comparison executed
n*n=n^2 times, thus complexity of the second task is O(n^2).

O(n) + O(n^2) is O(n^2), thus the complexity of the algortihm is
O(n^2).

"""
