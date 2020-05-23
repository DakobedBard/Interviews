'''

Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.
'''


def longestWord(words):
    wordset= set(words)
    ans = ''
    longest = 0
    for word in wordset:
        if len(word) > len(ans) or len(word) == len(ans) and word < ans:
            if all([word[:k] in wordset for k in range(1,len(word))]):
                ans = word

    return ans

words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]