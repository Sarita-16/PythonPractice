def fibonacci(len):
    if len <= 1:
        return (len)
    else:
        return (fibonacci(len-1) + fibonacci(len-2))

len = int(input("Enter the number : "))

print("The series : ")

if len <= 0:
    print("Enter Valid Number. ")
else:
    for i in range(len):
        print(fibonacci(i))

