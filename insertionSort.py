def insertionSort(list, len):
    for i in range(1, len):

        temp = list[i]
        j = i - 1

        while j >= 0 and temp < list[j]:
            list[j + 1] = list[j]
            j -= 1

        list[j + 1] = temp


len = int(input("How many numbers you want to insert : "))
print("Enter the numbers : ")
list = []
for i in range(len):
    list.append(int(input()))

print(f"Before ascending the list {list}")

insertionSort(list, len)

print(f"After ascending the list {list}")

'''
    Time Complexity = O(n^2)
'''
