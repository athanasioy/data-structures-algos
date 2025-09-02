"""
Describe a nonrecursive algorithm for enumerating all permutations of the
numbers {1, 2, . . . , n} using an explicit stack.

Answer:

For a set of numbers from 1 to n, I will produce all permutations
for a set size of n.

I will push an empty set and the available numbers into my stack
While the stack is not empty, i will do:

1. I will pop the current position from the stack
2. For every available number i will do add it to the set
3. I will check if the if the set is equal to the permutation number
3.1. If it is, I will add it to the result set
3.2 if it is not, I will push the current set and the available numbers to the stack
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

    @property
    def is_empty(self):
        return self.size()==0

    def __repr__(self):
        return str(self._data)

def generate_permutations(nums:list[int], n:int):
    S = Stack()
    S.push(([], nums))
    results = []
    while not S.is_empty:
        s, avail_nums = S.pop()
        for num in avail_nums:
            s.append(num)
            if len(s)==n:
                results.append(s.copy())
            else:
                S.push((s.copy(),[number for number in avail_nums if number!=num]))
            s.remove(num)

    return results

def generate_permutations_r(nums,avail_nums,n):

    if len(nums)==n:
        return [nums]

    s = []
    for num in avail_nums:
        nums.append(num)
        s.extend(generate_permutations_r(nums.copy(),[number for number in avail_nums if number!=num],n))
        nums.remove(num)

    return s


r = generate_permutations([1,2,3,4],n=2)
print(r)
print(len(r))
rr = generate_permutations_r([],[1,2,3,4],n=2)
#print(rr)
# print(len(rr))
