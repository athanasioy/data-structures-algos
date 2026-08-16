"""
Draw the AVL tree resulting from the removal of the entry with key 62
from the AVL tree of Figure 11.14b.
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

after delete 62:
replace 62 with the position before (in our tree 54)
           54
        /      \
       /        \
     44          78
    /  |           \
  17    50          88
       /
      48

tree is balanced
"""
