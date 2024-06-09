def singleNumber(nums):
    ones, twos = 0, 0

    for num in nums:
        twos |= ones & num
        ones ^= num
        common_mask = ~(ones & twos)
        ones &= common_mask
        twos &= common_mask

    return ones

print(singleNumber([0, 1, 0, 1, 0, 1, 99]))
