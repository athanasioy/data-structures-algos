"""
Modify the DoublyLinkedBase class to include a reverse
method that reverses the order of the list,
yet without creating or destroying any nodes.


Answer:
I need to swap the next and previous
pointers for each node.

I need to update the sentinels,
self._header and self._trailer
next and previous nodes respectively.

H <-> A <-> B <-> C <-> D <-> T
H <-> D <-> C <-> B <-> A <-> T

H -> A
D <- T

B <- A -> H
C <- B -> A
D <- C -> B
T <- D -> C

# head next points to old tail
H -> D
# old tail previous to head
H <- D

# old head next points to trailer
# tralier previous points to old head
A -> T
A <- T
"""


class _DoublyLinkedBase:

    class _Node:
        def __init__(self, value,prev_node, next_node):
            self.value = value
            self.previous = prev_node
            self.next = next_node

    def __init__(self):
        self._head = self._Node(None,None,None)
        self._trailer = self._Node(None,None,None)
        self._head.next = self._trailer
        self._trailer.previous = self._head
        self._size = 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e,predecessor, successor)
        predecessor.next = newest
        successor.previous = newest
        self._size +=1
        return newest

    def _delete(self,n):
        prev = n.prev
        next_ = n.next

        prev.next = next_
        next_.prev = prev
        self._size -=1
        n.prev = n.next = None

        return n.value

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self)==0

    def __iter__(self):
        cursor = self._head.next
        while cursor is not self._trailer:
            yield cursor.value
            cursor = cursor.next

    def reverse(self):
        if len(self)<=1:
            return
        first = self._head.next
        last = self._trailer.previous
        next_ = first
        while next_ is not self._trailer:
            # next_.prev,next_.next = next_.next, next_.prev
            # swap next with previous and continue

            tmp = next_.next
            next_.next = next_.previous
            next_.previous = tmp
            next_ = tmp

        last.prev = self._head
        self._head.next = last

        first.next = self._trailer
        self._trailer.previous = first


a = _DoublyLinkedBase()
n = a._insert_between(1,a._head, a._trailer)
n2 = a._insert_between(2,n,a._trailer)
n3 = a._insert_between(3,n,n2)
n4 = a._insert_between(50,n3,n2)
print("Len=" + str(len(a)))
for e in a:
    print(e)


a.reverse()
print("after reverse")
for e in a:
    print(e)
