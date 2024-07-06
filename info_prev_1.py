import math
def modulo(num):
    n = num
    lt = []
    for i in range(num-1, 0, -1):
        fact = math.factorial(i)
        count = i

        if fact % n == 1:
            for j in range(1, count+1):
                lt.append(j)
            return count, lt

    return -1

num = int(input("Enter the number : "))
length, list = modulo(num)
print(f"Biggest length of set {num} is {length}.")
print(f"Biggest list of set {num} is {list}.")