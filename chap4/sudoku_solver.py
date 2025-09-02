from pprint import pprint
sudoku = [[0,0,0,0,0,0,9,5,1],
          [0,0,0,0,2,8,0,0,7],
          [0,0,0,0,0,0,0,8,0],
          [9,8,3,4,0,1,0,0,0],
          [5,7,0,8,0,2,0,3,9],
          [0,2,0,9,0,7,8,1,5],
          [0,3,0,0,0,0,0,4,0],
          [1,0,0,3,8,0,0,0,0],
          [8,4,5,0,0,0,0,9,0]]

def is_sudoku_valid(sudoku):
    for x in range(9):
        for y in range(9):
            if sudoku[x][y]!=0:
                candidate= sudoku[x][y]
                sudoku[x][y]=0
                if not is_valid_number(sudoku,(x,y), candidate):
                    print(f"Sudoku invalid for position {(x,y)}")
                    sudoku[x][y]=candidate
                    return False
                sudoku[x][y]=candidate
    return True



def is_valid_number(sudoku, position:tuple[int,int], candidate):
    x = position[0]
    y = position[1]
    row = sudoku[x]

    for num in row:
        if candidate == num:
            return False

    for i in range(9):
        if candidate == sudoku[i][y]:
            return False
    x_block = x // 3
    y_block = y // 3

    for i in range(3):
        for j in range(3):
            if sudoku[i +x_block*3][j + y_block*3] == candidate:
                return False
    return True

def solve(sudoku):
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                for num in range(1,10):
                    if is_valid_number(sudoku,(x,y), num):
                        sudoku[x][y] = num
                        solve(sudoku)
                        sudoku[x][y] = 0
                return # dead end; no possible candidates for x,y, we must backtrack
    pprint(sudoku)

print(is_valid_number(sudoku,(0,0),6))
print(is_valid_number(sudoku,(0,0),9))
print(is_valid_number(sudoku,(0,0),2))
print(is_valid_number(sudoku,(1,0),2))
print(is_valid_number(sudoku,(1,0),3))
print(is_valid_number(sudoku,(2,3),2))

is_sudoku_valid(sudoku)

solve(sudoku)
