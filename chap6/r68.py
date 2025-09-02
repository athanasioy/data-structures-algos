"""
Suppose an initially empty queue Q has executed a total of 32 enqueue
operations, 10 first operations, and 15 dequeue operations, 5 of which
raised Empty errors that were caught and ignored. What is the current
size of Q?

Answer:

The queue Q has had a total of 32 elements
pushed. The first operations do not affect the size
of Queue, so we disregard them. 15 dequeue
operations decrement the size of the Queue by one,
except when an Empty exception is raised, in which
cause the do not affect the size of the (the queue size
remains 0).
So, in the total items present in the queue is equal
to 32 -(15-5)=22

"""
