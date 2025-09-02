"""
Give a complete implementation of the queue ADT using a singly linked
list that includes a header sentinel
"""
from typing import Any

class Empty(Exception):
    pass

class LinkedListQueue:

    class _Node:
        def __init__(self, next_node,value):
            self.next = next_node
            self.value = value

    def __init__(self):
        self._tail = self._Node(None,None)
        self._head = self._Node(self._tail,None)
        self._size = 0

    def enqueue(self,e):
        newest = self._Node(None,e)
        self._tail.next = newest
        self._tail = newest
        if self._size == 0:
            self._head = newest
        self._size +=1

    def dequeue(self) -> Any:
        if self.is_empty():
            raise Empty("Queue is empty")
        value = self._head.value
        self._head = self._head.next
        self._size -=1
        return value

    def first(self) -> Any:
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._head.value

    def is_empty(self) -> bool:
        return self._size==0


q = LinkedListQueue()
q.enqueue(1)
assert q.dequeue() == 1
q.enqueue(2)
q.enqueue(3)
assert q.dequeue() == 2
assert q.dequeue() == 3
# q.dequeue() # Should raise empty
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
assert q.first() == 10
assert q.dequeue() == 10
assert q.dequeue() == 20
assert q.dequeue() == 30
