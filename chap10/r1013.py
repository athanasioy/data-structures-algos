"""
What is the worst-case time for putting n entries in an initially empty hash
tale, with collisions resolved by chaining? What is the best case?


Answer:
in the worst case, we have n-1 collisions (all keys hash to the same index) and
all elements have distinct keys.
For each collision, we append each element to the same
secondary container after checking all existing
elements for equality.
Hence, we make 1,2,3,...,n-1 comparisons, which is O(n^2).

the best case is that all elements map to distinct indexes, which is O(1).
Since we are adding N elements, each of each takes
O(1) time, the total time is O(n).
"""
