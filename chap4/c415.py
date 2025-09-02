"""
Write a recursive function that
will output all of the subsets of
a set of n elements (without
repeating any subsets)

Answer:
for a sequence of N elements,
I will find all possible subsets
by appending the last element of
the sequence to all the subsets
of the N-1 sequence elements.
"""


def subsets_of(S):
    if len(S)==0:
        return [[]]
    elem = S.pop()
    subsets = subsets_of(S)
    for subset in subsets[:]:
        subset_copy = subset.copy()
        subset_copy.append(elem)
        subsets.append(subset_copy)
    return subsets

print(subsets_of(['a','b','c','d','e','f','g']))


