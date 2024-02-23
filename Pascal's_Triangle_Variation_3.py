def nCr(row, col):
    ans = 1
    # calculating nCr:
    for i in range(col):
        ans = ans * (row - i)
        ans = ans // (i + 1)
    return int(ans)

def pascalTriangle(row):
    ans=[]
    # Store the entire pascal's triangle:
    for i in range(1, row+1):
        tempList = []
        for j in range(1, i+1):
            tempList.append(nCr(i-1, j-1))
        ans.append(tempList)
    return ans


row = int(input("Enter the ROW : "))
print(f'Pascal Triangle upto {row}th row : ')
result = pascalTriangle(row)
for i in result:
    for ele in i:
        print(ele, end=" ")
    print()
