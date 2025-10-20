"""
Give an efficient algorithm that computes and prints, for every position p
of a tree T, the element of p followed by the height of p’s subtree.
"""

from abc import ABC, abstractmethod
from typing import Self,Any
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

    def is_leaf(self,p):
        return self.num_children(p)==0

    def is_empty(self):
        return len(self) == 0

    def is_root(self,p):
        return self.root() == p

    @abstractmethod
    def root(self):
        ...

    @abstractmethod
    def parent(self,p):
        ...

    @abstractmethod
    def __len__(self):
        ...

    @abstractmethod
    def num_children(self,p):
        ...

    @abstractmethod
    def children(self,p):
        ...

    def height(self,p):
        if self.is_leaf(p):
            return 0
        return max((self.height(c) for c in self.children(p))) + 1

    def depth(self,p):
        if self.is_root(p):
            return 0
        return self.depth(self.parent(p)) + 1



class LinkedTree(Tree):

    class Node:
        def __init__(self, value:Any, parent:Self, children:list[Self]):
            self.value = value
            self.children = children if children else []
            self.parent = parent

    class Position(Tree.Position):
        def __init__(self, container, node):
            self.container = container
            self.node = node

        def __eq__(self,other):
            if type(other) is not type(self):
                return False
            return self.node is other.node
        def element(self):
            return self.node.value


    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def _validate(self,p):
        if not isinstance(p, self.Position):
            raise TypeError("p must be of type position")
        if p.container is not self:
            raise ValueError("p does not belong to this tree")
        if p.node == p.node.parent:
            raise ValueError("p is no longer value")
        return p.node

    def _make_position(self,n):
        if n is not None:
            return self.Position(self,n)
        return None
    def children(self, p):
        node = self._validate(p)
        if node.children is not None:
            for c in node.children:
                yield self._make_position(c)

    def num_children(self,p):
        node = self._validate(p)
        return len(node.children)

    def parent(self,p):
        node = self._validate(p)
        return self._make_position(node.parent)

    def root(self):
        return self._make_position(self._root)

    def add_root(self,v):
        assert not self._root, "root exists"
        n = self.Node(v,parent=None,children=None)
        self._root =n
        self._size +=1
        return self._make_position(n)

    def add_children(self,p,v):
        node = self._validate(p)
        new = self.Node(v,node,children=None)
        node.children.append(new)
        self._size +=1
        return self._make_position(new)

    def descendants(self,p):
        n = self._validate(p)
        yield p
        for c in self.children(p):
            for other in self.descendants(c):
                yield other


def th(n,d):
    if n.children is None or len(n.children)==0:
        print(f"{n.value} at depth={d}: height={0}")
        return 0

    heights = []
    for c in n.children:
        heights.append(th(c,d+1))
    sbh = max(heights)
    print(f"{n.value} at depth={d}: height={sbh}")
    return sbh + 1

t = LinkedTree()
root = t.add_root("root")
for i in range(4):
    c = t.add_children(root,i)

for z in range(10,15):
    z = t.add_children(c,z)

a = t.add_children(z,"123")
t.add_children(z,"end")
t.add_children(a,"someday")

for elem in t.descendants(t.root()):
    print(elem.element())

print()
print()
th(t._root,0)
