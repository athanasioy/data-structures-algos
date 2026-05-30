"""
Give a concrete implementation of the items( ) method in the context of
the MutableMapping class, relying only on the five primary abstract methods
of that class. What would its running time be if directly applied to the
UnsortedTableMap subclass?
"""

from collections.abc import MutableMapping


class EnumerableMutableMapping(MutableMapping):
    def items(self):
        for k in self:
            yield k, self[k]

# if applied to the UnsortedTableMap,
# the running time would be O(n^2),
# since we are executing n times
# the 'self[k]' operation, which
# itself is O(n).
