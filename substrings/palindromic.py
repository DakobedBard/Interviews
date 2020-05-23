def palindromicsubstring(s):
    if not s and len(s) < 1: return ""
    start = 0
    end = 0
    for i in range(len(s)):
        len1 = explandFromMiddle(s, i, i)
        len2 = explandFromMiddle(s, i, i+1)

        print("len1 {} and len2 {} ".format(len1, len2))
        len12 = max(len1, len2)
        if len12 > end - start:
            start = i - ((len12 - 1) //2)
            end = i + (len12//2)

    return s[start:end+1]

def explandFromMiddle(s, left, right):
    if s == None or left > right:
        return 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -=1
        right +=1
    return right - left -1


s = "cbbddbbca"

print("The longest palindrom is {}".format(palindromicsubstring(s)) )