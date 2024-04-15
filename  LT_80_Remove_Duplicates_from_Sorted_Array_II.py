def removeDuplicate(arr):
    if len(arr) <= 2:
        return arr
    count = 2
    for i in range(2, len(arr)):
        if arr[i] != arr[count - 2]:
            arr[count] = arr[i]
            count += 1
    return arr[:count]


n = int(input("How many numbers u want to insert: "))
print("Enter the numbers: ")
nums = []
for i in range(n):
    nums.append(int(input()))
result = removeDuplicate(nums)
print("After deleting duplicate elements the array look like : ", result)