def buddyStrings(A,B):
    if len(A) != len(B): return False

    if A == B:
        unique_chars = set()
        for c in A:
            unique_chars.add(c)
        if len(unique_chars) < len(A):
            return True
        else:
            return False

    diff = []
    for i, c in enumerate(A):
        if c != B[i]:
            diff.append(i)


    if len(diff) == 2 and A[diff[0]] == B[diff[1]] and A[diff[1]] == B[diff[0]]:
        return True
    else:
        return False
a = "abc"
b = "abc"
print("The strings {} and {} are buddies {} ".format(a, b, buddyStrings(a,b)))