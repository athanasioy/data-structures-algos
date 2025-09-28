"""
Let T be a binary tree with n positions that is realized with an array representation A, and let f() be the level numbering function of the positions
of T, as given in Section 8.3.2. Give pseudo-code descriptions of each of
the methods root, parent, left, right, is leaf, and is root.


Answer:

tree.root():
    return A[0]

tree.parent(p):
    for i from 0 to A.count - 1:
        if A[i] == p.node:
            index = i
    if index == 0:
        return

    if index mod 2 == 0:
        parent_idx = (index-2)/2
    else:
        parent_idx = (index-1)/2
    return A[parent_idx]

tree.left(p):
    for i from 0 to A.count - 1:
        if A[i] == p.node:
            index = i
    idx = 2*index +1
    return A[idx]

tree.right(p):
    for i from 0 to A.count - 1:
        if A[i] == p.node:
            index = i
    idx = 2*index +2
    return A[idx]


tree.is_leaf(p):
    for i from 0 to A.count - 1:
        if A[i] == p.node:
            index = i
    left = 2*index +1
    right = 2*index +2
    return A[left] is null and A[right] is null

tree.is_root(p):
    return p.node is A[0]
"""
