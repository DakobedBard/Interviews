
def sortedSquares(A):
    positive = 0
    while(positive < len(A) and A[positive] < 0):
        positive +=1
    negative = positive -1


    squares = [0] * len(A)

    counter = 0
    while negative >=0 and positive < len(A):
        if(A[negative] **2 < A[positive] **2):
            squares[counter] = A[negative] **2
            counter +=1
            negative -=1
        else:

            squares[counter] = A[positive] **2
            counter += 1
            positive +=1
    while negative >= 0:
        squares[counter] = A[negative] **2
        counter +=1
        negative -=1
    while positive < len(A):
        squares[counter] = A[positive] **2
        counter +=1
        positive +=1
    return squares



arr = [-4,-1,0,3,10]
squares = sortedSquares(arr)