def isHappy(n):
    visited = set()
    while n != 1 and n not in visited:
        visited.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1


n = 19
print(isHappy(n))