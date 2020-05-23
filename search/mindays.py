import time
from math import ceil
def mindays(machines, goal):

    nmachines = 0

    fastestmachine = min(machines)
    slowestmachine = max(machines)
    lowerbound = ceil(goal *(fastestmachine/len(machines)))
    upperbound = ceil(goal * (slowestmachine/len(machines)))

    print(lowerbound)
    print(upperbound)

    while lowerbound<=upperbound:
        s = 0
        mid = int((lowerbound+upperbound)/2)
        print("mid {} lowerbound {} upperbound  {} ".format(mid, lowerbound, upperbound))
        for m in machines:
            s  += int(mid/m)
        print("nmachines {} ".format(s))
        if s > goal:

            if upperbound == mid:
                return upperbound
            upperbound = mid
        else:
            if lowerbound == mid:
                return upperbound
            lowerbound = mid
        time.sleep(1)
    return lowerbound




print("The min days is " + str(mindays([2,5],5)))