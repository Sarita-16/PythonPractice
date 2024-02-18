size = int(input("Enter the size of Square Matrix : "))

matrix = []

for i in range(size):
    col = []
    for j in range(size):
        col.append(int(input()))
    matrix.append(col)

for i in range(size):
    for j in range(size):
        print(matrix[i][j], end="  ")
    print()
