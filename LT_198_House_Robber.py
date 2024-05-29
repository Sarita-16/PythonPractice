def rob(nums):
    if not nums:
        return 0
    elif len(nums) == 1:
        return nums[0]

    prev1, prev2 = max(nums[0], nums[1]), nums[0]
    print(prev1, prev2)

    for i in range(2, len(nums)):
        current = max(nums[i] + prev2, prev1)
        prev2, prev1 = prev1, current

    return prev1


nums = list(map(int, (input("Enter the amount of money : ").split())))
print("Total amount of robbing : ", rob(nums))