def canJump(nums):
    max_reachable = 0
    for i, num in enumerate(nums):
        if i > max_reachable:
            return False
        max_reachable = max(max_reachable, i + num)
    return max_reachable >= len(nums) - 1

nums = list(map(int, input("Enter the numbers : ").split()))
print(canJump(nums))

