
def maxIncreaseKeepingSkyline(grid):

    row_maxes = [max(row) for row in grid]
    col_maxes = [max(col) for col in zip(*grid)]



grid = [ [3, 0, 8, 4],
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]