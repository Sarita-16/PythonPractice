def searchMatrix(matrix, target):
    row = len(matrix)
    col = len(matrix[0])

    for i in range(row):
        for j in range(col):
            if target == matrix[i][j]:
                return True

    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
result = searchMatrix(matrix, target)
print("The Result : ", result)

