"""
Give a complete implementation of the stack ADT using a singly linked
list that includes a header sentinel.
"""

class Empty(Exception):
    pass


class LinkedListStack:

    class _Node:
        def __init__(self,  next_node, value):
            self.next = next_node
            self.value = value

    def __init__(self):
        self._head = self._Node(None,None)
        self._size = 0

    def push(self,e) -> None:
        newest = self._Node(self._head, e)
        self._head = newest
        self._size +=1

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        value = self._head.value
        self._head = self._head.next
        self._size -=1
        return value

    def is_empty(self) -> bool:
        return self.size() == 0


    def size(self)->int:
        return self._size

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._head.value


s = LinkedListStack()
s.push(1)
s.push(2)
s.push(3)
assert s.pop() == 3
assert s.pop() == 2
s.push(10)
assert s.pop() == 10
assert s.pop() == 1

s.push(1)
s.push(2)
assert s.top() == 2
assert s.size() == 2
