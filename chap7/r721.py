"""
Suppose we have an n-element list L maintained according to the move-
to-front heuristic. Describe a sequence of n2 accesses that is guaranteed
to take Ω(n3) time to perform on L.


Answer:

let 1 to n be the elements of L.
I will repeat the following sequence N times.
I will access element n which will take Ω(n)
I will acesss element n-1 which will take Ω(n), since n-1 is the new back.
...
I will access element 1 which will take Ω(n)


Hence, this sequence will take n*n*Ω(n), Ω(n^3)
"""
