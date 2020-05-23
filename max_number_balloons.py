def maxNumberOfBalloons(text):
    char_counts = [0] * 26
    for char in text:
        char_counts[ord(char) -ord('a')] +=1

    minchar = char_counts[ord('b')-ord('a')]
    minchar = min(minchar, char_counts[ord('a')-ord('a')])
    minchar = min(minchar, char_counts[ord('l')-ord('a')]//2)
    minchar = min(minchar, char_counts[ord('o')-ord('a')]//2)
    minchar = min(minchar, char_counts[ord('n')-ord('a')])
    return minchar

text =  "loonbalxballpoon"
print("The minimum number of times the word balloon can be made from the letters in {}  is {} ".format(text, maxNumberOfBalloons(text)))