"""
Describe how to clone a LinkedBinaryTree instance representing a proper
binary tree, with use of the attach method.

Answer:


I will create a function that clones an instance of
LinkedBinaryTree.
This function will take a tree instance and return
a new instance of tree with nodes holding the same
values, but having completely different references.

The function will create a tree, create two subtrees
from the node.left and node.right and attach them to
tree, and return the tree.
For the base case, that tree is empty, it will simply
attach an empty tree.


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
            return f"Value={self.value}"

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
            return "(Position): " + str(self.node)

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


    def clone(self):
        return self._clone(self)

    def _clone(self,t):
        tree = LinkedBinaryTree()
        if not t.is_empty():
            tree.add_root(t.root().element())
            #tree._root = self.Node(None,None,None, t.root().element())
            left_subtree = LinkedBinaryTree()
            left_subtree._root = t._root.left
            left_subtree._size = 1 if t._root.left is not None else 0

            right_subtree = LinkedBinaryTree()
            right_subtree._root = t._root.right
            right_subtree._size = 1 if t._root.right is not None else 0

            tree._attach(tree.root(),self._clone(left_subtree), self._clone(right_subtree))
        return tree

    def _attach(self,p,t1,t2):
        n = self._validate(p)
        assert self.is_leaf(p), "p is a not a leaf position"
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            n.left = t1._root
            t1._root.parent = n
            t1._root =None
            t1._size=0
        if not t2.is_empty():
            n.right = t2._root
            t2._root.parent = n
            t2._root =None
            t2._size=0

tree = LinkedBinaryTree()
root =tree.add_root("root")
l = tree.add_left(root,"left")
r = tree.add_right(root,"right")
ll = tree.add_left(l,"lleft")
lr = tree.add_right(l,"lright")

lll = tree.add_left(ll,"lll")
llr = tree.add_right(ll,"llr")

newTree = tree.clone()
for e in tree.traverse(root):
    print(e.element())

print()
for e in newTree.traverse(newTree.root()):
    print(e.element())

for e1,e2 in zip(tree.traverse(tree.root()), newTree.traverse(newTree.root())):
    print("e1 is e2?", end="\t")
    print(e1.node is e2.node)

for e1,e2 in zip(tree.traverse(tree.root()), newTree.traverse(newTree.root())):
    print("v1 == v2?", end="\t")
    print(e1.node.value == e2.node.value)

print(len(tree))
print(len(newTree))
