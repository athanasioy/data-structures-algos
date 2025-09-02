"""

Modify the ArrayStack implementation so that the stack’s capacity is lim-
ited to maxlen elements, where maxlen is an optional parameter to the
constructor (that defaults to None). If push is called when the stack is at
full capacity, throw a Full exception (defined similarly to Empty).

"""

class Full(Exception):
    pass

class Empty(Exception):
    pass

class ArrayStack:

    def __init__(self,maxlen:int=None):
        self._data = []
        self._maxlen = maxlen

    def push(self,elem):
        if self._maxlen and self.size() == self._maxlen:
            raise Full("Stack is Full.")
        self._data.append(elem)

    def pop(self):
        if self.size() == 0:
            raise Empty("Stack is Empty.")
        return self._data.pop()

    def top(self):
        if self.size() == 0:
            raise Empty("Stack is Empty.")
        return self._data[-1]

    def size(self):
        return len(self._data)

    def __len__(self):
        return self.size()


s = ArrayStack(maxlen=4)
print(len(s))
s.push(1)
print(len(s))
s.push(10)
s.push(100)
print(len(s))
print(s.pop())
print(s.pop())
print(s.pop())
s.push(100)
s.push(100)
s.push(100)
s.push(100)
print(s.size())
s.push("should throw")
