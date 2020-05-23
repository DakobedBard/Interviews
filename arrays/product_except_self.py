

def productExceptSelf(nums):
    n= len(nums)
    L = [0] * n
    R = [0] *  n
    result =  [0] * n
    L[0] = 1
    R[n-1] =1

    for i in range(1,n):
        L[i] = L[i-1] * nums[i-1]
    for i in range(n-2,-1,-1):
        R[i] = R[i+1] * nums[i+1]
    for i in range(n):
        result[i] = L[i] * R[i]

    return result

nums = [4,5,1,8,2]
L, R = productExceptSelf(nums)