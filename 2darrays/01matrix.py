
def updateMatrix(matrix):
    nrows = len(matrix)
    ncolumns  = len(matrix[0])

    dp = [[float('inf') for i in range(ncolumns)] for j in range(nrows)]
    for i in range(nrows):
        for j in range(ncolumns):
            if matrix[i][j] ==0:
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] = min(dp[i-1][j] +1, dp[i][j])
                if j > 0:
                    dp[i][j] = min(dp[i][j-1] +1, dp[i][j] )
    for i in range(nrows-1,-1,-1):
        for j in range(ncolumns-1, -1, -1):
            if i < nrows - 1:
                dp[i][j] = min(dp[i+1][j] +1, dp[i][j])
            if j < ncolumns -1:
                    dp[i][j] = min(dp[i][j+1] +1, dp[i][j] )

    return dp


grid =[[0,0,0],
 [0,1,0],
 [1,1,1]]

dp = updateMatrix(grid)


m1 = [[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]
dp = updateMatrix(m1)
