"""
Describe how a sorted list implemented as a doubly linked list could be
used to implement the sorted map ADT.
"""

"""
Answer:
The sorted map ADT allow the user to
find efficiently the minimum and maximum
entries, as well as find keys in a given
range.

It is therefore convienet to have items
be placed in a sorted list for the sorted map
ADT, since minimum and maximum operations
take O(1) time, while searching is O(logn)
via binary search. It is enough, therefore,
to show how to implement a sorted list
via a doubly linked list in order to realize
the map ADT.


We can implement a sorted list via doubly
linked list by keeping the minimum value
at the start of the list and the maximum value
at the end of list. With this we can achieve
minimum and maximum values in O(1) time. Searching,
however, still requires O(N) time, since we
are unable to do binary search on a doubly linked list.


"""
