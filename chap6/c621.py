"""
Show how to use a stack S and a queue Q to generate all possible subsets
of an n-element set T nonrecursively.
"""

class Stack:
    def __init__(self):
        self._data = []

    def push(self,elem):
        self._data.append(elem)

    def pop(self):
        return self._data.pop()

    def size(self):
        return len(self._data)

    def __len__(self):
        return self.size()

    @property
    def is_empty(self):
        return self.size()==0

    def __repr__(self):
        return str(self._data)

from queue import Queue

def subsets(l):
    result = set()
    S = Stack()
    Q = Queue()
    Q.put([])
    for e in l:
        while not Q.empty():
            sub = Q.get()
            S.push(sub.copy()+[e])
            S.push(sub.copy())

        while not S.is_empty:
            Q.put(S.pop())

    return Q


def to_list(Q):
    l = []
    while not Q.empty():
        l.append(Q.get())
    return l

q = subsets([1,2,3,4])
ls=to_list(q)
print(ls) # Should output [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,3],[1,2,3]]
