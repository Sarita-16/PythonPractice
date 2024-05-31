def combinationSum3(k, n):
    def backtrack(start, k, n, path, res):
        if k == 0 and n == 0:
            res.append(path)
            return
        if k == 0 or n < 0:
            return
        for i in range(start, 10):
            backtrack(i + 1, k - 1, n - i, path + [i], res)

    res = []
    backtrack(1, k, n, [], res)
    return res


k = int(input("Combinations of numbers : "))
n = int(input("Enter the number : "))
print(combinationSum3(k, n))
