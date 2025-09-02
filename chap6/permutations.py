
class Stack:

    def __init__(self):
        self._data = []

    def push(self,elem):
        self._data.append(elem)

    def pop(self):
        return self._data.pop()

    def size(self):
        return len(self._data)

    @property
    def is_empty(self):
        return self.size()==0

    def __repr__(self):
        return str(self._data)


def permutations(elements, n):
    results = []
    S = Stack()
    S.push(([],elements))
    while not S.is_empty:
        curr_set, curr_elements = S.pop()
        for elem in curr_elements:
            curr_set.append(elem)
            if len(curr_set) == n:
                results.append(curr_set.copy())
            else:
                S.push((curr_set.copy(), [el for el in curr_elements if el != elem]))
            curr_set.remove(elem)
    return results



print(permutations([1,2,3,4],2))
