"""
Give a simple adapter that implements our queue ADT while using a
collections.deque instance for storage.
"""
from collections import deque

class DequeQueue:
    def __init__(self,capacity=128):
        self._queue = deque(maxlen=capacity)

    def enqueue(self,elem):
        self._queue.append(elem)

    def dequeue(self):
        return self._queue.popleft()

    def first(self):
        return self._queue[0]

    @property
    def is_empty(self):
        return len(self)==0

    def __len__(self):
        return len(self._queue)


q = DequeQueue()
print(len(q))
print(q.is_empty)
q.enqueue(1)
print(len(q))
print(q.is_empty)
print(q.first())
q.enqueue(10)
print(len(q))
print(q.is_empty)
print(q.first())
q.enqueue(100)
f = q.dequeue()
print("f==1?", end='\t')
print(f==1)
f = q.dequeue()
print("f==10?", end='\t')
print(f==10)
f = q.dequeue()
print("f==100?", end='\t')
print(f==100)
print(len(q))
print(q.is_empty)
