def palindrome(n):
    originalNoStr = str(n)
    reverseNoStr = originalNoStr[::-1]

    if originalNoStr == reverseNoStr:
        return True
    else:
        return False

    # By Mathematical
    """x = n
    sum = 0
    while x > 0:
        r = x % 10
        sum = (sum * 10) + r
        x = x // 10
    if n == sum:
        return True
    else:
        return False"""


n = int(input("Enter any number : "))
print("The number is Palindrome : ", palindrome(n))