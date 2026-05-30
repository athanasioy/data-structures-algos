"""
What would be a good hash code for a vehicle identification number that
is a string of numbers and letters of the form “9X9XX99X9XX999999,”
where a “9” represents a digit and an “X” represents a letter?
"""

"""
Answer:
What consistutes a good hash code?
it should avoid collisions.

Sequence of number and elements should be taken
into account, therefore a simple of the ascii number
does not suffice.

A good approach for generating a hash
code for this kind of string is a polynomial
hash code.
"""
