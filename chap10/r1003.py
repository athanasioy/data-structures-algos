"""
Give a concrete implementation of the items( ) method directly within the
UnsortedTableMap class, ensuring that the entire iteration runs in O(n)
time.
"""

from collections.abc import MutableMapping


class MapBase(MutableMapping):

    class _Item:
        def __init__(self, k, v):
            self.key = k
            self.value = v

        def __eq__(self, o):
            return self.key == o.key

        def __ne__(self, o):
            return not (self == o)


class UnsortedTableMap(MapBase):

    def __init__(self):
        self._table = []

    def __setitem__(self, k, v):
        for i in range(len(self._table)):
            if k == self._table[i].key:
                self._table[i] = self._Item(k, v)
                return
        self._table.append(self._Item(k, v))

    def __getitem__(self, k):
        for i in range(len(self._table)):
            if k == self._table[i].key:
                return self._table[i].value
        raise KeyError(k)

    def __iter__(self):
        for i in self._table:
            yield i.key

    def __len__(self):
        return len(self._table)

    def __delitem__(self, k):
        for i in range(len(self._table)):
            if k == self._table[i].key:
                value = self._table.pop(i)
                return value
        raise KeyError(k)

    def items(self):
        for i in range(len(self._table)):
            yield self._table[i].key, self._table[i].value
