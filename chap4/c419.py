"""
write a short recursive function
that rearranges a sequence of integers
values so that all the even values
appear before all odd values


answer:

I will compare compare element i with
element j (j>i). If element j is even and element
i is odd, i will swap them.

I will do that until i equals the length of
sequence minus 1 and j equals the length of
the sequence minus two
"""


def all_even_before_odd(s,i,j):
    if i==len(s)-2 and j==len(s)-1:
        # iterated all elements
        # end
        return
    if s[i]%2==1 and s[j]%2==0: # if s[i] is odd and s[j] is even
        #swap
        tmp=s[i]
        s[i]=s[j]
        s[j]=tmp
    if j==len(s)-1:
        i+=1
        j=i+1
    else:
        j+=1
    all_even_before_odd(s,i,j)

s = [1,2,3,4,5,6,7,8,9]
print(s)
all_even_before_odd(s,0,1)
print(s)
