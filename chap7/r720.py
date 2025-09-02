"""
Let L be a list of n items maintained according to the move-to-front heuris-
tic. Describe a series of O(n) accesses that will reverse L.


Answer:
WRONG
=====
Assuming that L is sorted by recency, with
the most recent time being the first, I need
to describe a series of O(n) access that
reverse L, meaning that the first element
of N is the least recent.


I am also assumnig that L is a PositionalList.

I will accomplish the reversin of L by
getting the first position of L and adding
it to the back L for every element of L.

I will take the front and back element,
I will store back.previous and the front.next
into local variables, and I will swap positions.
If back.previous is front.next, I have reached
the middle of the list, so that means I will stop.
Also, if back.previous.previous is front.next, I need to
swap and end the reversing, since I have reached
adjanced nodes in the middle of the list.

SECOND ATTEMPT:
===============
To reverse L, i need to bring the least recent
to the front and the most recent to the back.


Let the length of L be n. For 1 to n-1,
I will access each Position of the List.
For example, in the first iteration, I will
access the second element, the third iteration
the third etc. By position I meant how far
away to move from the head of the list .
For the final iteration, I will
access the last element.
This has effectively reversed the list


"""
