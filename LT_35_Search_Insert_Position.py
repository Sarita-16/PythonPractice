def searchInsert(nums, target):
    l = 0
    u = len(nums) - 1

    while l <= u:
        mid = (l + u) // 2
        if nums[mid] == target:
            return mid+1
        elif nums[mid] < target:
            l = mid + 1
        else:
            u = mid - 1

    return l+1


nums = list(map(int, input("Enter the numbers : ").split()))      # [1, 3, 5, 6]
target = int(input("Enter which value you want to search : "))       # 3
result = searchInsert(nums, target)
print("The index would be : ", result)
