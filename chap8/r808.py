"""
Answer the following questions so as to justify Proposition 8.8.
    a. What is the minimum number of external nodes for a proper binary
    tree with height h? Justify your answer.
    b. What is the maximum number of external nodes for a proper binary
    tree with height h? Justify your answer.
    c. Let T be a proper binary tree with height h and n nodes. Show that
    log(n+1)−1 ≤ h ≤ (n−1)/2.
    d. For which values of n and h can the above lower and upper bounds
    on h be attained with equality?


Answer:
A binary tree is proper when all nodes have either
two or zero children.
a)
Thus, the minimum number of external nodes happens
when only one node has leaf nodes at height h, and
the other external nodes are at height h-1.
This is equal to the number of nodes at height h-1 (i.e. 2^(h-1)) plus 1.

This is because to reach height "h" and preverse properness, we
add two nodes, two of which are now external and one of
them becomes internal, adding to the number of external nodes
by one (two new external nodes minus one external node).
Hence the total number of external nodes
for the minimum case is the number of nodes at level h-1 plus 1,
i.e 2^(h-1)+1.

b)
The maximum case is where all nodes at height "h" are external.

Hence, 2^h is the maximum external nodes.
c)
The maximum height w.r.t "n" for a proper binary tree
is achieved when the two nodes are added in the leaf node
with the greatest height and no two leaf node share the
same height.

In other words, for every two extra nodes (n+2), the
height is increased by 1. More generally, for
any k integer, k is even, the height is increased
by k/2.

Further more, for n=1 (only the root node), h=0.

Hence, 2h+1<=n => h <= (n-1)/2


The minimum height w.r.t to "n" for a proper binary
tree is achieved when binary tree is "full", i.e
there are the maximum amount of leaf nodes at all
heights from 0 to "h".

The maximum amount of leaf nodes L is 2^h
 =>
 L<=2^h

The leaf nodes is a proper binary tree is equal to
L=(n+1)/2
EXPL:

for a proper binary tree, every internal node
has two edges. The total number of edges in a
a proper binary tree is n-1 (a tree with n nodes
has n-1 edges).
Thus, 2I=n-1

we can also relate the total number of nodes
with internal and external nodes.

n=I+L
=> n=(n-1)/2 +L => (n+1)/2 = L

End of EXPL:

hence 2^h>=L=(n+1)/2 =>
2^h>=(n+1)/2 =>
h>= log(n+1) - 1

d)
for the lower bound:
h>=(n-1)/2
h=1 => n=3
h=2 => n=5
h=3 => n=7
...
n=f(h)=2h+1

every tall and thin proper binary tree


for the upper bound:
h=1 => n=3
h=2 => n=7
h=3 => n=15
...
n=f(h)=2^(h+1) - 1
"""
