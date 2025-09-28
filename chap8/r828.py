"""
What is the running time of parenthesize(T, T.root( )), as given in Code
Fragment 8.25, for a tree T with n nodes?
Answer:

p.element() runs in O(1)
T.is_leaf(p) runs in O(1)
assingiments and prings are O(1)
parenthensise_tree is executed for every Tree node N
Thus, parenthensise_tree is O(N)
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

