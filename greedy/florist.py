
def getMinimumCost(k, c):
    c.sort(reverse=True)
    cost = 0
    prev = 0
    for i in range(len(c)):
        cost += (prev+1) * c[i]
        if (i+1)%k ==0:
            prev +=1
    return cost
c = [1,3,5,7,9]

print("The minimum cost to buy these flowers is {}".format(getMinimumCost(3,c)))