"""
Our definition of the level numbering function f(p), as given in Section 8.3.2, began with the root having number 0. Some authors prefer
to use a level numbering g(p) in which the root is assigned number 1, because it simplifies the arithmetic for finding neighboring positions. Redo
Exercise R-8.18, but assuming that we use a level numbering g(p) in
which the root is assigned number 1

f(p)=1, p is root
f(p)=2f(q), p is left of q
f(p)=2f(q) +1, p is right of q

tree.root():
    return A[1]

tree.parent(p):
    for i from 1 to A.count:
        if A[i] == p.node:
            index =i
    if index ==1:
        return
    if index mod 2 ==0:
        return A[index/2]
    else:
        return A[(index-1)/2]

tree.left(p):
    for i from 1 to A.count:
        if A[i] == p.node:
            index =i
    return A[i*2]

tree.right(p):
    for i from 1 to A.count:
        if A[i] == p.node:
            index =i
    return A[index*2+1]

tree.is_leaf(p):
    for i from 1 to A.count:
        if A[i] == p.node:
            index =i
    return A[2*index] is not null and A[2*index+1]
tree.is_root(p):
    return A[1] is p.node
"""
