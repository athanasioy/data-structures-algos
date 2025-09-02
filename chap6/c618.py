"""

Show how to use the transfer function, described in Exercise R-6.3, and
two temporary stacks, to replace the contents of a given stack S with those
same elements, but in reversed order.

"""

def transfer(S:list,T:list):
    while len(S)>0:
        T.append(S.pop())

S = [1,2,3,4]
T1 = []
T2 = []

print(S)
transfer(S,T1)
transfer(T1,T2)
transfer(T2,S)
print(S)

S2 = [1,2,3,4]
T3 = []
print("S2=", end="")
print(S2)
transfer(S2,T3)
transfer(T3,S2)
print(S2)
