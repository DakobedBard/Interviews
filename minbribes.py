


def minimumBribes(q):
    j = len(q) -1
    counter = 0
    for j in range(j,0,-1):
        if q[j] != (j+1):
            if(j-1) >= 0 and q[j-1] == j+1:
                counter +=1
                q[j],q[j-1] = q[j-1], q[j]
            elif(j-2) >= 0 and q[j-2] == j+1:
                counter +=2
                q[j-2] = q[j-1]
                q[j-1] = q[j]
                q[j] = j+1
            else:
                print("Too chaotic")
                return
    print(counter)


q = [2,1,5,3,4]
minimumBribes(q)