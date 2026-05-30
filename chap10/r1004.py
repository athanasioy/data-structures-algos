"""
What is the worst-case running time for inserting n key-value pairs into an
initially empty map M that is implemented with the UnsortedTableMap
class?
"""


"""
ANSWER:
The worst running time of n calls of __setitem__
in a UnsortedTableMap occurs when every
key is unique, hence for each insert the
entire table is scanned.
In an initially empty table, thus, we
make n scans, each of which makes 1,2,3...
up to n comparisons.
Thus, the worst running time is O(n^2)
"""
