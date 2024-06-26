def longestCommonPrefix(strs):
    if not strs:
        return ""

    strs.sort()

    prefix = ""
    for i in range(len(strs[0])):
        if strs[0][i] == strs[-1][i]:
            prefix += strs[0][i]
        else:
            break

    return prefix


strs = ["flower", "flow", "flight"]
print("Longest common prefix:", longestCommonPrefix(strs))



