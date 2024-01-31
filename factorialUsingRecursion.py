def factorial(number):
    if number == 0 or number == 1:
        return 1

    else:
        return (number * factorial(number-1))

number = int(input("Enter any number : "))

answer = factorial(number)

print(f"Factorial of {number} is {answer} .")