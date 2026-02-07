"""
Give an O(n)-time algorithm for computing the depths of all positions of
a tree T, where n is the number of nodes of T.
"""
from abc import ABC, abstractmethod
class Tree(ABC):
    class Position:
        @abstractmethod
        def element(self):
            ...

        @abstractmethod
        def __eq__(self,other):
            ...

        def __ne__(self,other):
            return not (self == other)

    @abstractmethod
    def root(self):
        ...

    def is_root(self, p):
        return p == self.root()

    @abstractmethod
    def num_children(self,p):
        ...

    def is_leaf(self,p):
        return self.num_children(p)==0

    @abstractmethod
    def children(self,p):
        ...

    @abstractmethod
    def parent(self,p):
        ...

    @abstractmethod
    def __len__(self,p):
        ...

    def is_empty(self):
        return len(self)==0

    def height(self,p):
        if self.is_leaf(p):
            return 0
        return max((self.height(c) for c in self.children(p)))


class Node:
    def __init__(self, value, children, parent):
        self.value = value
        self.children = children if children else []
        self.parent = parent
class LinkedTree(Tree):


    class Position(Tree.Position):
        def __init__(self, node, container):
            self.node = node
            self.container = container

        def element(self):
            return self.node.value

        def __eq__(self,other):
            if isinstance(other,self):
                return other.node is self.node
            return False

    def __init__(self):
        self._size= 0
        self._root = None

    def _make_pos(self, node):
        if node is not None:
            return self.Position(node,self)

    def _validate(self,p):
        if type(p) is not self.Position:
            raise TypeError("p must be of type position")
        if p.container is not self:
            raise TypeError("p belongs to another tree")
        if p.node.parent == p.node:
            raise ValueError("p is no longer valid")
        return p.node

    def add_root(self,value):
        if self._root is not None:
            raise AssertionError("root exists")
        n = Node(value, None, None)
        self._root = n
        self._size +=1
        return self._make_pos(n)

    def parent(self, p):
        n = self._validate(p)
        return self._make_pos(n.parent)

    def add_children(self,p,v):
        n = self._validate(p)
        new = Node(v, None, n)
        n.children.append(new)
        self._size += 1
        return self._make_pos(new)

    def children(self,p):
        n = self._validate(p)
        for c in n.children:
            yield self._make_pos(c)

    def descendants(self,p):
        n = self._validate(p)
        yield p
        for c in self.children(p):
            for other in self.descendants(c):
                yield other

    def num_children(self,p):
        n = self._validete(p)
        return len(n.children)

    def __len__(self):
        return self._size

    def root(self):
        return self._make_pos(self._root)

def compute_depth(n, d):
    print(f"node = {n.value}; depth={d}")
    for c in n.children:
        compute_depth(c, d+1)

t = LinkedTree()

root = t.add_root("root")
r1 = t.add_children(root,"root1")
r2 = t.add_children(root, "root2")
t.add_children(r1, "root2/r1")
t.add_children(r1, "root2/r2")
r3 = t.add_children(r1, "root2/r3")
t.add_children(r3, "root2/r3/r1")
t.add_children(r3, "root2/r3/r2")


for p in t.descendants(t.root()):
    print(p.element())

compute_depth(t.root().node, 0)
