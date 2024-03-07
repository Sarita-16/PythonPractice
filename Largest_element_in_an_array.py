n = int(input("How many numbers you want to insert : "))
arr = []
print("Enter the elements : ")
for i in range(n):
    arr.append(int(input()))

print(arr)

max = arr[0]
loc = 0
for i in range(1, n):
    if max < arr[i]:
        max = arr[i]
        loc = i+1

print("Largest element in an Array is : ", max, ", at the location : ", loc)
