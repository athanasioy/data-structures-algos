"""
Implement a function that counts the number of nodes in a circularly
linked list.
"""
class _Node:
    def __init__(self,element,next_node):
        self.element = element
        self.next = next_node

class CircularLinkedList:
    def __init__(self,tail:_Node):
        self.tail = tail

def count_nodes(circLnkLst:CircularLinkedList):
    tail = circLnkLst.tail
    curr = tail
    count = 1
    while curr.next != tail:
        count +=1
        curr = curr.next
    return count

a0=_Node(1,None)
a1=_Node(2,None)
a2=_Node(3,None)
a3=_Node(4,None)
a0.next=a1
a1.next=a2
a2.next=a3
a3.next=a0

lnkList = CircularLinkedList(a0)

print(count_nodes(lnkList))
