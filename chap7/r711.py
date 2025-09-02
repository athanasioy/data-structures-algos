"""
Implement a function, with calling syntax max(L), that returns the max-
imum element from a PositionalList instance L containing comparable
elements.
"""

class _DoublyLinkedList:
    pass

class PositionalList(_DoublyLinkedList):

    class Position:
        pass


    def first(self) -> Position:
        pass

    def last(self) -> Position:
        pass

    def before(self,p) -> Position:
        pass

    def after(self,p) -> Position:
        pass

    def add_first(self,e) -> Position:
        pass

    def add_last(self,e) -> Position:
        pass

    def add_before(self,p,e) -> Position:
        pass

    def add_after(self,p,e) -> Position:
        pass

    def replace(self,p,e) -> Position:
        pass

    def delete(self,p) -> Position:
        pass

def max(L):
    m = None
    for e in L:
        if m is None or e>m:
            m=e
    return m
