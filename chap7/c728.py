"""

Describe a fast recursive algorithm for reversing a singly linked list.

Answer:

A->B->C->D->[None]
D->C->B->A->[None]

(B)->A
n.next.next = n
(C)->B
(D)->C

(Obviously wrong because I soon as I update B to point to A,
I can't reach node C.)


C->D
return D
hook D to C
return C
hook B to C
return B
hook A to B
return A
"Answer":

I will describe a recursive algorithm that
reverses a singly linked list. The algorithm
will be O(N), which is considered fast.


I will start by passing the head node the function.
The function call itself to return the next node in line.
I will hook the next node to point to current node.
The base case is when the next node is None, in which point
I will have reached the end of the list.

"""


class Node:
    def __init__(self, n,v):
        self.next = n
        self.value = v

    def __str__(self):
        return f"Value={self.value}"

    def __repr__(self):
        return f"Value={self.value}"

class LinkedList(Node):

    def __init__(self):
        self._head = None

    def add_tail(self,v):
        if self._head is None:
            self._head = Node(None,v)
        else:
            tail = self._head
            while tail.next:
                tail = tail.next
            tail.next = Node(None,v)

    def first(self):
        return self._head
    def tail(self):
        n = self._head
        while n.next:
            n = n.next
        return n

    def add_first(self,v):
        if self._head is None:
            self._head = Node(None,v)
        else:
            newest = Node(self._head,v)
            self._head = newest

    def __iter__(self):
        next_ = self._head
        while next_:
            yield next_
            next_ = next_.next

def reverse_list(l):
    def _reverse(current):
        """
        A -> B (A)
        B -> C (B)
        C -> D (C)
        return D (D)
        D -> C (C)
        return C (C)
        C -> B (B)
        return B (B)
        B -> A (A)
        return A
        """
        if current.next is None:
            return current
        next_node = _reverse(current.next)
        next_node.next = current
        return current
    new_head = l.tail()
    new_tail = _reverse(l.first())
    l._head = new_head
    new_tail.next = None


def reverse_list2(l):
    def _reverse(current):
        """
        A -> B (A)
        B -> C (B)
        C -> D (C)
        return D (D)
        D -> C (C)
        return C (C)
        C -> B (B)
        return B (B)
        B -> A (A)
        return A
        """
        if current.next is None:
            return current
        new_head = _reverse(current.next)
        current.next.next = current
        return new_head
    old_head = l.first()
    new_head = _reverse(l.first())
    l._head = new_head
    old_head.next = None

l = LinkedList()
l.add_first(0)
l.add_tail(1)
l.add_tail(2)
l.add_tail(3)
reverse_list2(l)
for i in l:
    print(i)

