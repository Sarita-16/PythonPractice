def reverseBits(n):
    ans = 0
    for i in range(32):
        ans <<= 1
        ans = ans | (n & 1)
        n >>= 1
    return ans

n = input("Enter 32 bits unsigned integer : ")
n = int(n, 2)   # Convert the binary string to an integer
print("Reverse bits : ", reverseBits(n))