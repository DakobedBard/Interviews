'''
Given two strings, determine if they share a common substring. A substring may be as small as one character.

For example, the words "a", "and", "art" share the common substring
. The words "be" and "cat" do not share a substring.

'''


import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):

    s1d = {}
    s2d = {}
    for char in s1:
        s1d[char] =1
        pass
    for char in s2:
        s2d[char] =1
    for char in s1d.keys():
        if char in s2d.keys():
            return 'YES'
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()
        s2 = input()

        result = twoStrings(s1, s2)
        fptr.write(result + '\n')

    fptr.close()
