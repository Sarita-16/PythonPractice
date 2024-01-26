def bubbleSort(list, len):
    for i in range (len-1):
        for j in range (0, len-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

len = int(input("How many numbers you want to insert : "))
print("Enter the numbers : ")
list = []
for i in range (len):
    list.append(int(input()))

print(f"Before sorting Array : {list}")

bubbleSort(list, len)

print(f"After sorting Array : {list}")


'''
    Time Complexity : O(n^2)
'''