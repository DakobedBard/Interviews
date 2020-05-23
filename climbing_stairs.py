

def minCostClimbingStairs(cost):

    for i in range(2, len(cost)):
        cost[i] += min(cost[i-1], cost[i-2])
    return min(cost[len(cost)-1], cost[len(cost)-2])


cost = [10,15,20]
print("The minimum cost is {}".format(minCostClimbingStairs(cost)))



cost = [0,0,1,1]
print("The minimum cost is {}".format(minCostClimbingStairs(cost)))