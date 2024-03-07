n = int(input("Enter how many numbers you want: "))
arr = []
print("Enter the numbers : ")
for i in range(n):
    arr.append(int(input()))

print(arr)

min = arr[0]
for i in range(1, n):
    if min > arr[i]:
        min = arr[i]
        loc = i+1

print("Smallest element in an Array is  : ", min, ", at the location : ", loc)