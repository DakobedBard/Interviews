def removeKdigits(num, k):
    size = len(num)
    if k == len(num):
        return "0"

    stack = []
    counter = 0
    while counter < size:
        while k > 0 and len(stack) > 0 and stack[-1] > num[counter]:
            stack.pop()
            k -= 1
        stack.append(num[counter])
        counter += 1

    print("k {}".format(k))
    while k > 0:
        print('len of stack {} '.format(len(stack)))
        stack.pop()
        k -= 1
    return stack
    sb = ''.join(stack)
    # while len(stack) > 0:
    #     current_char = stack.pop()
    #     sb += current_char
    # sb = sb[::-1]
    while len(sb) > 1 and sb[0] == '0':
        sb = sb[1:]

    return sb




num = "1432219"
k = 3
stack =  removeKdigits(num, k)
# print("the number {} after {}  deletions  that is minamized is {}".format(num, k, removeKdigits(num, k) ))