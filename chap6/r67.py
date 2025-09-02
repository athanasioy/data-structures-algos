"""
What values are returned during the following sequence of queue opera-
tions, if executed on an initially empty queue? enqueue(5), enqueue(3),
dequeue(), enqueue(2), enqueue(8), dequeue(), dequeue(), enqueue(9),
enqueue(1), dequeue(), enqueue(7), enqueue(6), dequeue(), dequeue(),
enqueue(4), dequeue(), dequeue().

Answer:
enqueue(5) -> [5]
enqueue(3) -> [5,3]
dequeue() -> RET 5
enqueue(2) -> [3,2]
enqueue(8) -> [3,2,8]
dequeue() -> RET 3
dequeue() -> RET 2
enqueue(9) -> [8,9]
enqueue(1) -> [8,9,1]
dequeue() -> RET 8
enqueue(7) -> [9,1,7]
enqueue(6) -> [9,1,7,6]
dequeue() -> RET 9
dequeue() -> RET 1
enqueue(4) -> [7,6,4]
dequeue() -> RET 7
dequeue() -> RET 6
"""

