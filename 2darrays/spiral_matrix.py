

def spiralOrder(matrix):
    result = []
    if len(matrix) == 0:
        return result


    rowBegin = 0
    rowEnd = len(matrix)-1
    columnBegin = 0
    columnEnd = len(matrix[0]) -1



    while rowBegin <= rowEnd and columnBegin <= columnEnd:
        for i in range(columnBegin, columnEnd+1):
            result.append(matrix[rowBegin][i])
        rowBegin +=1
        for i in range(rowBegin, rowEnd+1):
            result.append(matrix[i][columnEnd] )
        columnEnd -=1
        if rowBegin <= rowEnd:
            for i in range(columnEnd, columnBegin-1, -1):
                result.append(matrix[rowEnd][i])
        rowEnd -=1
        if columnBegin <= columnEnd:
            for i in range(rowEnd, rowBegin-1, -1):
                result.append(matrix[i][columnBegin])
        columnBegin+=1

    return result

matrix =[[1,2,3,4],[ 5,6, 7,8], [9,10,11,12]]

result = spiralOrder(matrix)