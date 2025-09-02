"""
Describe a recursive algorithm that counts the number of nodes in a singly
linked list.

"Answer":

I will count the number of nodes in singly linked list
recursively as follows:

1. I will check the next node
1.1. If the next node exists, I will return 1 plus the return of the function by passsing the next node as a parameter
1.1. If the next node is None, I will return 1

"""

class Node:

    def __init__(self, element, next_node):
        self.next = next_node
        self.element = element

n = Node(1, Node(2,Node(3,None)))

def count(node:Node):
    if node.next is None:
        return 1
    return 1 + count(node.next)

print(count(n))
