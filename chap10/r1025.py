"""
Give a concrete implementation of the pop method, in the context of a
MutableSet abstract base class, that relies only on the five core set behav-
iors described in Section 10.5.2.
"""

"""

"""


class MutableSet:

    def add(self, e):
        pass

    def discard(self, e):
        pass

    def __contains__(self, e):
        pass

    def __len__(self):
        pass

    def __iter__(self):
        pass

    def pop(self):
        for e in self:
            self.remove(e)
            return e

    def remove(self, e):
        pass

    def clear(self):
        pass
