row = int(input("Enter the row : "))

print(f'{row}th row of Pascal Triangle is : ')
ans = 1
print(ans, end=" ")
for i in range(1, row):
    ans = ans * (row-i)
    ans = ans / i
    print(int(ans), end=" ")