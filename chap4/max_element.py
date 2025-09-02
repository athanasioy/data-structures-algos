
def find_max_loop(S):
    n = len(S)
    biggest = S[0]
    for i in range(1,n):
        if S[i]>biggest:
            biggest = S[i]
    return biggest

def find_max_recursive(S, start):
    # handle empty Sequence Case
    if len(S)==0:
        return []
    # handle sequence with one elem case
    if len(S)==1:
        return S[0]

    # base case for recursion
    if len(S)-start-1<=2:
        if S[len(S)-start-1]>S[len(S)-1]:
            return S[len(S)-start-1]
        return S[len(S)-1]

    next_max = find_max_recursive(S,start+1)
    if S[start]>next_max:
        return S[start]
    else:
        return next_max

"""
Since we make n calls, 
the memory is O(n) since python
needs to hold up to N activation frames
"""
# print(find_max_loop([1,2,3,99,10,20,-1,-100]))
l=[10000,2,3,100,99,10,20,-1,-100,0]
print(find_max_recursive(l, 0))
print(find_max_recursive([1],0))
