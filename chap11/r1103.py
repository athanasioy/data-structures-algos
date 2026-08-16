"""
How many different binary search trees can store the keys {1,2,3}
"""

"""
ANSWER:
there are 6 possibe orders (3! = 6)
1,2,3 -> 1 root (2 Right (3 Right))
1,3,2 -> 1 root (3 Right (2 Left))
2,3,1 -> 2 root (3 Right, 1 Left)
2,1,3 -> 2 root (3 Right, 1 Left)
3,1,2 -> 3 root (1 Left ( 2 Right))
3,2,1 -> 3 root (2 Left (1 Left))

in total 5 different distinct trees
"""
