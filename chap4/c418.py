"""
use recursion to write a
Python function that for
determining if a string s
has vowels that consonants

answer:
I will return the number of
values and consonants in a tuple
by checking if the current character
is a value or a consonant plus
the result of function for the
next of the string.

my base case is when the string
is composed of a single char,in
which case I will simply do the
comparison without recursion calls.

"""
def is_vowel(char):
    return char.lower() in 'aeiou'
def vowels_consonants(s,start):
    if len(s)==start+1:
        if is_vowel(s[start]):
            return (1,0)
        else:
            return (0,1)
    v,c = vowels_consonants(s,start+1)
    if is_vowel(s[start]):
        return (v+1,c)
    else:
        return (v,c+1)

s = 'hello'
print(vowels_consonants(s,0))
s2 = 'aeioux'
print(vowels_consonants(s2,0))
