


def largestRectangle(h):
    l = 0
    r = len(h) -1
    maxarea = len(h)
    while l < r:
        if min(h[l], h[r]) * (r-l+1) >= maxarea:
            print("h[l] {} h[r] {} (r-l) {} ".format(h[l], h[r], r-l+1))
            maxarea =  min(h[l], h[r]) * (r-l+1)
        if h[l] < h[r]:
            l +=1
        else:
            r -= 1
    return maxarea

h = [1,2,3,4,5]

print("The maximum area is " + str(largestRectangle(h)))