def removeDuplicatesK(S, k ):
    stack = [0] * len(S)
    i = 0
    for j in range(len(S)):
        current_char = S[j]
        hasKDuplicates = False
        consecutive_characters = 1
        while consecutive_characters <= k :
            if j+consecutive_characters >= len(S):
                hasKDuplicates = False
                break
            if S[j+consecutive_characters] == current_char:
                consecutive_characters +=1
                if consecutive_characters == k:
                    print("I found {} duplicates and the char is {}".format(k,S[j] ))
                    hasKDuplicates = True
                    break
            else:
                hasKDuplicates = False
                break

        if i >0 and hasKDuplicates:
            i -=1
        else:
            print("I am adding a character to the stack {}".format(current_char))
            stack[i] = current_char
            i+=1
    newstring =''
    return newstring.join(stack[:i])



def removeDuplicates(S):
    stack = [0] * len(S)
    i = 0
    for j in range(len(S)):
        current_char = S[j]
        if i >0 and stack[i-1] == current_char:
            i -=1
        else:
            stack[i] = current_char
            i+=1
    newstring =''
    return newstring.join(stack[:i])
s = "abbaca"
r= removeDuplicates(s)



s = "deeedbbcccbdaa"
k = 3

print("The outpyut string after elements w/ more than {} duplicates have been removed from {}  is {}".format(k, s,  removeDuplicatesK(s, k)))
