"""
Let T be a binary tree with n nodes, and let f() be the level numbering
function of the positions of T, as given in Section 8.3.2.
a. Show that, for every position p of T, f(p) ≤ 2^n −2.
b. Show an example of a binary tree with seven nodes that attains the
above upper bound on f(p) for some position p

Answer:

f(p)=0, if p is root
f(p)=2f(q) + 1, where q is p's parent and p is left of q
f(p)=2f(q) + 2, where q is p's parent and p is right of q

a)
I need to show that f(p)<=2^n -2, for every p in
a binary tree with n nodes.

For that, I need to find the position(s) p
that f(p) achieves a maximum.

Trivially, these are the leaf positions.
PROOF:
let some position p' that is not leaf position
of a binary tree have level numbering of f(p').
Since p' is not a leaf position, p' has either
a left or a right node. Without loss of generality,
let left p_left be an existing child node of p'.
p_left has a level position equal to 2f(p')+1,
which is obviously greater than f(p').
Hence, for every position that is not a leaf,
I can find a position with a greater level number.
Therefore, the maximum level position must exist
on a leaf position.
END OF PROOF:

Futhermore, from the recursive definition of f(p),
which depends on th parent node, we trivially conclude
that the leaf position with the greatest depth has
the greater level numbering.

Therefore, the maximum depth position that we can
achieve in a binary tree with n nodes is a tree
that is tall and thin like a straight line. Moreover,
in order to increase the level numbering position,
that tree has to fill the right node only.

Thus, for the maximum depth position we get

f(p)=2f(q)+2
= 2(f(q')+2)+2
= 2(2(2f(q'')+2)+2)+2
= 2^n-1 + 2*n-2 + ... 2
(Observe that the first 2 gets multiplied n-1 times,
the second 2 gets multiplied n-2 times..etc)
=>
f(p)=2^n-1 + 2*n-2 + ... 2 + 1 -1 =2^(n) -1 -1 = 2^n-2

PROOF OF f(p)=2^n-1 + 2*n-2 + ... 2

let p0 be the root and pn be the right child of parent
f(p0)=0
f(p1)=2*0 +2=2
f(p2)=2*2 +2
f(p3)=2*(2*2 +2) +2 = 2*2*2 + 2*2 +2
f(p4)=2*(2*2*2 +2*2 +2) +2=2*2*2*2 + 2*2*2 + 2*2 + 2 (depth=5)

generalizing
f(p)= 2^(d-1) + 2^(d-2) + ... + 2

END OF PROOF f(p)=2^n-1 + 2*n-2 + ... 2


"""
