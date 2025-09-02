"""
Write a short recursive function
that takes a character string s
and outputs its reverse.
For example, the reverse of
'pots&pans' would be
'snap&stop'.


Answer:

"""

def reverse(S,start,stop):
    if stop-start>1:
        return S[stop-1] + reverse(S,start+1,stop-1) + S[start]
    # return S[stop-1]
    return S[start]

s = 'pots&pans'
print(reverse(s,0,len(s)))
print(reverse("hello_there!",0,len("hello_there!")))
print(reverse('abc',0,3))


