"""
Give a proof by induction of Proposition 8.9


In a nonempty proper binary tree T, with nE external nodes and
nI internal nodes, we have nE = nI +1.

Answer:
Proof by induction.
1)
n=1 (base case)
when we have only the root node, we have one
external node and 0 internal ones.
nE=1
nI=0
nE=nI+1 => 1 = 0 + 1

The equality holds for n=1
2)
(induction)

assume nE=nI+1 holds for n
prove that nE'=nI'+1 for n+2 (+2 in order to maintain properness of tree)

When we add two nodes to binary tree, we
convert an existing leaf node to an internal one,
and add two new external nodes. Hence,
we add one external (2 new ones minus 1 node that became internal)
and one internal node (the old external node).

Thus, nE' = nE+ 1 => nE = nE' -1
and nI' = nI + 1 => nI = nI' -1

nE = nI +1 => nE' -1 = nI' -1 +1 => nE' = nI' +1
end of proof.
"""
