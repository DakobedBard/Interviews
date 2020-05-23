



def countCharacters(words, chars):
    char_counts = [0] * 26
    for char in chars:
        char_counts[ord(char)-ord('a')] +=1
    good_words_sum = 0
    for word in words:
        word_char_counts = [0] * 26
        for char in word:
            word_char_counts[ord(char) - ord('a')] += 1
        if all([zipped[0] <= zipped[1] for zipped in zip(word_char_counts, char_counts)]):
            good_words_sum += len(word)

    return good_words_sum


words = ["cat","bt","hat","tree"]
chars = "atach"

print("The good words sum of these words is {}".format(countCharacters(words, chars)))