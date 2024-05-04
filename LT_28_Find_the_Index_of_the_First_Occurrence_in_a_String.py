def strStr(haystack, needle):
    nLen = len(needle)

    for i in range(len(haystack)):
        if needle == haystack[i:nLen]:
            return i+1
        nLen += 1

    return -1

haystack = input("Enter any string : ")
needle = input("Enter any subString : ")
result = strStr(haystack, needle)
print("The index : ", result)