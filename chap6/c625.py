"""
Describe how to implement the queue ADT using two stacks as instance
variables, such that all queue operations execute in amortized O(1) time.
Give a formal proof of the amortized bound.

Answer:

A Queue is able to support First In, First Out
operations. For that end, a Queue class needs
to define to methods; enqueue and dequeue.

We need to describe a way to enqueue elements
in a queue such that the first element that
comes in is the first one to out in a dequeue operation,
by using two stacks.


We will achieve that by push into first stack
(s1) the enqueued elements. When dequeuing,
we will pop all elements into the second stack (s2)
and we will pop the first element of s2.

Let's validate this logic by running an example.
I am enqueuing elements 1,2,3 into Queue q.
The internal state of Q is s1 -> [1,2,3], 3
being the top of the stack.

When dequeueing, I will pop all elements into s2,
such that s2 now gets first element 3, then 2, then 1.
The internal state of s2 is now [3,2,1], with 1 being
the top element, which is the element being returned.

Now, we need to be more specific here. There are some
checks that need to made before moving elements from
one stack to another, but it all works out.

The second dequeue operation checks if there are elements
in s2. If there are, it pops the second element from s2.
If there are no elements in s2, all elements from s1 are
poped into s2 before poping again.


Thus, we have shown that this is the expected behavior.

We now need to show that the enqueue operation of this
implementation has an amortized bound of O(1).

This is obviously the case, since the enqueue operation
simply pushes an element into the internal stack.
The internal stack is backed by a dynamic array that
resizes to double the size when it reaches capacity,
which is proved by previous exercises that this has
an amortized cost of O(1). Hence the enqueue operation
is O(1).

"""

class Stack:
    def __init__(self):
        self._data = []

    def push(self,elem):
        self._data.append(elem)

    def pop(self):
        return self._data.pop()

    def size(self):
        return len(self._data)

    def __len__(self):
        return self.size()

    @property
    def is_empty(self):
        return self.size()==0

    def __repr__(self):
        return str(self._data)

class Queue:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
