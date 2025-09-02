""" Describe in detail an algorithm for reversing a singly linked list L using
only a constant amount of additional space and not using any recursion.

Answer:

There are a couple of operations that need to be done
for the linked list. First, I need to get a refernce to the current head
of the list, which will become the new tail.

I will fetch the first node (previous) and the next node (current).
I will traverse the list by assinging current's next pointer to
point to the previous node until I have reached the end of the list
(tail). I will traverse the list by getting a reference to the
current's next pointer and checking if that is None. If it None,
that means I have reached the of the list and I should stop.
I will take special care to first take current's next pointer,
then updating current's next pointer to the previous value.
For this, I will use a temporary value called tmp. Lastly,
I need to update the previous node to point to the current(tmp).

When I reach the end of the list, I need to assing the tail to the
new head of the linked list.
I also need to assign the old's head pointer to None, which the old
head is the new tail of the list.

If the size of the linked is less or equal to one, I simply return.

Pseudocode:


D is Tail, will become new head
list._head = D
old_head.next = None

A -> B -> C -> D -> E -> None
E -> D -> C -> B -> A -> None

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
