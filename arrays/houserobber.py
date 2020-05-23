

def rob(nums):

    if nums == None or len(nums) ==0:
        return 0
    if len(nums) ==1:
        return nums[0]
    if len(nums) ==2:
        return max(nums[0],nums[1])
    dp= [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
       dp[i] = max(nums[i] + dp[i-2], dp[i-1])
    return dp[len(nums) -1 ]

arr = [1,2,3,1]
print("The maximum amoutn we can get by robbing these houses is " + str(rob(arr)))