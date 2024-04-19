def threeSum(nums):
    result = []
    nums.sort()

    for i in range(len(nums) - 2):
        # Avoid duplicates for i
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                # Avoid duplicates for left and right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return result

n = int(input("How many numbers you want to insert : "))
nums = []
for i in range(n):
    nums.append(int(input()))
print(threeSum(nums))
