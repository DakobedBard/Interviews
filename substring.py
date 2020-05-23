
'''
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

'''


def lengthOfLongestSubstring(s):
    if s == None or len(s)==0:
        return 0
    if len(s) ==1:
        return 1
    left = 0
    right =1
    maxlength = 0
    hashmap = {s[0]}
    while right < len(s):
        right_val = s[right]
        left_val = s[left]
        if right_val not in hashmap:
            hashmap.add(right_val)
            maxlength = max(len(hashmap), maxlength)
            right +=1
        else:
            hashmap.remove(left_val)
            left +=1
    maxlength = max(len(hashmap), maxlength)
    return maxlength



s = "bacdabcdef"
print("The length of the longest substring is {} and it should be {}".format(lengthOfLongestSubstring(s),6))
#
s= "abcabcbb"
print("The length of the longest substring is {} and it should be {}".format(lengthOfLongestSubstring(s), 3))

s= "abba"
print("The length of the longest substring is {} and it should be {}".format(lengthOfLongestSubstring(s), 2))