"""
Design a forward list ADT that abstracts the operations on a singly linked
list, much as the positional list ADT abstracts the use of a doubly linked
list. Implement a ForwardList class that supports such an ADT.
"""

class Node:
    def __init__(self, n,v):
        self.next = n
        self.value = v

class Position:

    def __init__(self,container,node):
        self._container = container
        self._node = node

    def element(self):
        return self._node.value



class ForwardList:

    def __init__(self):
        self._head = Node(None,None)

    def add_first(self,e) ->Position:
        newest = Node(self._head.next,e)
        self._head.next = newest
        return self._make_position(newest)

    def after(self,p) -> Position:
        node = self._validate(p)
        return self._make_position(node.next)

    def add_after(self,p,e) -> Position:
        node = self._validate(p)
        newest = Node(node.next,e)
        node.next = newest
        return self._make_position(newest)

    def first(self):
        return self._make_position(self._head.next)

    def delete(self,p):
        raise NotImplemented("This class does not support deletions.")

    def __iter__(self):
        cursor = self._head.next
        while cursor:
            yield cursor.value
            cursor = cursor.next

    def _validate(self,p) -> Node:
        if p._container is not self:
            raise ValueError("p does not belong in this list")
        if not isinstance(p, Position):
            raise TypeError("p must be of type Position")
        return p._node

    def _make_position(self,n) -> Position:
        if n is self._head:
            return None
        return Position(self, n)



fl = ForwardList()
p = fl.add_first(1)
p1 =fl.add_after(p,2)
p2 = fl.add_after(p,3)
p3 = fl.add_after(p2,4)

for e in fl:
    print(e)
print("End of loop")
print(p3.element())
pp = fl.after(p)
print(pp.element())
