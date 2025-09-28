"""
Describe, in pseudo-code, an algorithm for computing the number of descendants
of each node of a binary tree. The algorithm should be based
on the Euler tour traversal.


Answer:

postvisit_hook(node,depth,path,results):
    s = 0
    for r in result
        if r is not null # not a leaf position
            s = s + r +1 # the descendants of p are the sum of the descedant's descendants plus 1
    return s


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

    def __len__(self):
        return self._size

class BinaryEulerTour(ABC):

    def __init__(self,  tree):
        self._tree =tree


    def execute(self):
        if len(self._tree)>0:
            return self._tour(self._tree.root(), 0,[])

    def _tour(self, p, d, path):
        self.previsit(p,d,path)
        results = [None,None]
        if self._tree.left(p) is not None:
            path.append(0)
            results[0] = self._tour(self._tree.left(p), d+1,path)
            path.pop()

        if self._tree.right(p) is not None:
            path.append(1)
            results[1] = self._tour(self._tree.right(p), d+1,path)
            path.pop()

        answer = self.postvisit(p,d,path,results)
        return answer

    @abstractmethod
    def previsit(self,p,d,path):
        ...

    @abstractmethod
    def postvisit(self,p,d,path,result):
        ...


class DescendantsEulerTour(BinaryEulerTour):

    def previsit(self,p,d,path):
        pass


    def postvisit(self,p,d,path,results):
        s = 0
        for r in results:
            if r is not None:
                s +=r + 1
        print(f"{p.element()} at path {path} has {s} descendants")
        return s


t = BinaryTreeImpl()
root = t.add_root(1)
l = t.add_left(root,2)
r = t.add_right(root,3)
ll = t.add_left(l,4)
rr = t.add_right(r,5)
lll = t.add_left(ll,6)
rrr = t.add_right(rr,7)


tour = DescendantsEulerTour(t)
tour.execute()
