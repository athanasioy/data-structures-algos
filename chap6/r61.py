"""
What values are returned during the following series of stack operations, if
executed upon an initially empty stack? push(5), push(3), pop(), push(2),
push(8), pop(), pop(), push(9), push(1), pop(), push(7), push(6), pop(),
pop(), push(4), pop(), pop().



Answer:

push(5) -> 5
push(3) -> 3,5
pop() -> RET 3
push(2) -> 2,5
push(8) -> 8,2,5
pop() -> RET 8
pop() -> RET 2
push(9) -> 9,5
push(1) -> 1,9,5
pop() -> RET 1
push(7) -> 7,9,5
push(6) -> 6,7,9,5
pop() -> RET 6
pop() -> RET 7
push(4) -> 4,9,5
pop() -> RET 4
pop() -> RET 9
"""
