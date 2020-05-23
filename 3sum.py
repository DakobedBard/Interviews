
def threeSum(nums):
    nums = sorted(nums)

    result = []
    for i in range(len(nums)-2):
        if i ==0 or ( i > 0 and nums[i] != nums[i-1]):
            low = i +1
            high = len(nums) -1
            while low < high:
                sum = nums[low] + nums[high]
                if sum == -nums[i]:
                    result.append([nums[i],nums[low],nums[high]])
                    while low < high and nums[low] == nums[low+1]: low +=1
                    while low < high and nums[high] == nums[high-1]: high -=1
                    low+=1
                    high -=1
                elif nums[low] + nums[high] > - nums[i]:
                    high -=1
                else:
                    low+=1
    return result




def threeSumClosest(nums, target):
    nums = sorted(nums)
    n = len(nums)
    mindiff = float('inf')
    totalsum = 0

    for i in range(len(nums)):
        low = i +1
        high = n - 1

        while (low < high):

            current_sum = nums[i] + nums[low] + nums[high]
            diff = abs(target - current_sum)

            if diff < mindiff:
                mindiff = diff
                totalsum = current_sum

            if current_sum == target:
                return current_sum
            elif current_sum < target:
                low += 1
            else:
                high -= 1
    return totalsum


nums = [-1,0,1,2,-1,-4]

result = threeSum(nums)






nums = [1,1,1,0]
target = -100

print("the elements which have a sum of minimum difference from {} is {}".format(target, threeSumClosest(nums, target)))