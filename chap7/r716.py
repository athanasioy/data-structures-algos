"""
Describe an implementation of the PositionalList methods add last and
add before realized by using only methods in the set {is empty, first, last,
prev, next, add after, and add first}.

"Answer":
Add last method:

Add last method needs to insert a node between
the last node and the trailer node.
I need to get a reference to those two nodes.
I can get those references by calling
last() and next(last()) respectively.

If the list is empty, I can use Add First
to add to last

add before method:

I can implement add before by
getting a refernce to previous node
and calling add after.

let "n" be the node i want to add after
I can implement add before as follows:
add_after(n.previous)


"""
