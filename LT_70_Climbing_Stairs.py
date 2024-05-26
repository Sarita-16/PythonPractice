def climbStairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    first = 1
    second = 2

    for i in range(3, n + 1):
        third = first + second
        first = second
        second = third

    return second

n = int(input("Enter the number of steps of staircase : "))
print(f"There are {climbStairs(n)} ways to climb to the top of the staircase.")

