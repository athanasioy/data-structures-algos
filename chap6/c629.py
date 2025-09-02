"""
In certain applications of the queue ADT, it is common to repeatedly
dequeue an element, process it in some way, and then immediately en-
queue the same element. Modify the ArrayQueue implementation to in-
clude a rotate() method that has semantics identical to the combina-
tion, Q.enqueue(Q.dequeue( )). However, your implementation should
be more efficient than making two separate calls (for example, because
there is no need to modify size)
"""

class Empty(Exception):
    pass

class Queue:
    DEFAULT_CAPACITY=10

    def __init__(self, cap):
        if cap:
            self._data = [None] * cap
        else:
            self._data = [None] * Queue.DEFAULT_CAPACITY

        self._size=0
        self._front=0


    def enqueue(self, elem):
        if self._size == len(self._data):
            self._resize(len(self._data)*2)
        _next_idx = (self._front + self._size) % len(self._data)
        self._data[_next_idx] = elem
        self._size +=1

    def dequeue(self):
        if self._size ==0:
            raise Empty("queue is empty")
        e = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front +1)%len(self._data)
        self._size -=1
        return e

    def _resize(self,new_size):
        old = self._data
        new = [None]*new_size
        walk = self._front
        for i in range(self._size):
            new[i] = old[walk]
            walk = (walk + 1) % len(old)
        self._data = new
        self._front = 0

    def rotate(self):
        if self._size == len(self._data):
            self._front = (self._front+1) % len(self._data)
        else:
            old_front = self._front
            self._front = (self._front+1) % len(self._data)
            avail = (old_front+self._size) % len(self._data)
            self._data[avail] =self._data[old_front]
            self._data[old_front] = None


q = Queue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.rotate()
assert q.dequeue() == 2
assert q.dequeue() == 3
assert q.dequeue() == 1

q = Queue(10)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.rotate()
assert q.dequeue() == 2
print(q._data)
assert q.dequeue() == 3
print(q._data)
assert q.dequeue() == 4
print(q._data)
