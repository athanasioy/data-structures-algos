"""
What is the running time of a call to T._height2(p) when called on a
position p distinct from the root of T? (See Code Fragment 8.5.)


def _height2(self,p):
    if self.is_leaf(p):
        return 0
    return 1 + max(self._height(c) for c in p.children)
Answer:

The worst running case of the above algorithm is O(N),
since every node is visited only once.
"""

