
def findJudge(N, trust):
    count = [0] * (N+1)
    for i,t in enumerate(trust):
        count[t[0]] -= 1
        count[t[1]] +=1
    for i,c in enumerate(count):
        if c == N-1:
            return i

    return -1

trust = [[1,2]]
judge = findJudge(2,trust)