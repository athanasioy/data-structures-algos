"""
Describe in detail how to swap two nodes x and y (and not just their con-
tents) in a singly linked list L given references only to x and y. Repeat
this exercise for the case when L is a doubly linked list. Which algorithm
takes more time?


"Answer":

Let x and y be instances of a Node class.

For the Singly Linked List:
===============================
HEAD -> a -> x -> c -> b -> y -> z -> TAIL
To Swap x, y I need only to swap their next pointers.
(wrong, as illustrated below)
HEAD -> a -> x -> z -> b -> y -> c -> TAIL

To swap the positions of X, Y in a linked list,

I need to update the nodes that are pointing to X,Y.
HEAD -> a -> y -> c -> b -> x -> z -> TAIL
Let the previous nodes of X,Y be XPrev and YPrev respectively.
I need to update XPrev to point to Y and YPrev to point to X.
I also need to swap Y.Next and X.Next

For that, I will traverse the entire list and find XPrev and YPrev.
I will do that in a while loop by inspecting the current and previous node
until I find both XPrev and YPrev. If the current node is X or Y, I will
assign XPrev or YPrev respectively.

Once I find them, I will update their next pointers as described above.
I will also swap X.Next and Y.Next

For the Double Linked List:
==============================
HEADER <-> HEAD <-> a <-> x <-> c <-> b <-> y <-> z <-> TAIL <-> TRAILER
For the swap to happen, I need to Swap Y.Previous with X.Previous,
Y.Next with X.Next and XPrev.Next with YPrev.Next.

This algorithm is obviously faster, since I dont need to traverse
the whole tree find the nodes that I am looking for. (X and Y
have a reference to the previous node.)

"""
