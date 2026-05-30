"""
Modify our ProbeHashMap to use quadratic probing.
"""
from collections.abc import MutableMapping, abstractmethod
import random


class MapBase(MutableMapping):

    class _Item:
        def __init__(self, k, v):
            self.key = k
            self.value = v

        def __eq__(self, o):
            return self.key == o.key

        def __ne__(self, o):
            return not (self == o)


class HashMapBase(MutableMapping):
    def __init__(self, cap=11, prime=109345121,
                 load_factor_threshold: float = 2/3):
        self._table = cap * [None]
        self._n = 0
        self._load_factor_threshold = load_factor_threshold
        self._prime = prime
        self._scale = 1 + random.randrange(self._prime - 1)
        self._shift = random.randrange(self._prime)

    def _hash_function(self, key):
        return ((hash(key)*self._scale + self._shift)
                % self._prime) % len(self._table)

    @abstractmethod
    def _bucket_getitem(self, j, k):
        pass

    @abstractmethod
    def _bucket_setitem(self, j, k, v):
        pass

    @abstractmethod
    def _bucket_delitem(self, j, k):
        pass

    def __getitem__(self, k):
        bucket = self._hash_function(k)
        item = self._bucket_getitem(bucket, k)
        if item is None:
            raise KeyError(k)
        return item

    def __setitem__(self, k, v):
        if self._load_factor >= self._load_factor_threshold:
            self._resize(len(self._table)*2)
        bucket = self._hash_function(k)
        self._bucket_setitem(bucket, k, v)
        # self._n += 1
        # self._n is incremented inside _bucket_seitem

    def _resize(self, new_size):
        old = list(self.items())
        self._table = new_size * [None]
        self._n = 0  # IMPORTANT! do not set an infinite loop
        for k, v in old:
            self[k] = v

    @property
    def _load_factor(self):
        return self._n/len(self._table)


class ProbeHashMap(HashMapBase):
    _AVAIL = object()

    def _is_avail(self, j):
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, key, j):
        firstAvail = None
        i = 0
        while True:
            probeIdx = (j + i**2) % len(self._table)
            if self._is_avail(probeIdx):
                if firstAvail is None:
                    firstAvail = probeIdx
                if self._table[probeIdx] is None:
                    return (False, firstAvail)
            elif self._table[probeIdx].key == key:
                return (True, probeIdx)
            i += 1
