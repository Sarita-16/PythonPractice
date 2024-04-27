def sumStr(s):
    sum = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            subString = s[i:j]
            sum = sum + int(subString)
    return sum

s = input("Enter any input String : ")
result = sumStr(s)
print("Sum of all possible contiguous character from a string : ", format(result))