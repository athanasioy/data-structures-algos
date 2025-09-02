"""
Update the PositionalList class to support an additional method find(e),
which returns the position of the (first occurrence of ) element e in the list
(or None if not found).
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
            self._node.element

        def __eq__(self,other):
            return type(other) is type(self) and other is self._node
        def __ne__(self,other):
            return not (self == other)

    def _validate(self,p:Position):
        if not isinstance(p,Position):
            raise TypeError("p must be of type position")
        if not p._container not self:
            raise ValueError("P does not belong to this List")
        if p.element().next is None:
            raise ValueError("P is no longer valid")
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        return Position(self, node)

    def first(self)-> Position:
        return self._make_position(self._header.next)

    def last(self) -> Position:
        return self._make_position(self._trailer.previous)

    def before(self,p):
        self._validate(p)
        return self._make_position(p.previous)

    def after(self,p):
        self._validate(p)
        return self._make_position(p.next)

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
