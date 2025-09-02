"""
Describe a nonrecursive method for finding, by link hopping, the middle
node of a doubly linked list with header and trailer sentinels. In the case
of an even number of nodes, report the node slightly left of center as the
“middle.” (Note: This method must only use link hopping; it cannot use a
counter.) What is the running time of this method?


"Answer":
I will start by finding the header and trailer sentinels.
Let H and T start by being the header and the trailer node respectively.

I will then compare the next pointer of H with and Previous pointer of T.
If they are the same, then H.Next is the middle of the list. If H.Next is equal
T.Previous, then the list has an even number number of nodes and I will
return H.Next as the leftmost node. Else, I will continue the same operation
with H.next and T.Previous.

The running time is O(N) as the operation traverses the list at least once,
and the next operations traverse the list by n/2.
"""
