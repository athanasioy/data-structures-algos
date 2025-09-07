"""
There is a simple, but inefficient, algorithm, called bubble-sort, for sorting
a list L of n comparable elements. This algorithm scans the list n−1 times,
where, in each scan, the algorithm compares the current element with the
next one and swaps them if they are out of order. Implement a bubble sort
function that takes a positional list L as a parameter. What is the running
time of this algorithm, assuming the positional list is implemented with a
doubly linked list?
"""

class _Node:
    def __init__(self, previous_node,next_node,element):
        self.previous = previous_node
        self.next = next_node
        self.element = element

    def __repr__(self):
        return f"Value={self.element}"

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

        def __repr__(self):
            return str(self._node)

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

    def swap(self,p1,p2):
        n1 = self._validate(p1)
        n2 = self._validate(p2)
        if n1 is n2:
            return

        n1_prev = n1.previous
        n1_next = n1.next
        n2_next = n2.next
        n2_prev = n2.previous

        if n1.next is n2:
            n2.next = n1
            n1.previous = n2
            n2.previous = n1_prev
            n1_prev.next = n2
            n1.next = n2_next
            n2_next.previous = n1
        elif n2.next is n1:
            n1.next = n2
            n2.previous = n1
            n1.previous = n2_prev
            n2_prev.next = n1
            n2.next = n1_next
            n1_next.previous = n2
        else:
            n1.next = n2_next
            n2_next.previous = n1
            n1.previous = n2_prev
            n2_prev.next = n1

            n2.next = n1_next
            n1_next.previous= n2
            n2.previous = n1_prev
            n1_prev.next = n2



def bubble_sort(P):
    first = P.first()
    end = P.last()
    guard = end
    for _ in range(len(P)-1):
        while first._node != P.last()._node:
            if first.element() > P.after(first).element():
                P.swap(first, P.after(first))
            else:
                first = P.after(first)
        first = P.first()


p = PositionalList()
n1=p.add_first(1)
p.add_first(1000)
n2=p.add_last(2)
n3=p.add_last(3)
n4=p.add_last(4)
n4=p.add_last(-1)
n4=p.add_last(-100)
n4=p.add_last(50)


for e in p:
    print(e)

print("swap n2,n3")
print("----")
print(n2.element())
print(n3.element())
print("----")
p.swap(n2,n3)
for e in p:
    print(e)

bubble_sort(p)

print("sort!")
for e in p:
    print(e)
