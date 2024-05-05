def findMin(nums):
    min = nums[0]
    for i in range(1, len(nums)):
        if min > nums[i]:
            min = nums[i]

    return min

nums = list(map(int, input("Enter numbers : ").split()))
result = findMin(nums)
print("Minimum number among the list : ", result)