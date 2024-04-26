from collections import Counter
def vadilAnagram(firstStr, secondStr):
    return Counter(firstStr) == Counter(secondStr)

firstStr = input("Enter first String : ")
secondStr = input("Enter second String : ")
print("Answer : ", vadilAnagram(firstStr, secondStr))