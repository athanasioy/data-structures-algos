"""
Show the result of Exercise R-10.9, assuming collisions are handled by
quadratic probing, up to the point where the method fails.


0 -> 13
1 -> 94
2 -> 39
3 -> 11
4 -> empty
5 -> 44
6 -> 88
7 -> 16
8 -> 12
9 -> 23
10 -> 20

quadratic probing fails to find a suitable index on the last element, 5.
It cycles through indexes: 9,10,2,7,3,1,1,3,4,2,10 which are all occupied.
"""
