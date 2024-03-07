n = int(input("Enter how many numbers you want to insert: "))
arr = []
print("Enter the numbers: ")
for i in range(n):
    arr.append(int(input()))

print(arr)

min = float('inf')
secondMin = float('inf')
locMin = 0
for i in range(n):
    if min > arr[i]:
        secondMin = min
        min = arr[i]

    elif (secondMin > arr[i] and min != arr[i]):
        secondMin = arr[i]
        locMin = i + 1

print("Second Smallest number is : ", secondMin, ", at the location : ", locMin)


max = float('-inf')
secondMax = float('-inf')
locMax = 0
for i in range(n):
    if max < arr[i]:
        secondMax = max
        max = arr[i]

    elif (secondMax < arr[i] and max != arr[i]):
        secondMax = arr[i]
        locMax = i + 1

print("Second Largest number is : ", secondMax, ", at the location : ", locMax)
