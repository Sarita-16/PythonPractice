# Set matrix zero
def zeroMatrix(matrix, row, col):
    col0 = 1
    # Step1: Traverse the matrix and mark 1st row & col accordingly:
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0

    # Step 2: Mark with 0 from (1,1) to (n-1, m-1)
    for i in range(1, row):
        for j in range(1, col):
            if matrix[i][j] != 0:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

    # Step 3: Finally mark the 1st col & then 1st row
    if matrix[0][0] == 0:
        for j in range(col):
            matrix[0][j] = 0
    if col0 == 0:
        for i in range(row):
            matrix[i][0] = 0

    return matrix


# Creating the matrix
def createMatrix(row, col):
    matrix = []
    for i in range(row):
        row = []
        for j in range(col):
            ele = int(input())
            row.append(ele)
        matrix.append(row)
    return matrix


# Matrix input from user
row = int(input("Enter the numbers of row : "))
col = int(input("Enter the numbers of column: "))
print("Enter the numbers : ")
matrix = createMatrix(row, col)

# Priting the matrix
print("Matrix : ", )
for i in range(row):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print()

# Print the resulting matrix
print("The final matrix : ")
ans = zeroMatrix(matrix, row, col)
for i in range(row):
    for j in range(col):
        print(ans[i][j], end=" ")
    print()

