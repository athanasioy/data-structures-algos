"""
Implement a function with signature transfer(S, T) that transfers all ele-
ments from stack S onto stack T, so that the element that starts at the top
of S is the first to be inserted onto T, and the element at the bottom of S
ends up at the top of T.
"""
def transfer(S:list,T:list):
    while len(S)>0:
        T.append(S.pop())

S=[1,2,3,4]
T=[]
transfer(S,T)
print(T)
