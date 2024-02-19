def sumOfEvenOccurrence(matrix):
    elementCount = {}
    for row in matrix:
        for ele in row:
            if ele in elementCount:
                elementCount[ele] += 1
            else:
                elementCount[ele] = 1

    total_sum = 0
    for ele, c in elementCount.items():
        if c % 2 == 0:
            total_sum += ele * c

    return total_sum


size = int(input("Enter the size of Square Matrix : "))

matrix = []

print("Enter the elements : ")
for i in range(size):
    row = list(map(int, input().split()))
    matrix.append(row)

for row in matrix:
    for ele in row:
        print(ele, end="  ")
    print()

ans = sumOfEvenOccurrence(matrix)

print("Sum = ", ans)
