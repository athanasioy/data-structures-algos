""" Describe in detail an algorithm for reversing a singly linked list L using
only a constant amount of additional space and not using any recursion.

Answer:

See Code Implementation.
TODO: Add an explanation.
"""


class Node:
    def __init__(self, n,v):
        self.value =v
        self.next =n

class LinkedList:

    def __init__(self):
        self._head = None
        self._tail = None

    def add_last(self,e):
        newest = Node(None,e)
        if self._head is None:
            self._head = newest
        else:
            self._tail.next = newest
        self._tail = newest

    def first(self):
        return self._head

    def length(self):
        curr = self._head
        l = 0
        while curr:
            l+=1
            curr = curr.next
        return l

    def reverse(self):
        if self.length()<=1:
            return

        old_head = self._head

        prev = self._head
        curr = prev.next
        while curr:
            tmp = curr
            curr = curr.next
            tmp.next = prev
            prev = tmp

        tail = tmp
        self._head = tail
        old_head.next = None

    def __iter__(self):
        curr = self._head
        while curr:
            yield curr.value
            curr = curr.next


l = LinkedList()
l.add_last(10)
l.add_last(20)
l.add_last(30)
l.add_last(40)

for e in l:
    print(e)


l.reverse()
print("After reverse()")
for e in l:
    print(e)
