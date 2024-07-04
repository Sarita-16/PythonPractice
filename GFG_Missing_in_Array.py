def missingNumber(n, arr):

    total_sum = n * (n+1) // 2
    actual_sum = sum(arr)

    missing_num = total_sum - actual_sum

    return  missing_num


n = int(input("Enter the number : "))
arr = list(map(int, input("Enter the numbers : ").split(" ")))
print("The missing number in an Array : ", missingNumber(n, arr))