def canConstruct(ransomNote, magazine):
    count = ''
    for i in ransomNote:
        for j in magazine:
            if i == j:
                count += i
                magazine = magazine.replace(j, '', 1)
                break
    print("The common strings : ", count)
    if count == ransomNote:
        return True
    else:
        return False


ransomNote = input("Enter first string : ")
magazine = input("Enter second string : ")
result = canConstruct(ransomNote, magazine)
print(result)






