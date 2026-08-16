"""
Dr. Amongus claims that the order in which a fixed set of entries is inserted
into a binary search tree does not matter—the same tree results every time.
Give a small example that proves he is wrong.
"""


"""
let a set of entries be {1,2}
WTS that the order of insertion does not result always in the same tree
suffices to show that two different orders result in two different trees
(proof by counter example)

let a order be [1,2]
the resulting tree is
1 root ( 2 right)

let another order br [2,1]
the resulting tree is
2 root ( 1 left)

two diferent trees result from different orders
thereby proving that the statement is wrong
"""
