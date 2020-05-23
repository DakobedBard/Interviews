import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    freqs = {}
    results = []
    for query in queries:
        if query[0] == 1:
            if query[1] not in freqs.keys():
                freqs[query[1]] = 1
            else:
                freqs[query[1]] +=1
        if query[0] == 2:
            if query[1] in freqs.keys():
                freqs[query[1]] -= 1

        if query[0] == 3:
            print("query 3 " + str(query[1]))
            r = 0
            for (k,v) in freqs.items():
                if v == query[1]:
                    r = 1
            results.append(r)
    return results
queries = [[1,5],[1,6],[3,2],[1,10],[1,10],[1,10],[1,6],[2,5],[3,2]]
freqQuery(queries)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
