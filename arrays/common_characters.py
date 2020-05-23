
def commonChars(A):
    listOfSets = []
    listOfWordArrs = []

    for word in A:
        wordArr = [x for x in word]
        listOfWordArrs.append(wordArr)
        listOfSets.append(set(wordArr))
    elemIntersections = set.intersection(*listOfSets)
    result = []

    for elem in list(elemIntersections):
        toAdd = set()

        for wordAsList in listOfWordArrs:
            toAdd.add(wordAsList.count(elem))

        toAddMin = min(toAdd)

        for y in range(toAddMin):
            result.append(elem)

    return result

words = ["bella", "label","roller"]

sets = commonChars(words)