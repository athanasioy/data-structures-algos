"""
Dr. Amongus claims that the order in which a fixed set of entries is inserted
into an AVL tree does not matter—the same AVL tree results every time.
Give a small example that proves he is wrong.
"""


"""
ANSWER:
AVL Trees have the height-balancing property,
which means that in each tree position, the
height of the children differ at most by 1.


By previous exercise 11.04
we showed that the set {1,2} produces
different trees depending on order.

Trivially, these trees are also AVL trees,
thereby proving that the above statement is
wrong, since we found 1 counter example

"""
