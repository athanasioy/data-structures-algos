"""
Give a recursive implementation of a singly linked list class, such that an
instance of a nonempty list stores its first element and a reference to a list
of remaining elements.
"""


class RecursiveLinkedList:

    def __init__(self, l):
        if l:
            self.value = l[0]
            self.next = __class__(l[1:])
        else:
            self.value = None
            self.next = None

    def is_empty(self):
        return self.next is None

    def append(self,v):
        tail = self.next
        while tail.next is not None:
            tail = tail.next
        tail.value = v
        tail.next = __class__([])

    def length(self):
        if self.next == None:
            return 0
        return 1 + self.next.length()



l=[1,2,3,4]

ll = RecursiveLinkedList(l)
ll.append(10)

print("l="+ str(ll.length()))

while ll.next is not None:
    print(ll.value)
    ll = ll.next

q = RecursiveLinkedList([0])

while q.next is not None:
    print(q.value)
    q = q.next
