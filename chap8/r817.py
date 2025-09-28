"""
Show how to use the Euler tour traversal to compute the level number
f(p), as defined in Section 8.3.2, of each position in a binary tree T.

f(p)=0 if p is root
f(p)=2f(q)+1, if p is left of q
f(p)=2f(q)+2, if p is right of q
"""

class Tree:

    class Position:

        def element(self):
            raise NotImplementedError("Must be implemented by subclass")

        def __eq__(self, other):
            raise NotImplementedError("Must be implemented by subclass")
        def __ne__(self, other):
            return not self == other

    def root(self):
        raise NotImplementedError("Must be implemented by subclass")

    def parent(self,p):
        raise NotImplementedError("Must be implemented by subclass")

    def num_children(self,p):
        raise NotImplementedError("Must be implemented by subclass")

    def __len__(self):
        raise NotImplementedError("Must be implemented by subclass")

    def is_root(self,p):
        return self.root() == p

    def is_leaf(self,p):
        return self.num_children(p)==0

    def is_empty(self):
        return len(self) ==0

    def depth(self,p):
        if self.is_root(p):
            return 0
        return 1 + self.depth(self.parent(p))

    def height(self,p):
        if self.is_leaf(p):
            return 0
        return 1 + max(self.height(child) for child in self.children(p))

class BinaryTree(Tree):
    def left(self,p):
        raise NotImplementedError("Must be implemented by subclass")

    def right(self,p):
        raise NotImplementedError("Must be implemented by subclass")

    def sibling(self,p):
        parent = self.parent(p)
        if parent is None:
            return None
        if p == self.right(parent):
            return self.left(parent)
        if p == self.left(parent):
            return self.right(parent)

    def children(self,p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

class LinkedBinaryTree(BinaryTree):

    class _Node:
        def __init__(self, value, left, right, parent):
            self.value = value
            self.left = left
            self.right = right
            self.parent = parent

    class Position(Tree.Position):

        def __init__(self, node, container):
            self._node = node
            self._container = container

        def element(self):
            return self._node.value

        def __eq__(self, other):
            return  type(self) is type(other) and self._node is other._node

    def _validate(self,p):
        if type(p) is not self.Position:
            raise TypeError("p must be of type position")
        if p._container is not self:
            raise ValueError("this position does not belong to the current tree")
        if p._node.parent is p._node:
            raise ValueError("this position is no longer valid")
        return p._node

    def _make_position(self,n):
        return self.Position(n,self) if n is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def root(self):
        return self._make_position(self._root)

    def __len__(self):
        return self._size

    def parent(self,p):
        n = self._validate(p)
        return self._make_position(n.parent)

    def left(self,p):
        n = self._validate(p)
        return self._make_position(n.left)

    def right(self,p):
        n = self._validate(p)
        return self._make_position(n.right)

    def num_children(self,p):
        n = self._validate(p)
        cnt = 0
        if n.left is not None:
            cnt+=1
        if n.right is not None:
            cnt+=1
        return cnt

    def _add_root(self,v):
        if self.root() is not None: raise ValueError("Root Exists")

        n = self._Node(v,None,None,None)
        self._root = n
        self._size = 1
        return self._make_position(self._root)

    def _add_left(self,p,v):
        n = self._validate(p)
        if n.left is not None: raise ValueError("Left exists")
        new = self._Node(v,None,None,parent=n)
        n.left = new
        self._size +=1
        return self._make_position(new)

    def _add_right(self,p,v):
        n = self._validate(p)
        if n.right is not None: raise ValueError("Right exists")
        new = self._Node(v,None,None,parent=n)
        n.right = new
        self._size +=1
        return self._make_position(new)

    def _replace(self,p,v):
        n = self._validate(p)
        old = n.value
        n.value = v
        return old

    def _delete(self,p):
        n = self._validate(p)
        if self.num_children(p) == 2: raise ValueError("Node has two children")
        child = n.left if n.left else n.right 

        if p is self.root():
            self.root = child
        else:
            parent = n.parent
            if parent.left is n:
                parent.left = child
            else:
                parent.right = child
        n.parent = n
        self.size -=1
        return n.value

class EulerTour:

    def __init__(self, tree):
        self._tree = tree


    def execute(self):
        if len(self._tree)>0:
            return self._tour(self._tree.root(),0,[] )


    def _tour(self, p, d, path):
        self._previsit_hook(p,d,path)
        results = []
        path.append(0)
        for c in self._tree.children(p):
            results.append(self._tour(c,d+1,path))
            path[-1] +=1
        path.pop()
        answer = self._postvisit_hook(p,d,path, results)
        return answer

    def _previsit_hook(self,p,d,path):
        pass

    def _postvisit_hook(self,p,d,path,results):
        pass

class BinaryTreeEulerTour(EulerTour):

    def _tour(self, p, d, path):
        self._previsit_hook(p,d,path)
        results = [None, None]
        if self._tree.left(p) is not None:
            path.append(0)
            left = self._tree.left(p)
            results[0]=self._tour(left, d+1, path)
            path.pop()
        self._hook_invisit(p,d,path)
        if self._tree.right(p) is not None:
            path.append(1)
            right = self._tree.right(p)
            results[1]=self._tour(right, d+1, path)
            path.pop()

        answer = self._postvisit_hook(p,d,path,results)
        return answer
    def _hook_invisit(self,p,d,path):
        pass

class LevelNumberEulerTour(BinaryTreeEulerTour):
    def _previsit_hook(self,p,d,path):
        level_number = 0
        for i in path:
            if i == 0: #left
                level_number = 2*level_number + 1
            elif i == 1 : #right
                level_number = 2*level_number + 2
        print(f"{p.element()}:{level_number}")

tree = LinkedBinaryTree()
root = tree._add_root(1)
tree._add_left(root,2)
r=tree._add_right(root,3)
tree._add_left(r,10)
tree._add_right(r,30)


tour = LevelNumberEulerTour(tree)
tour.execute()
