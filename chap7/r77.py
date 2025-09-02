"""
Our CircularQueue class of Section 7.2.2 provides a rotate( ) method that
has semantics equivalent to Q.enqueue(Q.dequeue( )), for a nonempty
queue. Implement such a method for the LinkedQueue class of Sec-
tion 7.1.2 without the creation of any new nodes.
"""
class Empty(Exception):
    pass

class LinkedQueue:
    class _Node:
        def __init__(self, element,next_element):
            self.elem = element
            self.next = next_element

    def __init__(self):
        self._size = 0
        self._head = None
        self._tail = None

    @property
    def is_empty(self):
        return self.size() ==0

    def enqueue(self,elem):
        newest = self._Node(elem,None)
        if self.is_empty:
            self._head = newest
        else:
            self._tail.next = newest
        self._tail = newest
        self._size+=1

    def dequeue(self):
        if self.is_empty:
            raise Empty("Queue is empty")
        e = self._head.elem
        self._head = self._head.next
        self._size-=1
        if self.is_empty:
            self.tail = None
        return e

    def size(self):
        return self._size

    def __len__(self):
        return self.size()

    def rotate(self):
        if self.size()<=1:
            return
        self._tail = self._head
        self._head = self._head.next


q = LinkedQueue()
q.enqueue(1)
print(q.dequeue())
q.enqueue(2)
print(q.dequeue())
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.rotate()
print(q.dequeue())  #should print 4

