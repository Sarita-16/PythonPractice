def removeEle(nums, val):
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1
    return count

nums = []
l = int(input("How many numbers you want to insert : "))
print("Enter the elements: ")
for i in range(l):
    nums.append(int(input()))
val = int(input("Which element you want to remove: "))
result = removeEle(nums, val)
print(result)