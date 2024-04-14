def removeDuplicate(nums):
    k = []
    for i in range(len(nums)-1, -1, -1):
        if nums[i] in k:
            nums.remove(nums[i])
        else:
            k.append(nums[i])
    count = len(k)
    return sorted(k)

n = int(input("How many numbers u want to insert: "))
print("Enter the numbers: ")
nums = []
for i in range(n):
    nums.append(int(input()))

r = removeDuplicate(nums)
print("After deleting duplicate elements the array look like : ", r)