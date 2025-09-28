"""
Give the output of the function parenthesize(T, T.root( )), as described
in Code Fragment 8.25, when T is the tree of Figure 8.8

Answer:
- ( / ( X ( + ( 3, 1) , 3) , + ( - ( 9, 5), 2 ) ) + ( X (3), - (7,4), 6 ))
"""

def parenthenise_tree(T,p):
    print(p.element(), end="")
    if not T.is_leaf(p):
        first_time = True
        for child in T.children(p):
            sep = "( " if first_time else ", "
            print(sep, end="")
            first_time = False
            parenthensize_tree(T,child)
        print(" )", end="")

