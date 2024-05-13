def countBits(n):
    ans = [0] * (n+1)
    for i in range(n+1):
        ans[i] = bin(i).count('1')
    return ans

n = int(input("Enter any number : "))
print("List of each number of 1's in the binary representation : ", countBits(n))