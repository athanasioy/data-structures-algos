"""
There seems to be some redundancy in the repertoire of the positional
list ADT, as the operation L.add first(e) could be enacted by the alter-
native L.add before(L.first( ), e). Likewise, L.add last(e) might be per-
formed as L.add after(L.last( ), e). Explain why the methods add first
and add last are necessary.

answer:
the add first method is necessary because add_before(l.first(), e)
method F A I L S.

Specifically, First() return the header node (let it be H)
when the list is empty and proceeds to insert between
H.Previous and H. However, H.Previous is None in this case.

The same holds true with the Add_last and add_after method
calls. In this case, the trailer node gets returned, which
in turn has a .next element of None. Thus the add_after
call fails as well.

Answer (Correct One):

When the list is empty, the First() call returns None,
because the next node is the trailer node, and make position
makes sure not to return sentinel nodes. Thus, the
call to add_before would fail.
"""
