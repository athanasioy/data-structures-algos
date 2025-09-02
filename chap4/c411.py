"""
Describe an efficient recursive function
for solving the element uniqueness problem,
which runs in time that is at most O(n^2)
in the worst case without using sorting.
"""

"""
Answer:
I will take a sequence S together with
two indexes i,j (i<j in any case)

I will compare S[i] with S[j].

If they are equal, I will simply return false,
i.e. the sequence contains is not unique, since
two elements are equal to each other.

If they are not equal, I will call
the function again with i and j+1 and return
the result.

If j is equal to the length of S minus one,
I will increment i and set j=i+1.

If i is equal to the length of S two
and j is equal to the length of S minus 1,
that means that the function has iterated
all the elements in the sequence S and has
not found any elements to be equal to each other.
In this case, I will return true.

At most, this algorithm will run
for n+n-1+n-2...+2+1 times, which is O(n^2)
"""


def is_unique(S,i,j):
    if len(S)==0:
        return True

    if i == len(S)-2 and j==len(S)-1:
        # we have reached the end and no duplicates
        # were found, return true.
        return True

    if S[i]==S[j]:
        #duplicate found, S is not unique
        return False

    if j==len(S)-1:
        # if j has reached the end of the list
        # increment i and reset j to i+1
        i += 1
        j = i+1
    else:
        # else increment j to the next element
        # of S
        j += 1

    return is_unique(S,i,j)


print(is_unique([1,2,34,5,6,7,8,9,10],0,1)) #Should print true
print(is_unique([1,2,2,5,6,7,8,9,10],0,1)) #Should print false
print(is_unique([1,2,3,5,6,7,8,9,1],0,1)) #Should print false
