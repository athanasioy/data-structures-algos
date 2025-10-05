"""
Add support in LinkedBinaryTree for a method, delete _subtree(p), that
removes the entire subtree rooted at position p, making sure to maintain
the count on the size of the tree. What is the running time of your implementation?

Answer:

The running time of the implementation is O(N) worst case,
because in order to update the size of the tree, we need
to count (visit) each child of position. At worst case,
position P is root, and we visit all nodes.
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

    def is_leaf(self,p):
        return self.num_children(p)==0

    def is_empty(self,p):
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

class BinaryTree(Tree):

    @abstractmethod
    def left(self,p):
        ...

    @abstractmethod
    def right(self,p):
        ...


    @abstractmethod
    def sibling(self,p):
        ...

    def children(self,p):
        left = self.left(p)
        right = self.right(p)
        if left:
            yield left
        if right:
            yield right

    def num_children(self,p):
        left = self.left(p)
        right = self.right(p)
        cnt = 0
        if left:
            cnt +=1
        if right:
            cnt +=1
        return cnt

class LinkedBinaryTree(BinaryTree):

    class Node:
        def __init__(self, left,right,parent,value):
            self.left = left
            self.right = right
            self.parent =parent
            self.value = value

        def __repr__(self):
            return f"Value={self.value}, left=[{self.left}], right=[{self.right}]"

    class Position(Tree.Position):
        def __init__(self, container, node):
            self.container = container
            self.node = node

        def element(self):
            return self.node.value

        def __eq__(self,other):
            if not isinstance(other, type(self)):
                return False
            return self.node is other.node

        def __repr__(self):
            return str(self.node)

    def _make_position(self,node):
        return self.Position(self, node) if node else None

    def _validate(self,p):
        if not isinstance(p,self.Position):
            raise TypeError("p must be of type position")
        if p.container is not self:
            raise ValueError("p does not belong to this tree")
        if p.node.parent is p.node: #convention for deleted nodes
            raise ValueError("p is no longer valid")
        return p.node

    def __init__(self):
        self._root = None
        self._size = 0

    def root(self):
        return self._make_position(self._root)

    def parent(self,p):
        node = self._validate(p)
        return self._make_position(node.parent)

    def __len__(self):
        return self._size

    def left(self,p):
        node = self._validate(p)
        return self._make_position(node.left)

    def right(self,p):
        node = self._validate(p)
        return self._make_position(node.right)

    def sibling(self,p):
        node = self._validate(p)
        parent = self.parent(p)
        if parent is None:
            return None
        if self.left(parent) == p:
            return self.right(parent)
        if self.right(parent) == p:
            return self.left(parent)

    def add_root(self,v):
        assert self._root is None
        self._root = self.Node(None,None,None,v)
        self._size +=1
        return self._make_position(self._root)

    def add_left(self,p, v):
        node = self._validate(p)
        new = self.Node(None,None,node,v)
        node.left = new
        self._size +=1
        return self._make_position(new)

    def add_right(self,p, v):
        node = self._validate(p)
        new = self.Node(None,None,node,v)
        node.right = new
        self._size +=1
        return self._make_position(new)

    def delete_subtree(self,p):
        cnt = 0
        def count_children(self,p):
            nonlocal cnt
            cnt+=1
            for c in self.children(p):
                count_children(self,c)
        if self.root() == p:
            self._root = None
            self._size = 0
            return

        node = self._validate(p)
        parent = self.parent(p)
        count_children(self,p)

        if self.left(parent) == p:
            parent.node.left = None
        if self.right(parent) == p:
            parent.node.right = None

        node.parent = node
        node.left=None
        node.right=None

        self._size -= cnt
        return p

    def traverse(self,p):
        yield p
        for c in self.children(p):
            for other in self.traverse(c):
                yield other


t = LinkedBinaryTree()
r = t.add_root(1)

l = t.add_left(r,10)
r = t.add_right(r,10)

ll = t.add_left(l,59)
lr = t.add_right(l,59)

print(t.root())
print(len(t))
print("after delete")
t.delete_subtree(r)
print(t.root())
print(len(t))
print("delete root")
t.delete_subtree(t.root())
print(len(t))
