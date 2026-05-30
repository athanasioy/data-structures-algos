"""
Which of the hash table collision-handling schemes could tolerate a load
factor above 1 and which could not?
λ=n/N
"""


"""
ANSWER:
1. Separate Chaining -> include a second container for collisions
2. Open Addressing -> use table slots for collisions,
linear probing, quadratic probing, double hashing

By definition, the open addressing collision-handling
strategy can not handle a load factor above 1,
since the table itself is used to hold all
elements. It is not possible therefore to have
λ>1, which implies n>N, which implies that the
table stores more elements that its size.


Separate chaining on the order hand can handle
the load factor to be above one, albeit perfomance
does take a hit, since we increase the chance of collisions
thus making searching and inserting elements slower
"""
