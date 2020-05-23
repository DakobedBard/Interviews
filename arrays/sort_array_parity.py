[def sortArrayByParity(A):

    parity = [0] * len(A)
    evens = 0
    odds = len(A) -1

    for num in A:
        if num % 2 ==0:
            parity[evens] = num
            evens +=1
        else:
            parity[odds] = num
            odds -= 1
    return parity


def sortArrayByParityII(A):
    i = 0
    j = 1
    n = len(A)
    while i < n and j < n:
        while i < n and A[i] % 2 == 0:
            i +=2
        while j < n and A[j] % 2 ==1:
            j +=2

        if i < n and j < n:
            A[j],A[i] = A[i], A[j]
    return A

nums = [4,2,5,7]
parity= sortArrayByParityII(nums)