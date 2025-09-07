"""
Exercise P-6.35 describes a LeakyStack abstraction. Implement that ADT
using a singly linked list for storage.
"""


class LeakyStack:
    class _Node:
        def __init__(self,  n,v):
            self.next = n
            self.value = v

    def __init__(self,maxlen):
        self._maxlen=maxlen
        self._head=None
        self._size=0

    def push(self,e):
        newest = self._Node(self._head,e)
        self._head = newest
        if self._size > self._maxlen:
            self._leak()
        else:
            self._size +=1

    def pop(self):
        if self.is_empty():
            return
        a = self._head.value
        self._head = self._head.next
        self._size -=1
        return a

    def is_empty(self):
        return self._size == 0

    def top(self):
        return self._head.value

    def _leak(self):
        cursor = self._head
        for _ in range(self._maxlen-1):
            cursor = cursor.next
        cursor.next = None

    def __iter__(self):
        cursor = self._head
        while cursor:
            yield cursor.value
            cursor = cursor.next



s = LeakyStack(4)

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
for e in s:
    print(e)

s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
print("after pops")
for e in s:
    print(e)


