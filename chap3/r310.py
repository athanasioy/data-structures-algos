"""
Show that if d(n)is O(f(n)) and e(n) is O(g(n)), then the product d(n)e(n)
is O(f(n)g(n)).

Answer:
if d(n) is O(f(n)), then there is a constant c and a number n0
such that

d(n)<=cf(n) (1), for every n>=n0

respectively

e(n)<=c'g(n) (2), for every n>=n0'

Since in algorithmic analysis, negative "cost" values are not
defined, we assume d(n)>0 and e(n)>0

Since n0 and n0' are real numbers, if n0 and n0' are not equal,
one is larger than the other.

Without loss of generality, we assume that n0' is greater
than n0

(1) and (2)
=>
d(n)e(n) <=c*c'*f(n)*g(n), for every n>=n0'

thus,by definion, d(n)e(n) is O(f(n)g(n)),
since we have found a real number z=c*c'
and a n'=n0'

such that

d(n)e(n) <=c*c'*f(n)*g(n), for every n>=n0'
"""
