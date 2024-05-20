import math
def minSubArrayLen(target, nums):
    count = math.inf
    sum, start = 0, 0

    for i in range(len(nums)):
        sum = sum + nums[i]
        while sum >= target:
            count = min(count, i - start + 1)
            sum -= nums[start]
            start += 1

    return 0 if count == math.inf else count

target = 7
nums = [2, 3, 1, 2, 4, 3]
print("Min Sub Array Len : ", minSubArrayLen(target, nums))
