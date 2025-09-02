"""

Implement a function that reverses a list of elements by pushing them onto
a stack in one order, and writing them back to the list in reversed order.

"""

def reverse(l:list):
    stack = list()
    for i in range(len(l)):
        stack.append(l[i])
    l.clear()
    while len(stack)>0:
        l.append(stack.pop())

l = [1,2,3,4,5]
print(l)
reverse(l)
print(l)
