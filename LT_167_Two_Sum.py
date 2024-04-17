def two_sum(numbers, target):
    left = 0  # Pointer for the leftmost element
    right = len(numbers) - 1  # Pointer for the rightmost element

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            # Indices are 1-indexed, so add 1 to each index
            return [left + 1, right + 1]
        elif current_sum < target:
            # If the sum is less than the target, move the left pointer to the right
            left += 1
        else:
            # If the sum is greater than the target, move the right pointer to the left
            right -= 1
    # If no solution is found, return an empty list
    return []

numbers = [1,2,3,4,4,9,56,90]
target = 8
print(two_sum(numbers, target))  # Output: [1, 2]
