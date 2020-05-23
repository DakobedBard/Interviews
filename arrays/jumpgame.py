#
#
# def canJump(nums):
#
#     stack = [(nums[0],0)]
#     while len(stack) >0:
#         print(stack)
#         current_val, index = stack.pop()
#         if current_val+ index >= len(nums) -1:
#             return True
#         for i in range(1,current_val+1):
#             stack.append((nums[index+i], index+i))
#
#     return False


def canJump(nums):
    lastGoodIndexPosition = len(nums) -1
    for i in range(len(nums)-1,-1,-1):
        if i + nums[i] >= lastGoodIndexPosition:
            lastGoodIndexPosition = i
    if lastGoodIndexPosition ==0:
        return True
    return False



nums1 = [2,3,1,1,4]
nums2 = [3,2,1,0,4]
nums3 = [2,5,0,0]
print("I can make it to the end of this array {} ".format(canJump(nums1)))
print("I can make it to the end of this array {} ".format(canJump(nums2)))
print("I can make it to the end of this array {} ".format(canJump(nums3)))