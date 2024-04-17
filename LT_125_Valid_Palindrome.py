def is_palindrome(s):
    st = ''.join(i.lower() for i in s if i.isalnum())
    return st == st[::-1]


# Example usage:
s = input("Enter string : ")
print(is_palindrome(s))
