"""
TODO:
In Section 5.4.2, we described four different ways to compose a long
string: (1) repeated concatenation, (2) appending to a temporary list and
then joining, (3) using list comprehension with join, and (4) using genera-
tor comprehension with join. Develop an experiment to test the efficiency
of all four of these approaches and report your findings
"""

def create_with_concat(n:int):
    s = ""
    for i in range(n):
        s += "_"

def create_with_list(n:int):
    temp = []
    for i in range(n):
        temp.append("_")
    s = "".join(temp)

def create_with_list_comp(n:int):
    s = "".join(["_" for _ in range(n)])

def create_with_gen(n:int):
    s = "".join("_" for _ in range(n))


k = [10**x for x in range(7)]

import timeit

for n in k:
    print(f"n={n}, Conc", end="\t\t")
    print(timeit.timeit("create_with_concat(n)", number=1000,globals=globals()))
    print(f"n={n}, List", end="\t\t")
    print(timeit.timeit("create_with_list(n)", number=1000,globals=globals()))
    print(f"n={n}, Comp", end="\t\t")
    print(timeit.timeit("create_with_list_comp(n)", number=1000,globals=globals()))
    print(f"n={n}, Gens", end="\t\t")
    print(timeit.timeit("create_with_gen(n)", number=1000,globals=globals()))
