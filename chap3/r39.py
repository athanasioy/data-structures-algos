"""
Show that if d(n) is O(f(n)), then ad(n) is O(f(n)), for any constant
a > 0
Answer:
if d is O(f(n)), then there exist a n0 such that and a constant c

d(n)<=cf(n), for every n>=n0
=>
ad(n)<=acf(n) ,for every n>=n0

Thus, ad(n) is, by definition, O(f(n)),
since we have found a real number n=n0
and a constant c'=ac such that
ad(n) <= c'f(n)

"""
