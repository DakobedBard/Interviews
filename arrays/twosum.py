
def twosum(nums, target):
    complements = {}
    for i in range(len(nums)):
        if nums[i] in complements:
            return [complements[nums[i]], i]

        comp = target - nums[i]
        complements[comp] = i


nums = [2,7,11,15]
target = 9

print("The indices of the nums array which sum to {} are {} ".format(target, twosum(nums, target)))