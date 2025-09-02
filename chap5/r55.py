"""
Redo the justification proposition
5.1 assuming that the cost of growing
the array from k to size 2k in 3k cyber-dollars.
How much should each append operation be charged
to make the amortization work?

Answer:
Assume that one cyber-dollar is enough for
each append operation and for resizing
from k to 2k costs 3k cyber-dollars.

A resize operation happens at some integer
i at position 2^i, at which position the array
doubles in size.
Thus, a resize operation costs 3*2^i cyber dollars.
These dollars be found between elements 2^(i-1) to
2^(i)-1, i.e. in 2^(i-1) elements inside these two
indexes.

thus:
let k be the resize point at 2^(i-1)
thus resize operation costs 3*k=3*2^(i-1)
2^(i-1)*c=3*2^(i-1) =>
c=3 cyber dollars must over-charged to amortize the cost
of the resize operation. Thus each charge should be
4 dollars to cover to for the append cost itself.
"""
