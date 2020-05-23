def luckBalance(k, contests):
    contests = sorted(contests, key=lambda l: l[0])
    print(contests)
    tluck, nimportant =  [sum(i) for i in zip(*contests)]
    c = 0
    index = 0
    while c < nimportant-k and index < len(contests):
        if contests[index][1] == 1:
            tluck -= 2* contests[index][0]
            c +=1
        index +=1
    return tluck

contests = [[5,1],[2,1],[1,1],[8,1],[10,0],[5,0]]
print("The total luck is {}".format(luckBalance(3, contests)))


