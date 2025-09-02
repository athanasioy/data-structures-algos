"""
Write a short recursive function that
finds the min, max of a sequence
without using any loops.
"""

def min_max(S,start):
    if len(S)==0:
        return []

    if start==len(S)-1:
        return S[len(S)-1], S[len(S)-1]

    biggest = S[start]
    smallest = S[start]

    next_biggest, next_smallest = min_max(S,start+1)
    if biggest > next_biggest:
        if smallest< next_smallest:
            return biggest, smallest
        else:
            return biggest, next_smallest
    else:
        if smallest< next_smallest:
            return next_biggest, smallest
        else:
            return next_biggest, next_smallest




S = [1,2,(10**5),-100,-1000,-100,50,123]
print(S)
print(min_max(S,0))
