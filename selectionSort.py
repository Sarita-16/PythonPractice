def selectionSort(list, len):
    for i in range(len-1):
        pivot = i
        for j in range(i+1, len):
            if list[pivot] > list[j]:
                pivot = j

        list[i], list[pivot] = list[pivot], list[i]

len = int(input("How many numbers you want to insert : "))
print("Enter the numbers : ")
list = []
for i in range (len):
    list.append(int(input()))

print(f'Before Selection Sort the list {list}')
selectionSort(list, len)
print(f'After Selection Sort the list is {list}')

'''
    Time Complexity = O(n^2)
'''