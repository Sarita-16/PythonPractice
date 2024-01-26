def linearSearch(list, size, key):
    for i in range (size):
        if list[i] == key:
            return (i + 1)
    return -1

size = int(input("How many number you want to insert in any list : "))
print("Enter the numbers : ")
list = []
for i in range (size):
    list.append(int(input()))

key = int(input("Which number you want to searched : "))

result = linearSearch(list, size, key)

if result == -1:
    print("Number is not found :(")
else:
    print(f'The number is found :) at the position of {result}.')






'''
    Time Complexity : O(n)
'''