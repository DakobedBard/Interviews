def findShortestSubArray(nums):

    hashmap = {}
    firstSeen = {}
    degree = 0
    min_length = 0
    for i, num in enumerate(nums):
        if num in hashmap:
            hashmap[num]  += 1
        else:
            firstSeen[num] = i
            hashmap[num] =1
        if hashmap[num] > degree:
            degree = hashmap[num]
            min_length = i - firstSeen[num] + 1
        elif hashmap[num] == degree:
            min_length = min(min_length, i - firstSeen[num] + 1)
    return  min_length
arr = [1,2,2,3,1,2]
print("The minium length of a subarry with same degree is {}".format(findShortestSubArray(arr)))