from collections import  defaultdict
def groupAnagram(strs):
    anagram_dict = defaultdict(list)

    for string in strs:
        sorted_string = ''.join(sorted(string))
        anagram_dict[sorted_string].append(string)

    return list(anagram_dict.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = groupAnagram(strs)
print(result)
