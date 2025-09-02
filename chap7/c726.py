"""
Implement a method, concatenate(Q2) for the LinkedQueue class that
takes all elements of LinkedQueue Q2 and appends them to the end of the
original queue. The operation should run in O(1) time and should result
in Q2 being an empty queue.
"""

class LinkedQueue:

    class _Node:
        def __init__(self, next_node, value):
            self.next=next_node
            self.value=value


    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self,e):
        newest = self._Node(None, e)
        if self.is_empty():
            self._head = newest
        else:
            self._tail.next = newest
        self._tail = newest
        self._size +=1


    def dequeue(self):
        if self.is_empty():
            raise ValuError("Empty")
        val = self._head.value
        self._head = self._head.next
        self._size -=1
        if self.is_empty():
            self._head = None
        return val

    def is_empty(self):
        return self.size() ==0

    def size(self):
        return self._size


def concatenate(q1:LinkedQueue,q2:LinkedQueue):
    """ Must concatenate list in O(1) """
    if q2.is_empty():
        return

    if q1.is_empty():
        q1._head = q2._head
        q1._tail = q2._tail
        q1._size = q2._size
        return

    q1._tail.next = q2._head
    q1._tail = q2._tail
    q1._size = q1._size + q2._size

    q2._head = None
    q2._tail = None
    q2._size = 0

q = LinkedQueue()
q.enqueue(1)
assert q.dequeue()==1
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

assert q.dequeue()==1
assert q.dequeue()==2
assert q.dequeue()==3


q1 = LinkedQueue()
q2 = LinkedQueue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)

q2.enqueue(100)
q2.enqueue(200)
q2.enqueue(300)

concatenate(q1,q2)
q1.enqueue(123)
q1.enqueue("a")
while not q1.is_empty():
    print(q1.dequeue())
