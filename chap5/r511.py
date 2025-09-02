
def sum_matrix(l:list[list[int]]):
    total=0
    for row in l:
        for elem in row:
            total +=elem
    return total
