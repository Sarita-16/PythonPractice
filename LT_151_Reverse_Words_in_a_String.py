def reverseWords(s):
    revS = " ".join(reversed(s.split()))
    return revS

s = input("Enter any String : ")
print("Reverse the order of the words : ", reverseWords(s))