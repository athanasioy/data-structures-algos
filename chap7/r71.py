"""
Give an algorithm for finding the second-to-last node in a singly linked
list in which the last node is indicated by a next reference of None.
Answer:
I will begin by asserting that the linked list has a size
greater than 1.
If the size is equal to two, then the second to last node is the Head Node.
Else, I will traverse the list while keeping the track of the previous
and current node WHILE the current node does not point to a None object.

When I reach the end, I will return the previous node.

"""

