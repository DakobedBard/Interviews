def whatFlavors(cost, money):
    complements = {}
    for i,c in enumerate(cost):
        print(complements)
        if c in complements:
            print("c {}".format(c))
            return (complements[c]+1,i+1)
        complements[money - c] = i



cost = [1,4,5,3,2]
print("The indices are {} ".format(whatFlavors(cost, 4)))
cost = [2,2,4,3]
print("The indices are {} ".format(whatFlavors(cost, 4)))