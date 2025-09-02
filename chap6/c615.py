"""
Suppose Alice has picked three distinct integers and placed them into a
stack S in random order. Write a short, straight-line piece of pseudo-code
(with no loops or recursion) that uses only one comparison and only one
variable x, yet that results in variable x storing the largest of Alice’s three
integers with probability 2/3. Argue why your method is correct.

answer:

code:

x = S.pop()
if S.top() > x: #top() does not mutate the stack
    x = S.pop()

I take a random number x out of the three numbers.
If the next number is bigger than my initial number,
I switch numbers.

My initial chances of choosing the biggest number
is 1/3. Whether I switch or not, I have essentially
eliminated one possible number as NOT being the
largest one.

So in a pool of three numbers, one of which is the
biggest, I have 2/3 chances of chosing the largest
one, if I am sure that 1 is definitely the wrong choice.

So my chances are always 2/3.

Mathetically,
P(A>C|A>B) = P(A>B AND A>C)/P(A>B)
=(1/3)/(1/2)=2/3

if I switch with B
P(B>C|B>A) = P(B>C and B>A)/P(B>A)=2/3


"""
