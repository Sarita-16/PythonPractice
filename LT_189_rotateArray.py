"""
def rotateArray(nums, k):
    for i in range(k):
        last = len(nums)-1
        first = 0
        t = nums[last]
        for j in range(len(nums)-1, -1, -1):
            nums[j] = nums[j-1]
        nums[first] = t
    return nums

nums = [1,2,3,4,5,6,7]
k = 3
result = rotateArray(nums, k)
print(result)
"""




# ShortCut
def rotateArray(nums, k):
    # If k is greater than the length of nums, take the modulo to avoid unnecessary rotations
    k = k % len(nums)
    # Rotate the array by slicing and concatenating
    nums[:] = nums[-k:] + nums[:-k]
    return nums
nums1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 8
print(rotateArray(nums1, k1))  # Output: [5, 6, 7, 1, 2, 3, 4]

