def equalORNot(arr,sum):
    result_pairs = []
    for i in range(len(arr)):
        s = 0
        if arr[i] == sum:
            result_pairs.append(arr[i], )
        for j in range(i+1, len(arr)):

            s = arr[i] + arr[j]
            if s == sum:
                result_pairs.append((arr[i], arr[j]))

    print("The pair of given number : ", result_pairs)


n = int(input("Enter how many numbers you want to insert : "))
arr = []
print("Enter the elements : ")
for i in range(n):
    arr.append(int(input()))
sum = 7
equalORNot(arr,sum)
