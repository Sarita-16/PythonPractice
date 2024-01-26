def binarySearch(list, left, right, key):
    mid = left + (right - left) // 2
    if right >= left:

        if list[mid] == key:
            return mid + 1

        elif list[mid] > key:
            return binarySearch(list, left, mid - 1, key)

        else:
            return binarySearch(list, mid + 1, right, key)
    else:
        return -1


len = int(input("How many number you want in the list : "))
print("Enter the numbers in ascending order : ")
list = []
for i in range(len):
    list.append(int(input()))

key = int(input("Which number you want to search : "))

result = binarySearch(list, 0, (len - 1), key)

if result == -1:
    print(f'Number is not found :(')
else:
    print(f'Number found at the location of {result}')

'''
    Time Complexity : O(log n)
'''
