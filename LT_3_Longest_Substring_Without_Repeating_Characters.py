def lengthOfLongestSubstring(s):
    maxLength = 0
    charSet = set()
    l = 0

    for r in range(len(s)):
        if s[r] not in charSet:
            charSet.add(s[r])
            maxLength = max(maxLength, r - l + 1)
        else:
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])

    return maxLength


s = "abcabcbb"
print("Length Of Longest Substring : ", lengthOfLongestSubstring(s))

