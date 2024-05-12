def missingNumber(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return total_sum - actual_sum


nums = list(map(int, input("Enter the numbers : ").split()))
print("Missing Number :", missingNumber(nums))
