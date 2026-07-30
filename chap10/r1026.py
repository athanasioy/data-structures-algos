"""
Give a concrete implementation of the isdisjoint method in the context
of the MutableSet abstract base class, relying only on the five primary
abstract methods of that class. Your algorithm should run in O(min(n,m))
where n and m denote the respective cardinalities of the two sets.
"""


"""
def isdisjoint(self, other):
    if len(self) > len(other):
        smaller = other
        bigger = self
    else:
        smaller = self
        bigger = other

    for e in smaller:
        if e in bigger:
            return false

    return true
"""
