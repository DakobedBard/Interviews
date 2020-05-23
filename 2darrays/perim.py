

def islandPerimiter(grid):
    nrows = len(grid)
    ncolumns = len(grid[0])

    perim = 0

    for i in range(nrows):
        for j in range(ncolumns):

            if grid[i][j] ==1:
                perim +=4
                print("i: {} j {} perim {}".format(i,j, perim))
                if i>0 and grid[i-1][j] ==1:
                    perim -=2
                    print("i: {} j {} perim {}".format(i,j, perim))
                if j >0 and grid[i][j-1] ==1:
                    perim -= 2
                    print("i: {} j {} perim {}".format(i,j, perim))
    return perim

grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]


print("The perimiter of the island is {}".format(islandPerimiter(grid)))