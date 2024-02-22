'''
    5 C 2 = (5!)/((2!) * (5-2)!)
'''
r = int(input("Enter the number of ROW : "))
c = int(input("Enter the number of COLUMN : "))

row = r-1
col = c-1
res = 1
for i in range(col):
    res = res * (row-i)
    res = res / (i+1)

print(f'The number at the position {(r, c)} is : {int(res)}')