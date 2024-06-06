import functools

def singleNumber(nums):
    number = 0
    for i in nums:
        number ^= i

    return number

nums = list(map(int, input("Enter the numbers : ").split()))
print("Single element in the list is : ", singleNumber(nums))