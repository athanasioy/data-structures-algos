"""
For a tree T, let nI denote the number of its internal nodes, and let nE
denote the number of its external nodes. Show that if every internal node
in T has exactly 3 children, then nE = 2nI +1.

Answer:

For every tree T, the following holds:
n = nE + nI (1)

Also, every tree T has n-1 edges.

Furthermore, if every internal node has exactly 3 children,
meaning that for every 3 edges I have one internal node,
I can derive the following equation.

3nI = n - 1
=> n = 3nI +1 (2)

combining (1) + (2)

3nI + 1 = nE + nI
=> nE = 2nI +1
"""
