"""
Add support in LinkedBinaryTree for a method, _swap(p,q), that has the
effect of restructuring the tree so that the node referenced by p takes the
place of the node referenced by q, and vice versa. Make sure to properly
handle the case when the nodes are adjacent.
"""
from abc import ABC,abstractmethod
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


    def _swap_parent_child(self, parent,child,pos):
        assert pos == "left" or pos =="right"
        # tmp vars used for swapping
        parent_left = parent.left
        parent_right = parent.right

        parent.left = child.left
        parent.right = child.right

        if pos == "left":
            child.left = parent
            child.right = parent_right
        elif pos =="right":
            child.right == parent
            child.left = parent_left
        else:
            assert False, "Impossible Code Path"

        if parent.parent.left == parent:
            parent.parent.left = child
        elif parent.parent.right == parent:
            parent.parent.right = child
        else:
            assert False, "Impossible Code Path"

        child.parent = parent.parent
        parent.parent = child


    def _is_ancenstor_of(self,p,q):
        parent = p
        while parent is not None:
            if parent == q:
                return True
            parent = self.parent(parent)
        return False


    def _swap(self,p,q):
        p_node = self._validate(p)
        q_node = self._validate(q)

        if p == q:
            return

        # Case 1: p and q are do not have ancenstor-descendant relationship
        if not (self._is_ancenstor_of(p,q) or self._is_ancenstor_of(q,p)):  # This excluded the case that either q or p is root
            # Case 1.1: Same parent
            if self.parent(p)==self.parent(q):
                if self.left(self.parent(p)) == p:
                    p_node.parent.left = q_node
                    p_node.parent.right = p_node
                elif self.right(self.parent(p)) == p:
                    p_node.parent.right = q_node
                    p_node.parent.left = q_node
                else:
                    assert False, "Impossible code path; p is neither left nor right of p's parent"
                return
            else:
                # Swap Subtrees
                if self.left(self.parent(p)) == p:
                    p_node.parent.left = q_node
                elif self.right(self.parent(p)) == p:
                    p_node.parent.right = q_node
                else:
                    assert False, "Impossible code path; p is neither left nor right of p's parent"

                if self.left(self.parent(q)) == q:
                    q_node.parent.left = p_node
                elif self.right(self.parent(q)) == q:
                    q_node.parent.right = p_node
                else:
                    assert False, "Impossible code path; q is neither left nor right of q's parent"

                # Swap parents
                tmp = p_node.parent
                p_node.parent = q_node.parent
                q_node.parent = tmp
        else:
            # Handle Ancenstor Descendant relationship
            # Case 2.1: q or p is root
            if q == self.root():
                self._handle_root_swap(root=q_node,child=p_node)
                return
            if p == self.root():
                self._handle_root_swap(root=p_node,child=q_node)
                return

            # Case 2.2: direct parent-child
            if self.parent(q) == p:  # p is q's parent
                if self.left(self.parent(p)) == p:  # p is the left of parent
                    self._handle_parent_child(parent=p_node,child=q_node,pos="left")
                elif self.right(self.parent(p)) == p:
                    self._handle_parent_child(parent=p_node,child=q_node,pos="right")
                else:
                    assert False
                return

            if self.parent(p) == q:  # q is p's parent
                if self.left(self.parent(q)) == q:  # q is the left of parent
                    self._handle_parent_child(parent=q_node,child=p_node,pos="left")
                elif self.right(self.parent(q)) == q:
                    self._handle_parent_child(parent=q_node,child=p_node,pos="right")
                else:
                    assert False
                return

            # Case 2.3: General Case

            p_left = p_node.left
            p_right = p_node.right
            p_node.left = q_node.left
            p_node.right = q_node.right
            q_node.left = p_left
            q_node.right = p_right

            if p_node.parent.left == p_node:
                p_node.parent.left = q_node
            elif p_node.parent.right == p_node:
                p_node.parent.right = q_node

            if q_node.parent.left == q_node:
                q_node.parent.left = p_node
            elif q_node.parent.right == q_node:
                q_node.parent.right = p_node


            p_parent = p_node.parent
            p_node.parent = q_node.parent
            q_node.parent = p_parent

    def _handle_parent_child(self,parent,child,pos):
        assert pos == "left" or pos == "right"
        if pos == "left":
            parent.parent.left = child
        elif pos == "right":
            parent.parent.right = child
        child.parent = parent.parent
        parent.parent = child

        # swap references
        c_left =child.left
        c_right = child.right
        if parent.left == child:
            child.left = parent
        elif parent.right == child:
            child.right = parent
        else:
            assert False
        parent.left = c_left
        parent.right = c_right

    def _handle_root_swap(self, root,child):
        if root.left == child:
            root.parent = child

            c_left = child.left
            c_right = child.right
            child.left = root
            child.right = root.right
            root.left= c_left
            root.right = c_right

        elif root.right == child:
            root.parent = child

            c_left = child.left
            c_right = child.right
            child.right = root
            child.left = root.left
            root.left= c_left
            root.right = c_right
        else:
            root.parent = child.parent

            c_left =child.left
            c_right = child.right
            child.left = root.left
            child.right = root.right
            root.left = c_left
            root.right = c_right

            if child.parent.left == child:
                child.parent.left = root
            elif child.parent.right == child:
                child.parent.right = root
            else:
                assert False

        child.parent = None
        self._root = child




class EulerTour:

    def __init__(self, tree:BinaryTree):
        self._tree = tree

    def execute(self):
        if len(self._tree)>0:
            self._tour(self._tree.root(), 0,[])

    def _tour(self, p, d, path):
        self.pre_visit(p,d,path)
        results = [None,None]
        if self._tree.left(p) is not None:
            path.append(0)
            results[0] = self._tour(self._tree.left(p), d+1, path)
            path.pop()

        if self._tree.right(p) is not None:
            path.append(1)
            results[1] = self._tour(self._tree.right(p), d+1, path)
            path.pop()
        r = self.post_visit(p,d,path,results)
        return r

    @abstractmethod
    def pre_visit(self,p,d,path):
        ...
    @abstractmethod
    def post_visit(self,p,d,path,results):
        ...

class PrintTreeEulerTour(EulerTour):

    def pre_visit(self,p,d,path):
        pos = ""
        if path: # path is empty for root
            pos = "left " if path[-1]==0 else "right "
        print(2*d*' '+ pos + str(p.element() ))

t = LinkedBinaryTree()
r = t.add_root("root")

l = t.add_left(r,"l")
r = t.add_right(r,"r")

ll = t.add_left(l,"ll")
lr = t.add_right(l,"lr")


lll = t.add_left(ll,"lll")

printCmd = PrintTreeEulerTour(t)
printCmd.execute()
t._swap(lll,t.root())
print('After swap lll, root')
printCmd.execute()
#print('After swap ll, l')
#t.swap(ll,l)

#printCmd.execute()
