import math
def trailingZeroes(n):
    factorail_of_n = math.factorial(n)
    c = 0
    while factorail_of_n % 10 == 0:
        c += 1
        factorail_of_n //= 10

    return c

n = int(input("Enter any number : "))
print("Factorail Trailing Zeroes of ", n, " is : ", trailingZeroes(n))