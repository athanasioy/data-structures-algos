"""
The build expression tree method of the ExpressionTree class requires
input that is an iterable of string tokens. We used a convenient example, (((3+1)x4)/((9-5)+2)) , in which each character is its own token, so that the string itself sufficed as input to build expression tree.
In general, a string, such as (35 + 14) , must be explicitly tokenized
into list [ ( , 35 , + , 14 , ) ] so as to ignore whitespace and to
recognize multidigit numbers as a single token. Write a utility method,
tokenize(raw), that returns such a list of tokens for a raw string.
"""


def tokenize(raw):
    tokens = []
    start_idx = 0
    single_char_tokens= ['(',')', '+','-','/','*','X']
    i=0
    while i<len(raw):
        char = raw[i]
        if char in single_char_tokens:
            tokens.append(char)
            i+=1
        elif char.isdigit():
            start_of_digit = i
            while i<len(raw) and char.isdigit():
                i+=1
                char = raw[i]
            tokens.append(raw[start_of_digit:i])
        else:
            i+=1
    return tokens


print(tokenize("( 35 + 14  )"))
print(tokenize("( (35 + 14 ) * (2 /(5-3) +1)"))
print(tokenize('(((3+1)x4)/((9-5)+2))'))
