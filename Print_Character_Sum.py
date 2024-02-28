word = input("Enter the letters by space : ")

# Splitting the input string into a list of values
values = word.split()

sum = 0
for i in range(len(values)):
    sum = sum + ord(values[i])

print(sum)