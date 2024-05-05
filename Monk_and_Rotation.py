def rotate_array(arr, positions):
    n = len(arr)
    positions %= n
    return arr[-positions:] + arr[:-positions]


T = int(input("Enter How many test cases you want : "))

for _ in range(T):
    N, K = map(int, input("Enter how many numbers you want in array & enter the number of steps of rotation by space : ").split())
    print("Enter the numbers : ")
    A = list(map(int, input().split()))

    # Rotate the array
    rotated_arr = rotate_array(A, K)


    print("The Output : ", *rotated_arr)
