"""
What is the worst-case asymptotic running time for performing n deletions
from a SortedTableMap instance that initially contains 2n entries?
"""


"""
SortedTableMap holds its element in inside
a sorted dymanic array. Deletions in dynamic arrays
are O(n), since the worst case of a deletion in
a dynamic array is the deletion of the first position,
which requires a location of n-1 elements in the array.

Thus, in a SortedTableMap, n deletions have a
worst time n*O(n), thus O(n^2).
"""
