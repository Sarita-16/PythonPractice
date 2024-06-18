def singleNumber(nums):
    ones, twos = 0, 0

    for num in nums:
        twos |= ones & num
        ones ^= num
        common_mask = ~(ones & twos)
        ones &= common_mask
        twos &= common_mask

    return ones

nums = list(map(int, input("Enter numbers : ").split()))
print(singleNumber(nums))
