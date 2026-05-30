"""
Consider the following variant of the find index method from Code Frag-
ment 10.8, in the context of the SortedTableMap class:

def _find_index(self, k, low, high):
    if high < low: 
        return high + 1
    else:
        mid = (high + low) // 2
        if self._table[mid].key < k:
            return self._find_index(self,k, mid + 1, high)
        else:
            return self._find_index(self, k, low, mid - 1)

Does this always produce the same result as the original version? Justify
your answer.

Answer:
Original Version:
def _find_index(self, k, low, high):
    if high < low:
        return high + 1
    # no element qualifies
    else:
        mid = (low + high) // 2
        if k == self. table[mid]._key:
            return mid # found exact match
        elif k < self. table[mid]._key:
            return self. find index(k, low, mid - 1) # Note: may return mid
        else:
            return self. find index(k, mid + 1, high)

No, the code is not equevalent in output. The provided code never checks
for self._table[mid].key == k, hence it fails to find matching indexes. w
"""
def binary_search(  array, value, low, high):

    if low > high:
        return high + 1

    mid = (low + high) // 2
    if array[mid] == value:
        return mid
    if array[mid] > value:
        return binary_search(array, value, low, mid - 1)
    if array[mid] < value:
        return binary_search(array, value, mid + 1, high)


array = [1, 5, 6, 9, 13, 22, 55, 56, 57, 100]


print(binary_search(array, 5, 0, len(array) - 1))
print(binary_search(array, 1, 0, len(array) - 1))
print(binary_search(array, 100, 0, len(array) -1))
print(binary_search(array, 101, 0, len(array) -1))
