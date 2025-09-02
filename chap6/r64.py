"""
Give a recursive method for removing all the elements from a stack.
"""

def clear_all(S):
    if len(S)>0:
        _ = S.pop()
        clear_all(S)


S = [1,2,3,4] # 4 is the top element
print(S)
clear_all(S)
print(S)

