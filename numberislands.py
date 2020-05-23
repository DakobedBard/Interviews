def nislands(grid):
    n = 0

    def dfs(i, j):
        if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[1]) and grid[i][j] == "1":
            arr[i][j] = "0"
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i, j + 1)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                dfs(i, j)

                n += 1

    return n


    return n




# arr = [[1,1,0,0,0],
#        [1,1,0,0,0],
#        [0,0,1,0,0],
#        [0,0,1,0,0],
#        [0,0,0,1,1]
#     ]
arr = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print("There are {} islands ".format(nislands(arr)) )