"""
Give a concrete implementation of the pop method in the context of the
MutableMapping class, relying only on the five primary abstract methods
of that class.
"""

from collections.abc import MutableMapping
# MutableMapping has 5 abstract methods
# __getitem__, __setitem__, __delitem__,
# __iter__, __len__


class PopableMutableMapping(MutableMapping):
    def pop(self, k, default=None):
        try:
            val = self[k]
            del self[k]
            return val
        except KeyError:
            if default is not None:
                return default
            raise
