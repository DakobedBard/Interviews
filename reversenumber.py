
def reverseNumber(x):
    reversed_int = 0
    while x != 0:
        pop = x % 10
        x = x//10
        reversed_int = (reversed_int*10) + pop
    return reversed_int