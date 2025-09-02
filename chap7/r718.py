"""
Given the set of element {a, b, c, d, e, f } stored in a list, show the final state
of the list, assuming we use the move-to-front heuristic and access the el-
ements according to the following sequence: (a, b, c, d, e, f , a, c, f , b, d, e)


Answer:
a -> [a,b,c,d,e,f]
b -> [b,a,c,d,e,f]
c -> [c,b,a,d,e,f]
e -> [e,c,b,a,d,f]
f -> [f,e,c,b,a,d]
a -> [a,f,e,c,b,d]
c -> [c,a,f,e,b,d]
f -> [f,c,a,e,b,d]
b -> [b,f,c,a,e,d]
d -> [d,b,f,c,a,e]
e -> [e,d,b,f,c,a]
"""
