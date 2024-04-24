def gameOfLife(board):
    newBoard = [[0] * len(board[0]) for i in range(len(board))]  # Initialize new board

    for i in range(len(board)):
        for j in range(len(board[0])):
            count = 0
            # Define the neighbors' relative positions
            neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
            for dx, dy in neighbors:
                x, y = i + dx, j + dy
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 1:
                    count += 1

            # Apply rules
            if board[i][j] == 1:
                if count == 2 or count == 3:
                    newBoard[i][j] = 1
                else:
                    newBoard[i][j] = 0
            else:
                if count == 3:
                    newBoard[i][j] = 1
                else:
                    newBoard[i][j] = 0

    return newBoard


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
print("The board : ")
for i in range(len(board)):
    print(board[i])
result = gameOfLife(board)
print("After applying GAME OF LIFE rule the board looks like : ")
for i in range(len(result)):
    print(result[i])
