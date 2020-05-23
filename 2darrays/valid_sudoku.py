


def isValidSudoku(board):
    nrows = len(board)
    ncolumns = len(board[0])

    seen = set()

    for i in range(nrows):
        for j in range(ncolumns):
            current_val = board[i][j]
            if current_val != '.':

                if str(current_val) + " found in row " + str(i) not in seen:
                    seen.add(current_val + " found in row " + str(i))
                else:
                    return False
                if str(current_val) + " found in column " + str(j) not in seen:
                    seen.add(current_val + " found in column " + str(j))
                else:
                    return False
                if str(current_val + " found in box " + str(i//3) + " - " + str(j//3)) not in seen:
                    seen.add(current_val + " found in box " + str(i//3) + " - " + str(j//3))
                else:
                    return False
    return True

board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  ["5","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]


b = isValidSudoku(board)

print("This is a valid sudoku board {} ".format(str(isValidSudoku(board))))