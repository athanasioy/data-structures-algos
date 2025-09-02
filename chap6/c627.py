"""
Suppose you have a stack S containing n elements and a queue Q that is
initially empty. Describe how you can use Q to scan S to see if it contains a
certain element x, with the additional constraint that your algorithm must
return the elements back to S in their original order. You may only use S,
Q, and a constant number of other variables.

Answer:

Given a stack S that contains N elements,
I want to find if element x exists in stack S.

The contraints of the problem is using only a
queue Q and a fixed amount of variables.


I will initialize a boolean variable found
and set its initial value to false.
I will also initialize a integer variable
count set it equal to 0.

While the element is not found, I will do
the following:

1. Pop an element of S into local variable e
2. check if e is equal to x
3. if it is, I set found equal to true. If not, I will skip this.
4. I will enqueue e into Q
5. I will increment count by 1

This way I check if x is in stack S.
Now I need to restore the original order of S
by using Q and the variable 'count'.

First, I will dequeue all items from Q to S.
This will restore the elements taken from S,
but in reversed order.

Then I will pop 'count' amount of elements from
S to Q. Finally, I will dequeue all times from Q
to S, effectively restoring original order.


Let's validate that with an example:
S=[1,2,3,4,5]
x=3
Q =[]

First Step:
x=5
found=false
Q=[5]
S=[1,2,3,4]
c=1
Second Step:
x=4
found=false
Q=[5,4]
S=[1,2,3]
c=2
Third Step:
x=3
found=True
Q=[5,4,3]
S=[1,2]
c=3
(Stop popping elements from S, x is found)
Now we restore the original order of S.
First, we dequeue all elements from Q to S.
S=[1,2,5,4,3]
Q=[]
Now we pop 'count' elements from S to Q
S=[1,2]
Q=[3,4,5]
Now we dequeue again:

S=[1,2,3,4,5]
Q=[]
We observe that the original order of S is restored.
"""
