"""
TODO:
Develop an experiment to compare the relative efficiency of the extend
method of Python’s list class versus using repeated calls to append to
accomplish the equivalent task.
"""

def extend_list(l:list):
    t = []
    t.extend(l)

def append_list(l):
    t = []
    for i in l:
        t.append(i)


import timeit


k = [10**n for n in range(4)]

for n in k:
    t = [0 for _ in range(n)]
    print(f"n={n}")
    print("extend", end="\t")
    print(f'{timeit.timeit("extend_list(t)", globals=globals()):0.2f}')
    print("append", end="\t")
    print(f'{timeit.timeit("append_list(t)", globals=globals()):0.2f}')
