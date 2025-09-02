"""
Prove that when using a dynamic array that grows and shrinks as in the
previous exercise, the following series of 2n operations takes O(n) time:
n append operations on an initially empty array, followed by n pop oper-
ations

Answer:
We have already proven that N append operations
on an array that resizes from N to 1,25N is O(n).

We now have to prove that the pop method that
shrinks from C to C/2 when N is below C/4,
where C is the total capacity, is also O(n).

For N elements, we can have a total of
k resize operations until capacity reaches 1.
N*(1/2)^k=1 -> 2^-k = 1/N => k = logN

For simplicity and without loss of generality,
we assume that the capacity C is a power of two.

The total cost of the shrinks operation is as follows:
S=C/2 + C/4 + C/8 + C/16 + ... + 1 = C*(1/2^k-1)/(1/2-1)
(geomtric series sum with a=C, r=1/2 and k number of operations)
since k =logN, S is O(n)

When popping from an array that does not trigger a resize,
the cost is obviously O(1).

Hence the total cost of shrinking an Array from N elements
is O(n)
"""
