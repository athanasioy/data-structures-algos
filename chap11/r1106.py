"""
Our implementation of the TreeMap. subtree search utility, from Code
Fragment 11.4, relies on recursion. For a large unbalanced tree, Python’s
default limit on recursive depth may be prohibitive. Give an alternative
implementation of that method that does not rely on the use of recursion.
"""

"""
def _subtree_search(self, p, k):
    ”””Return Position of p s subtree having key k, or last node searched.”””
    if k == p.key():
        # found match
        return p
    elif k < p.key():
        # search left subtree
        if self.left(p) is not None:
            return self. subtree search(self.left(p), k)
    else:
        # search right subtree
        if self.right(p) is not None:
            return self. subtree search(self.right(p), k)
    return p


ANSWER:
def _subtree_search(self, p, k):
    cursor = p
    while cursor is not null:
        if cursor.key == k:
            return cursor
        elif cursor.key > k:
            next = cursor.left
        else:
            next = cursor.right
        if next is None:
            return cursor
        cursor = next
    return None

"""
