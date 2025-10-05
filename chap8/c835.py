"""

Two ordered trees T and T are said to be isomorphic if one of the following holds:
• Both T and T are empty.
• The roots of T and T have the same number k ≥ 0 of subtrees, and
    the i th such subtree of T is isomorphic to the i
    th such subtree of T for i = 1,...,k.

Design an algorithm that tests whether two given ordered trees are isomorphic. What is the running time of your algorithm?

Answer:
The algorthim is O(N), since every node is visted exactly once
"""

class OrderedNode:
    def __init__(self, children, value):
        self.children = children if children else []
        self.value = value
        self._size = len(self.children)

    def append_child(self,child):
        assert type(child) is type(self)
        self.children.append(child)
        self._size +=1

    def insert_child_at(self,child,pos):
        assert type(child) is type(self)
        self.children.insert(pos, child)
        self._size +=1

    def subtrees(self):
        return self.children

    def __repr__(self):
        return f"Value={self.value}, Children=({self.children})"


    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self)==0

class OrderedTree:

    def __init__(self):
        self._root =None

    def set_root(self, root:OrderedNode):
        assert self._root is None
        self._root = root

    def root(self):
        return self._root


def is_isomorphic(tree1, tree2):
    if tree1.is_empty() and tree2.is_empty():
        return True
    if len(tree1.subtrees()) != len(tree2.subtrees()):
        return False
    for i in range(len(tree1.subtrees())):
        if not is_isomorphic(tree1.subtrees()[i], tree2.subtrees()[i]):
            return False
    return True

t1 = OrderedNode(None,1)
t1.append_child(OrderedNode(None,2))
t1.append_child(OrderedNode(None,3))
t1.append_child(OrderedNode(None,4))
t1.children[1].append_child(OrderedNode(None,5))
t1.children[1].append_child(OrderedNode(None,6))


t2 = OrderedNode(None,1)
t2.append_child(OrderedNode(None,2))
t2.append_child(OrderedNode(None,3))
t2.append_child(OrderedNode(None,4))
t2.children[1].append_child(OrderedNode(None,5))
t2.children[1].append_child(OrderedNode(None,6))

print("t1, t2?")
print(is_isomorphic(t1,t2))

t3 = OrderedNode(None,1)
t3.append_child(OrderedNode(None,2))
t3.append_child(OrderedNode(None,3))
t3.append_child(OrderedNode(None,4))

# change index from 1 to 2

t3.children[2].append_child(OrderedNode(None,5))
t3.children[2].append_child(OrderedNode(None,6))

print("t1, t3?")
print(is_isomorphic(t1,t3))
