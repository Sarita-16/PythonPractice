def searchRange(nums, target):
    first, last = -1, -1
    for i in range(len(nums)):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    return [first, last]

# Test the function with the examples
nums = list(map(int, input("Enter the numbers : ").split()))
target = int(input("Enter the Target : "))
print("First & Last position of element in a Array : ", searchRange(nums, target))