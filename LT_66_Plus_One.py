def plusOne(arr):
    # Array to Numbers
    number = 0
    for i in (arr):
        number = (number * 10) + i

    # Plus One
    number = number + 1

    # Numbers to Array/ List
    d = [int(l) for l in str(number)]

    return d


arr = list(map(int, input("Enter numbers : ").split()))
print("The array : ", arr)
print("Plus One : ", plusOne(arr))