"""
Suppose an initially empty stack S has executed a total of 25 push opera-
tions, 12 top operations, and 10 pop operations, 3 of which raised Empty
errors that were caught and ignored. What is the current size of S?

Answer:

Top operations do not alter the size of the Stack.
Pop operations decrease the size of the stack by 1,
except for the case of Empty exception, in which
the size of the Stack remains the same (zero).

Thus, the total size of the stack is 25-7=18



"""
