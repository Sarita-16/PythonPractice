def rotateImage(matrix):

    '''
    row = len(matrix)
    col = row
    transposed = []
    for j in range(col):
        temp = []
        for i in range(row):
            temp.append(matrix[i][j])
        transposed.append(temp)
    rotated = []
    for r in transposed:
        rotated.append(r[::-1])
    return rotated
    '''

    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()

    return matrix


matrix = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(matrix)):
    print(matrix[i])
result = rotateImage(matrix)
print("Rotate 90° Clockwise : ")
for i in range(len(result)):
    print(result[i])