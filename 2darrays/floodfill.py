
def floodfill(image, sr, sc, new_color):
    color = image[sr][sc]

    def dfs(image, i, j, new_color):
        if i < 0 or i >= len(image) or j <0 or j>= len(image[0]) or image[i][j] != color:
            return
        image[i][j] = new_color
        dfs(image, i+1,j, new_color)
        dfs(image, i-1,j, new_color)
        dfs(image, i,j+1, new_color)
        dfs(image, i,j-1, new_color)

    dfs(image, sr, sc, new_color)
image = [[1,1,1],[1,1,0],[1,0,1]]
floodfill(image, 1,1,2)