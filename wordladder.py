def ladderLength(beginWord, endWord, wordList):
    wordset = set(wordList)
    if endWord not in wordset:
        return 0
    queue = []
    queue.append(beginWord)
    level = 1
    letters = 'abcdefghijklmnopqrstuvwxyz'
    while len(queue) != 0:
        for word in queue:
            for j,char in enumerate(word):
                for l in letters:
                    if char == l:
                        continue
                    word_list = list(word)
                    word_list[j] = l
                    newword = ''.join(word_list)
                    # print("The new word is " + newword)
                    if newword == endWord: return level
                    if newword in wordset:

                        queue.append(newword)
                        wordset.remove(newword)
                    word_list[j] = char
                    word = ''.join(word_list)
            level +=1
    return 0
beginWord = "hit"
endWord = "doga"

wordList = ["hot", "dot", "dog", "lot", "log", "cog"]


print("There are {} transformations needed to transform {} into {} ".format(ladderLength(beginWord, endWord, wordList), beginWord, endWord))