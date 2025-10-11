"""
We can simplify parts of our LinkedBinaryTree implementation if we
make use of of a single sentinel node, referenced as the sentinel member
of the tree instance, such that the sentinel is the parent of the real root of
the tree, and the root is referenced as the left child of the sentinel.

Furthermore, the sentinel will take the place of None as the value of the left
or right member for a node without such a child.

Give a new implementation of the update methods delete and attach, assuming such a
representation
"""

from abc import ABC,abstractmethod
class Tree(ABC):

    class Position(ABC):
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
        def __init__(self, left=None, right=None,parent=None,value=None):
            self.left = left
            self.right = right
            self.parent = parent
            self.value = value
        def __repr__(self):
            return str(self.value)

    class Position(Tree.Position):
        def __init__(self, container,node):
            self.container = container
            self.node = node

        def __eq__(self,other):
            if not isinstance(other,self):
                return False
            return other.node is self.node
        def element(self):
            return self.node.value

    def _validate(self,p):
        if not isinstance(p,self.Position):
            raise TypeError("p must be of type position")
        if not p.container is self:
            raise ValueError("p does not belong to this container")
        if p.node.parent == p.node:  #Convention for depricated nodes
            raise ValueError("this position is no longer valid")
        return p.node
    def _make_pos(self,n):
        if n is not None:
            return self.Position(self,n) if n not in self._sentinel_list else None

    def __init__(self):
        self._sentinel = self.Node()
        self._root = self._sentinel
        self._size = 0
        self._sentinel_list = [self._sentinel] # necessary when combining trees

    def __len__(self):
        return self._size

    def root(self):
        return self._make_pos(self._sentinel.left)

    def add_root(self, value):
        assert self._sentinel.left is None, "Root Exists"
        new = self.Node(parent=self._sentinel,value=value)
        self._root = new
        self._sentinel.left = new
        new.right = self._sentinel
        new.left = self._sentinel
        self._size +=1
        return self._make_pos(new)

    def add_left(self,p,v):
        node = self._validate(p)
        new = self.Node(self._sentinel, self._sentinel,node,v)
        node.left = new
        self._size +=1
        return self._make_pos(new)

    def add_right(self,p,v):
        node = self._validate(p)
        new = self.Node(self._sentinel, self._sentinel,node,v)
        node.right=new
        self._size +=1
        return self._make_pos(new)

    def left(self,p):
        node = self._validate(p)
        return self._make_pos(node.left)

    def right(self,p):
        node = self._validate(p)
        return self._make_pos(node.right)

    def parent(self,p):
        node = self._validate(p)
        return self._make_pos(node.parent)

    def sibling(self,p):
        node = self._validate(p)
        if node.parent.left == node:
            return self._make_pos(node.right)
        if node.parent.right == node:
            return self._make_pos(node.left)
        assert False

    def delete(self,p):
        """
        TODO
        Deletes the node at position p, and replaces it which its child, if any.

        Returns the element stored at position p.
        Raises ValueError if p has two children or p is invalid.
        """
        node = self._validate(p)  # check if p is valid
        assert self.num_children(p) != 2, "p has to 2 children"
        child = node.left if node.left != self._sentinel else node.right

        if child != self._sentinel:
            child.parent = node.parent

            if node.parent is self._sentinel: #root
                self._root = child
            if node.parent.left == node:
                node.parent.left = child
            elif node.parent.right ==node:
                node.parent.right = child

        node.parent = node #Depricate node
        return p

    def attach(self,p,t1,t2):
        """
        TODO
        Attaches t1 and t2 to the left and right of p.

        Raises ValueError if p is not a leaf position.
        """
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError("p is not a leaf position")
        self._size += len(t1) + len(t2)
        node.left = t1._root
        t1._root.parent = node
        t1._size=0
        node.right = t2._root
        t2._root.parent = node
        t2._size=0

        # This is necessary because we are combining
        # trees with different sentinel instances,
        # however when accessing position of the tree
        # we need a way to determine if the node
        # is an actual tree node or an empty position
        # occupied by a sentinel value. Do do that
        # we need to hold the sentinel references
        # of the merged trees.

        self._sentinel_list.append(t1._sentinel)
        self._sentinel_list.append(t2._sentinel)

    def traverse(self):
        return self._traverse(self.root())

    def _traverse(self,p):
        yield p
        for c in self.children(p):
            for other in self._traverse(c):
                yield other


t = LinkedBinaryTree()

t.add_root("root")
left=t.add_left(t.root(),"left")
right=t.add_right(t.root(),"right")

t2 = LinkedBinaryTree()
t2.add_root("t2")
t2.add_left(t2.root(), "left t2")
t2.add_right(t2.root(), "right t2")

t3 = LinkedBinaryTree()
t3.add_root("t3")
t3l = t3.add_left(t3.root(), "left t3")
t3.add_left(t3l, "Left")

t.attach(right,t2,t3)
for e in t.traverse():
    print(e.element())
t3l.container = t
t.delete(t3l)
print()
print("after delete")
print()
for e in t.traverse():
    print(e.element())

