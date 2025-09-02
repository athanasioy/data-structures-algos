"""
Towers of Hanoi puzzle.


In the Towers of Hanoi puzzle, we are given
a platform with three pegs, a, b, and c, sticking
out of it. On peg a is a stack of n disks,
each larger than the next, so that the smallest
is on the top and the largest is on the bottom.

The puzzle is to move all the disks
from peg a to peg c, moving one disk
at a time, so that we never place
a larger disk on top of a smaller one.


Describe a recursive algorithm for solving the
Towers of Hanoi puzzle for arbitrary n. (Hint:
Consider first the subproblem of moving all but
the nth disk from peg a to another peg using the
third as "temporary storage.")
"""


"""
Answer:

move n-1 disks from a to temp storage
move the largest disk that sits alone from a to c
move n-1 disks from temp storage to c, using a as temp storage

"""


def hanoi(n,_from, to, tmp):
    if n==1:
        print(f"move from {_from} to {to}")
        return
    hanoi(n-1,_from,tmp,to)
    print(f"move from {_from} to {to}")
    hanoi(n-1,tmp,to,_from)


hanoi(4,"a","c","b")

