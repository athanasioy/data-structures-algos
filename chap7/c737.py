"""
Implement a function that accepts a PositionalList L of n integers sorted
in nondecreasing order, and another value V, and determines in O(n) time
if there are two elements of L that sum precisely toV. The function should
return a pair of positions of such elements, if found, or None otherwise.
"""

class _Node:
    def __init__(self, previous_node,next_node,element):
        self.previous = previous_node
        self.next = next_node
        self.element = element

class _DoublyLinkedList:


    def __init__(self):
        self._header = _Node(None,None,None)
        self._trailer = _Node(None,None,None)
        self._header.next = self._trailer
        self._trailer.previous = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self)==0

    def _insert_between(self,e,n1,n2):
        newest = _Node(n1,n2,e)
        n1.next = newest
        n2.previous = newest
        self._size +=1
        return newest


    def _delete_node(self, node):
        previous = node.previous
        next_ = node.next
        previous.next = next_
        next_.previous = previous
        e = node.element
        node.next = node.previous = node.element = None
        self._size -=1
        return e


class PositionalList(_DoublyLinkedList):

    class Position:
        def __init__(self, container,node):
            self._container = container
            self._node = node
        def element(self):
            return self._node.element

        def __eq__(self,other):
            return type(other) is type(self) and other is self._node
        def __ne__(self,other):
            return not (self == other)

    def _validate(self,p:Position):
        if not isinstance(p,self.Position):
            raise TypeError("p must be of type position")
        if not p._container is self:
            raise ValueError("P does not belong to this List")
        if p._node.next is None:
            raise ValueError("P is no longer valid")
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        return self.Position(self, node)

    def first(self)-> Position:
        return self._make_position(self._header.next)

    def last(self) -> Position:
        return self._make_position(self._trailer.previous)

    def before(self,p):
        node = self._validate(p)
        return self._make_position(node.previous)

    def after(self,p):
        node = self._validate(p)
        return self._make_position(node.next)

    def add_first(self,e):
        node = self._insert_between(e, self._header, self._header.next)
        return self._make_position(node)

    def add_last(self,e):
        node = self._insert_between(e, self._trailer.previous, self._trailer)
        return self._make_position(node)

    def add_before(self,e,p):
        node = self._validate(p)
        newest = self._insert_between(e,node.previous,node)
        return self._make_position(newest)

    def add_after(self,e,p):
        node = self._validate(p)
        newest = self._insert_between(e,node,node.next)
        return self._make_position(newest)

    def replace(self,e,p):
        node = self._validate(p)
        old_value = node._element
        node._element = e
        return old_value

    def delete(self,p):
        node = self._validate(p)
        return self._delete_node(node)

    def __iter__(self):
        next_pos = self.first()
        while next_pos is not None:
            e = next_pos.element()
            yield e
            next_pos = self.after(next_pos)

    def find(self,e):
        next_pos = self.first()
        while next_pos is not None:
            elem = next_pos.element()
            if elem == e:
                return next_pos
            next_pos = self.after(next_pos)

def find_indices_of_sum(P, V):
    first = P.first()
    last = P.last()
    smallest_sum = first.element() + P.after(first).element()
    if smallest_sum > V:
        return None, None

    largest_sum = last.element() + P.before(last).element()
    if largest_sum  < V:
        return None, None

    S = first.element() + last.element()

    while S != V and first._node is not last._node:
        # if the sum is greater
        # reduce sum by moving a step back
        if S>V:
            last = P.before(last)
        else:
            first = P.after(first)
        S = first.element() + last.element()
        print(S)
    if S==V:
        return first, last
    else:
        return None, None



P = PositionalList()
P.add_first(1)
P.add_last(1)
P.add_last(3)
P.add_last(10)
P.add_last(11)
P.add_last(20)
P.add_last(22)



for e in P:
    print(e)

print("indices for V=13")
idx1, idx2 = find_indices_of_sum(P,13)
if idx1 is not None:
    print(idx1.element())
    print(idx2.element())

print("indices for V=14")
idx1, idx2 = find_indices_of_sum(P,14)
if idx1 is not None:
    print(idx1.element())
    print(idx2.element())

print("indices for V=15")
idx1, idx2 = find_indices_of_sum(P,15)
if idx1 is not None:
    print(idx1.element())
    print(idx2.element())

print("indices for V=2")
idx1, idx2 = find_indices_of_sum(P,2)
if idx1 is not None:
    print(idx1.element())
    print(idx2.element())
