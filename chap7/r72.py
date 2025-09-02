"""
Describe a good algorithm for concatenating two singly linked lists L and
M, given only references to the first node of each list, into a single list L′
that contains all the nodes of L followed by all the nodes of M.

Answer:

I will create a new linked linked list L' intially empty.
I set the head of the L' to the first node of list L.
Then I will traverse to the end of the linked list
and find the tail. Once I find the tail, I will set the
tail of the linked list L' to the head of M.

"""
