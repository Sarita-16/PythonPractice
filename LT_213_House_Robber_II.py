def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])

    def rob_linear(houses):
        prev2, prev1 = 0, 0
        for amount in houses:
            current = max(prev1, prev2 + amount)
            prev2 = prev1
            prev1 = current
        return prev1

    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


nums = list(map(int, input("Enter the amounts : ").split()))
print("Total amount of robbing : ", rob(nums))
