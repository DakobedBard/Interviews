

def findMaxLength(nums):
    hashmap = {0:-1}
    maxlength = 0
    count = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        else:
            count +=1
        print("i {} and count {} ".format(i, count))
        if count in hashmap:
            maxlength = max(maxlength, i - hashmap[count])
        else:
            hashmap[count] = i
    return maxlength


nums = [0,0,1,0,0,0,1,1]
maxlength = findMaxLength(nums)