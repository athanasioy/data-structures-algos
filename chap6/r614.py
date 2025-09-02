"""
Repeat the previous problem using the deque D and an initially empty
stack S.
D=[1,2,3,4,5,6,7,8]
S=[]
S.push(D.pop())
S.push(D.pop())
S.push(D.pop())
S.push(D.pop())
S.push(D.pop())
S=[8,7,6,5,4]
D=[1,2,3]
D.appendleft(S.pop())
D.append(S.pop())
S=[8,7,6]
D=[4,1,2,3,5]
S.push(D.popleft())
S=[8,7,6,4]
D=[1,2,3,5]
D.append(S.pop())
D.append(S.pop())
D.append(S.pop())
D.append(S.pop())
S=[]
D=[1,2,3,5,4,6,7,8]
"""


