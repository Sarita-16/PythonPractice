def wordPattern(pattern, s):
    words = s.split()
    # print(words)

    if len(pattern) != len(words):
        return False

    dictionary = {}
    mapWords = set()

    for i, j in zip(pattern, words):
        if i in dictionary:
            if dictionary[i] != j:
                return False

        else:
            if j in mapWords:
                return False
            dictionary[i] = j
            mapWords.add(j)

    return True


pattern = input("Enter any pattern : ")     # abba
s = input("Enter any String : ")            # dog cat cat dog
print("The word pattern is : ", format(wordPattern(pattern, s)))
