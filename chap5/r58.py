"""
Experimentally evaluate the efficiency of the pop method of Python’s list
class when using varying indices as a parameter, as we did for insert on
page 205. Report your results akin to Table 5.5

"""

N = [10**(n+1) for n in range(1,6)]
print(N)

import random
import timeit
for n in N:
    a = [random.random() for _ in range(n)]
    print(f"N={n:_},k=0", end='\t')
    print(timeit.timeit('a.pop(0)',number=100, globals=globals()))
for n in N:
    a = [random.random() for _ in range(n)]
    print(f"N={n:_},k=n//2", end='\t')
    print(timeit.timeit('a.pop(n//2)',number=1, globals=globals()))

for n in N:
    a = [random.random() for _ in range(n)]
    print(f"N={n:_},k=n", end='\t')
    print(timeit.timeit('a.pop(n-1)',number=1, globals=globals()))
