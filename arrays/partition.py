


def arrayPairSum(nums):
    sum_ = 0
    nums.sort()
    for i in range(0,len(nums), 2):
        sum_ += nums[i]
    return sum_

nms = [1,4,3,2]
print("The minimum sum of pairs is {}".format(arrayPairSum(nums)))