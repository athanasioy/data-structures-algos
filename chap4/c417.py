"""
Write a short recursive function
that determines if a string
is a palindrome, that is,
it is equal to its reverse.

For example, 'racecar' and
'gohangasalamiimalasagnahog'
are palindromes.

answer:
I will check the the digits
at position i and j for equality.
if they are not, the function returns false.
if they are equal, I will call
the function for i+1 and j-1 until
j-i <1 

"""

def is_palindrome(s,i,j):
    if j-i>1:
        if s[i]!=s[j]:
            return False
        else:
            return is_palindrome(s,i+1,j-1)
    return True

s = 'gohangasalamiimalasagnahog'
print(is_palindrome(s,0,len(s)-1))
s2 = 'not_palindrome'
print(is_palindrome(s2,0,len(s2)-1))
s3 = 'racecar'
print(is_palindrome(s3,0,len(s3)-1))

