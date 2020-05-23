'''
Make use of a cumulative sum array which has corresponds to elements to the left (i-1)th index

'''


def subarraySum(nums):
    result = 0
    cumsum = [0] * (len(nums) +1)
    cumsum[0] = 0

    for i in range(1,len(nums)+1):
        cumsum[i] = cumsum[i-1] + nums[i-1]
    for start in range(len(nums)):
        for end in range(start+1, len(nums)+1):
            if cumsum[end] - cumsum[start] == k:
                result +=1
    return result
nums = [1,1,1]
k = 2

result = subarraySum(nums)