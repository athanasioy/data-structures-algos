"""
Define the internal path length, I(T), of a tree T to be the sum of the
depths of all the internal positions in T. Likewise, define the external path
length, E(T), of a tree T to be the sum of the depths of all the external
positions in T. Show that if T is a proper binary tree with n positions, then
E(T) = I(T) +n−1.

Answer:

We will prove the statement
E(T) = I(T) +n−1 (1)
by induction (sadly I cannot find a more clever way to do it...)

We need to show that:
1. statement (1) holds for the base case (n=1)
2. if E(T) = I(T)+ n-1 is true for some n, then
E(T') = I(T') +n' -1 is true for n' = n +2.
(Note that we add two nodes to maintain
binary tree properness)


for 1. we have a tree with only one node, the root node.
Since the root node is an external node (no children)
and has a depth of 0,
the equation
0=0+1-1 holds.

Now we need to show statement 2.

Assume E(T)=I(T) +n -1 for n=n0 nodes.
When we add two nodes to a proper binary tree,
we add two external nodes and convert external node
to internal. Assume,without loss of generality,
also that we add the nodes at depth d.
Also note that n'=n0+2

Thus,
E(T') = E(T) +(d +1) + (d+1) - d => E(T) = E(T') - (d+2)
consequently,
I(T') = I(T) + d => I(T) = I(T') -d

Thus,
E(T)=I(T) +n -1=>
E(T') - (d+2) = I(T') -d + n -1 =>
E(T') = I(T') n + 2 -1 => (n+2 =n')
E(T') = I(T') +n' -1
thus we have proven statement 2.

Since we shown 1 and 2, we have proved the statement by induction.
"""
