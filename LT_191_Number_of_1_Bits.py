def hammingWeight(n):
    return (bin(n).count('1'))

n = int(input("Enter any number : "))
print("Hamming Weight of this", n, " is : ", hammingWeight(n))