"""
The collections.deque class supports an extend method that adds a collection of elements to the end of the queue at once. Reimplement the
breadthfirst method of the Tree class to take advantage of this feature
"""


from collections import deque


def breath_first(tree):
    Q = deque()
    root = tree.root()
    Q.append(root)
    while Q.count >0:
        p = Q.popleft()
        Q.extend(tree.children(p))
        yield p

