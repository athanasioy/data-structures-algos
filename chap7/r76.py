"""
Suppose that x and y are references to nodes of circularly linked lists,
although not necessarily the same list. Describe a fast algorithm for telling
if x and y belong to the same list.


Answer:
I will start at node X and loop through every next node.
If I find Y before X, X and Y belong to the same list.

next = X.next
found = False
while next !=X or not found:
    if next==Y:
        found = True
    next = next.next
return found
"""
