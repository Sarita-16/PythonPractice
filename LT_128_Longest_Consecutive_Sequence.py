def longest_consecutive(nums):
    if not nums:
        return 0

    num_set = set(nums)
    max_length = 0

    for i in num_set:
        if i - 1 not in num_set:
            current_num = i
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length


nums = list(map(int, input("Enter numbers : ").split()))
print("The longest consecutive sequence : ", longest_consecutive(nums))
