"""
Give a fast algorithm for concatenating two doubly linked lists L and M,
with header and trailer sentinel nodes, into a single list L′.

Answer:

L:
H <-> A <-> B <-> C <-> T
M:
H <-> 1 <-> 2 <-> 3 <-> T

L':
H <-> A <-> B <-> C <-> 1 <-> 2 <-> 3 <-> T

I need to assign the header of M to the trailer
of L. I also need to update LTrailer.Previous to
point to MHeader.next. I also need to update
MHeader.next to point to LTrailer.Previous.

I need to assign Header node of L to the Header
node of L'. On the trailer node of L, I need to
assign the header.next node of M.
I need to update
the Header.next node of M to point to the previous node
Trailer.Previous. I also need to update Trailer.Previous
of L to point to Header.next of M.



"""
