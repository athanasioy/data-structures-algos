"""
Let A be an array of size n ≥ 2 containing integers from 1 to n − 1, inclu-
sive, with exactly one repeated. Describe a fast algorithm for finding the
integer in A that is repeated

Answer:
Let k be the duplicated integer.
I will compute the sum, let the sum be S, of the integers in the list in O(n).
The sum of the integers is equal to the sum of integers from 1 to N-1 +k.
Thus S = (n-1)*(n)/2 + k.

=> k = S - (n-1)*n/2.
"""
