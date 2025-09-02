
def isabela_sum(S):
    if len(S)==0:
        return 0
    n = len(S)
    B = [0]*(n//2)
    for i in range(n//2):
        B[i] = S[2*i] + S[2*i+1]
    if len(B)==1:
        return B[0]
    else:
        return isabela_sum(B)


print(isabela_sum([0,10,20,4,3,-1,1,7]))

import timeit
import random
n = []
for i in range(10):
    n.append(2**i)

for k in n:
    l = [random.random() for _ in range(k)]
    print(f"Timing for k={k}")
    print(timeit.timeit(stmt='isabela_sum(l)',globals=globals()))
