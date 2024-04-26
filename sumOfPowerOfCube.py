m = int(input("Enter 1st number : "))
n = int(input("Enter 2nd number : "))

sum = 0

if m < n:
    a = m
    b = n
else:
    a = n
    b = m

for i in range(a, b+1):
    sum = sum + (i*i*i)

print("Sum of power of cube : ", sum)