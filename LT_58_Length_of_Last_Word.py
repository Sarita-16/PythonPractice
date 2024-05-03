def lengthOfLastWord(s):
    w = s.split()
    last_word = w[-1]
    return len(last_word)

s = input("Enter sentence :  ")
result = lengthOfLastWord(s)
print("Length of last word of this sentence : ", result)