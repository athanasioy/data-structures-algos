"""
TODO:
Based on the discussion of page 207, develop an experiment to compare
the efficiency of Python’s list comprehension syntax versus the construc-
tion of a list by means of repeated calls to append
"""
import timeit
def create_with_append(k):
    l = []
    for i in range(k):
        l.append(None)
    return l

def create_with_list_comprehension(k):
    return [None for _ in range(k)]


n = [3,4,5,6,7,8]
k = [10**x for x in n]
print(k)

for n in k:
    print(f"k={n:_}\toperation:append", end='\t')
    print(timeit.timeit('create_with_append(n)',number=10,globals=globals()))
    print(f"k={n:_}\toperation:comprehension", end='\t')
    print(timeit.timeit('create_with_list_comprehension(n)',number=10,globals=globals()))
