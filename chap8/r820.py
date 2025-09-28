"""
Draw a binary tree T that simultaneously satisfies the following:
• Each internal node of T stores a single character.
• A preorder traversal of T yields EXAMFUN.
• An inorder traversal of T yields MAFXUEN.
"""

from abc import ABC, abstractmethod
class Tree(ABC):
    def preorder(self, p, action):
        action(p)
        for c in self.children(p):
            self.preorder(c,action)
    def preorder_iter(self):
        def _iter(self,p):
            yield p
            for c in self.children(p):
                for child in _iter(self,c):
                    yield child
        return _iter(self, self.root())
    @abstractmethod
    def children(self,p):
        """Returns an iterator of p's children"""
    @abstractmethod
    def root(self):
        """Returns the root of the tree"""

class BinaryTree(Tree):

    @abstractmethod
    def left(self,p):
        """returns the left node of position p"""

    @abstractmethod
    def right(self,p):
        """returns the left node of position p"""

    def inorder(self, p, action):
        if self.left(p) is not None:
            self.inorder(self.left(p), action)
        action(p)
        if self.right(p) is not None:
            self.inorder(self.right(p), action)

    def inorder_iter(self):
        def _iter(self,p):
            if self.left(p) is not None:
                for left in _iter(self,self.left(p)):
                    yield left
            yield p
            if self.right(p) is not None:
                for right in _iter(self,self.right(p)):
                    yield right

        return _iter(self,self.root())

class BinaryTreeImpl(BinaryTree):

    class Node:
        def __init__(self, left,right,parent,value):
            self.left = left
            self.right = right
            self.parent = parent
            self.value = value

    class Position:
        def __init__(self, container,node):
            self._container = container
            self._node = node

        def element(self):
            return self._node.value

    def _make_position(self,n):
        if n is not None:
            return self.Position(self,n)
        return None
    def __init__(self):
        self._root = None
        self._size = 0

    def add_root(self,v):
        assert self._root is None
        self._root = self.Node(None,None,None,v)
        self._size +=1
        return self._make_position(self._root)

    def add_left(self,p,v):
        n = self._validate(p)
        n.left = self.Node(None,None,n,v)
        self._size +=1
        return self._make_position(n.left)

    def add_right(self,p,v):
        n = self._validate(p)
        n.right = self.Node(None,None,n,v)
        self._size +=1
        return self._make_position(n.right)

    def root(self):
        return self._make_position(self._root)

    def left(self,p):
        n = self._validate(p)
        return self._make_position(n.left)

    def right(self,p):
        n = self._validate(p)
        return self._make_position(n.right)

    def _validate(self,p):
        if type(p) is not self.Position:
            raise TypeError("p must be of type Position")
        if not (p._container is self):
            raise ValueError("p does not belong to this tree")
        if p._node is p._node.parent:
            raise ValueError("p is no longer valid")
        return p._node

    def children(self,p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


t = BinaryTreeImpl()
root = t.add_root("E")
l = t.add_left(root,"X")
r = t.add_right(root,"N")
ll = t.add_left(l,"A")
lr = t.add_right(l,"U")
lll = t.add_left(ll,"M")
llr = t.add_right(ll,"F")
#rr = t.add_right(r,"cc")

print("preorder:")
t.preorder(t.root(),lambda p: print(p.element(), end=""))
print()
print("inorder:")
t.inorder(t.root(),lambda p: print(p.element(), end=""))
print()
print(" ".join(p.element() for p in t.preorder_iter()))
print()
print(" ".join(p.element() for p in t.inorder_iter()))

