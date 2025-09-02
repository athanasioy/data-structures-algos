"""
Postfix notation is an unambiguous way of writing an arithmetic expres-
sion without parentheses. It is defined so that if “(exp1) op (exp2)” is a
normal, fully parenthesized expression whose operation is op, the postfix
version of this is “pexp1 pexp2 op”, where pexp1 is the postfix version of
exp1 and pexp2 is the postfix version of exp2 . The postfix version of a sin-
gle number or variable is just that number or variable. For example, the
postfix version of “((5 + 2) ∗ (8 − 3))/4” is “5 2 + 8 3 − ∗ 4 /”. Describe
a nonrecursive way of evaluating an expression in postfix notation.


Answer:

Given an expression written in postfix notation,
I will evaluate it as follows in an non recursive manner:
1. I will begin by reading the first number, the second number and the operator.
2. I will put the result of the expression into a Stack
3. While the stack is not empty:
    1. if i reached the end of the end, I will return the one expression stored in the stack. if the stack has more than one element, the expression is invalid
    1. I will read the next character
        1. if the next character is an operator, I will pop the result of the previous expression and evaluate the result, and put it into the stack
        2. if the next character is a number, i will read the next character
            1. if the next character is also a number, i will read the next character which would be an operator, evaluate the result and put into the stack.


"""


