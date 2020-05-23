


def isSubsequence(s, t):
    if len(s) ==0:
        return True
    spointer = 0
    tpointer = 0

    while tpointer < len(t):
        if t[tpointer] == s[spointer]:
            spointer+=1
        tpointer +=1
    if spointer == len(s):
        return True
    return False

s = "abc"
t = "abhgde"



print(" s {} is a subsequence of t {}  {} ".format(s, t, isSubsequence(s,t)))