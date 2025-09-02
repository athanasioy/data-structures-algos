"""
Suppose you have a deque D containing the numbers (1, 2, 3, 4, 5, 6, 7, 8),
in this order. Suppose further that you have an initially empty queue Q.
Give a code fragment that uses only D and Q (and no other variables) and
results in D storing the elements in the order (1, 2, 3, 5, 4, 6, 7, 8).

Q.enqueue(D.popleft())
Q.enqueue(D.popleft())
Q.enqueue(D.popleft())
Q.enqueue(D.popleft())
Q=[1,2,3,4]
D=[5,6,7,8]
Q.enqueue(D.pop())
Q.enqueue(D.pop())
Q.enqueue(D.pop())
Q=[1,2,3,4,8,7,6]
D=[5]
D.append_left(Q.dequeue())
D.append_left(Q.dequeue())
D.append_left(Q.dequeue())
Q=[4,8,7,6]
D=[1,2,3,5] # Wrong D=[3,2,1,5]
D.append(Q.dequeue())
Q=[8,7,6]
D=[1,2,3,5,4]
D.append(Q.dequeue())
D.append(Q.dequeue())
D.append(Q.dequeue())
Q=[]
D=[1,2,3,5,4,8,7,6]
Q.enqueue(D.pop())
Q.enqueue(D.pop())
Q.enqueue(D.pop())
Q=[6,7,8]
D=[1,2,3,5,4]
D.append(Q.dequeue())
D.append(Q.dequeue())
D.append(Q.dequeue())
Q=[]
D=[1,2,3,5,4,6,7,8]

TRY 2#:

Q.put(D.popleft())
Q.put(D.popleft())
Q.put(D.popleft())
Q.put(D.popleft())

Q=[1,2,3,4]
D=[5,6,7,8]
Q.put(D.pop())
Q.put(D.pop())
Q.put(D.pop())
Q=[1,2,3,4,8,7,6]
D=[5]

D.append(Q.get())
D.append(Q.get())
D.append(Q.get())
Q=[4,8,7,6]
D=[5,1,2,3]
Q.put(D.popleft())
Q=[4,8,7,6,5]
D=[1,2,3]
D.appendleft(Q.get())
D.appendleft(Q.get())
D.appendleft(Q.get())
D.appendleft(Q.get())
Q=[5]
D=[6,7,8,4,1,2,3]
D.append(Q.get())
Q=[]
D=[6,7,8,4,1,2,3,5]
Q.put(D.popleft())
Q.put(D.popleft())
Q.put(D.popleft())
Q.put(D.popleft())
Q=[6,7,8,4]
D=[1,2,3,5]
Q.put(D.pop())
Q.put(D.pop())
Q.put(D.pop())
Q.put(D.pop())
Q=[6,7,8,4,5,3,2,1]
D=[]
D.append(Q.get())
D.append(Q.get())
D.append(Q.get())
Q=[4,5,3,2,1]
D=[6,7,8]
D.appendleft(Q.get())
D.appendleft(Q.get())
D.appendleft(Q.get())
D.appendleft(Q.get())
D.appendleft(Q.get())
Q=[]
D=[1,2,3,5,4,6,7,8]

"""


"""

from collections import deque
from queue import Queue

Q = Queue()
D = deque()

D.extend([1,2,3,4,5,6,7,8])

Q.append(D.popleft())
Q.append(D.popleft())
Q.append(D.popleft())
Q.append(D.popleft())
Q.append(D.pop())
Q.append(D.pop())
Q.append(D.pop())
D.appendleft(Q.pop())
D.appendleft(Q.pop())
D.appendleft(Q.pop())
D.append(Q.pop())
D.append(Q.pop())
D.append(Q.pop())
D.append(Q.pop())
Q.append(D.pop())
Q.append(D.pop())
Q.append(D.pop())
D.append(Q.pop())
D.append(Q.pop())
D.append(Q.pop())
print("final")
print(D)
print(Q)
