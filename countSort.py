""" countSort """
def countSort(lst, length, mini, maxi):
    rangee = maxi - mini + 1
    ans = [0] * length

    frequencyList = [0] * rangee

    for i in range(length):
        frequencyList[lst[i] - mini] += 1

    for i in range(1, rangee):
        frequencyList[i] += frequencyList[i - 1]

    for i in range(length - 1, -1, -1):
        position = frequencyList[lst[i] - mini] - 1
        ans[position] = lst[i]
        frequencyList[lst[i] - mini] -= 1

    for i in range(length):
        lst[i] = ans[i]

    print(f"After Sorting the List : {lst}")


""" Find Min & Max"""
def findMinMax(length, lst):
    """ list.sort()
        print(f"Min : {list[0]}")
        print(f"Max : {list[-1]}")"""

    """ print(min(list))
       print(max(list))"""

    mini = lst[0]
    maxi = lst[0]
    for i in range(1, length):
        if lst[i] < mini:
            mini = lst[i]
        if lst[i] > maxi:
            maxi = lst[i]
    return mini, maxi


length = int(input("How many numbers you want to insert: "))
lst = []
for i in range(length):
    lst.append(int(input()))

print(f"Before Sorting the list : {lst}")

mini, maxi = findMinMax(length, lst)
print(f" Min : {mini} & Max : {maxi}")

countSort(lst, length, mini, maxi)

