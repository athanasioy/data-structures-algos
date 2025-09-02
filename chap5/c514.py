"""
TODO:
Consider an implementation of a dynamic array, but instead of copying
the elements into an array of double the size (that is, from N to 2N) when
its capacity is reached, we copy the elements into an array with N/4
additional cells, going from capacity N to capacity N + N/4. Prove that
performing a sequence of n append operations still runs in O(n) time in
this case.


Answer:

Assume we have append N elements to a
dynamic array that resizes to 1,25N each time
that it reaches capacity.

For a N elements, we have a total of
N^(log1,25N) (1,25 is the base)
resizes.
Thus we have a total of
S=N + Σ(i=1 to log1,25N)1,25^1,25i=N + 2^(log(1,25(N+1)) -1 = O(n)

## Cleaner Answer

Assume a initial capacity of 1 and each
resize grows the capaicty by a factor of 1.25.

That means, in order to accomodate N elements,
we need to 1,25^r>=N => r>=log1,25N (where 1,25 is the base)

Each time we resize, we pay a price of c, which is the capacity
of the array.
Thus the total of the capacity is
c + c*1,25 + c*1,25^2 + ... + c*1,25^r.
This is a geometric series with a sum equal to
S = c*(1,25^r-1)/(1,25-1), which is O(n)
(1,25^r=1,25^(log1,25N)=N)

"""
