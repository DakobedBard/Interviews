def isPalindrome(x):
    if x ==0:
        return True
    if x <0 or x %10 == 0:
        return False
    reversed_int = 0
    while x > reversed_int:
        pop = x % 10
        x = x//10
        reversed_int = (reversed_int*10) + pop
    if x == reversed_int or x == reversed_int//10:
        return True
    else:
        return False

print("The number {} is a palindrome {}".format(121, isPalindrome(121)))