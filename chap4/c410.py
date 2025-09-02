"""
Describe a recursive algorithm
to compute the integer part of
the base-two logarithm of n
using only addition and integer divsion
"""

def compute_integer_part_of_logn(a):
    if a == 1:
        return 0
    return 1 + compute_integer_part_of_logn(a//2)



print(compute_integer_part_of_logn(4))
assert compute_integer_part_of_logn(4) == 2
assert compute_integer_part_of_logn(5) == 2
assert compute_integer_part_of_logn(8) == 3
assert compute_integer_part_of_logn(9) == 3
assert compute_integer_part_of_logn(32) == 5
assert compute_integer_part_of_logn(63) == 5


print(compute_integer_part_of_logn(4))
print(compute_integer_part_of_logn(5))
print(compute_integer_part_of_logn(8))
print(compute_integer_part_of_logn(9))
print(compute_integer_part_of_logn(32))
print(compute_integer_part_of_logn(63))
