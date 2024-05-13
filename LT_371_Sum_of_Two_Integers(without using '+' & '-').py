def getSum(num1, num2):
    mask = 0xffffffff   # mask to get last 32 bits
    while (num2 & mask) != 0:
        carry = (num1 & num2) << 1   # Shift the carry to the left by 1 bit
        num1 = num1 ^ num2      # Sum without considering the carry
        num2 = carry    # Assign the carry to num2 for the next iteration

    return (num1 & mask) if num2 > 0 else num1      # Ensures that the result is within the 32-bit range

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
print("Sum of both numbers without using '+' & '-' operators : ", getSum(num1, num2))