def uniquePaths(m, n):
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]

m, n = map(int, input("Enter the bottom-right corner, m and n separated by space: ").split())
print(uniquePaths(m, n))
