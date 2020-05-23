



def solve(board):
    def boundaryDFS(i, j, board):
        if i <0 or i > len(board) or j < 0 or j > len(board[0]): return

        if board[i][j] == 'O':
            board[i][j] = "*"
        if i > 0 and board[i-1][j] == 'O':
            boundaryDFS(i-1, j, board )
        if i < len(board) -1 and board[i+1][j] == 'O':
            boundaryDFS(i+1, j, board )
        if j > 0 and board[i][j-1] == 'O':
            boundaryDFS(i, j-1, board )
        if j < len(board[0]) -1 and board[i][j+1] == 'O':
            boundaryDFS(i, j+1, board )
        return

    for i in range(len(board)):
        if board[i][0] == 'O':
            boundaryDFS(i,0,board)
        if board[i][len(board[0])-1] =='O':
            boundaryDFS(i, len(board[0]) -1, board)

    for j in range(len(board[0])):
        if board[0][j] == 'O':
            boundaryDFS(0,j,board)
        if board[len(board)-1][j] =='O':
            boundaryDFS(len(board) -1, j, board)

    for i in range(len(board)):
        for j in range(len(board[1])):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            if board[i][j] =='*':
                board[i][j] = 'O'




grid =[["X","O","X","O","X","O"],
       ["O","X","O","X","O","X"],
       ["X","O","X","O","X","O"],
       ["O","X","O","X","O","X"]]


newgrid = solve(grid)