"""
Draw the AVL tree resulting from the insertion of an entry with key 52
into the AVL tree of Figure 11.14b.
"""


"""
ANSWER:

    original tree:
           62
        /      \
       /        \
     44          78
    /  |           \
  17    50          88
       /  \
      48   54


    after inserting 52:
           62
        /      \
       /        \
     44          78
    /  |           \
  17    50          88
       /  \
      48   54
          /
         52

tree is unbalanced ar 44: (height of 17 =1, height of 50=3, diff =2 > 1)

After balancing
           62
        /      \
       /        \
     50          78
    /  \           \
  44    54          88
 / \    /
17  48 52
"""
