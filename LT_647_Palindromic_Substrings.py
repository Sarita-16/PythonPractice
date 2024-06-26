def countSubstrings(s: str) -> int:
    n = len(s)
    count = 0
    dp = [[False] * n for _ in range(n)]

    # Single character substrings are palindromes
    for i in range(n):
        dp[i][i] = True
        count += 1

    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            count += 1

    # Check for substrings of length greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                count += 1

    return count

# Test cases
print(countSubstrings("abc")) # Output: 3
print(countSubstrings("aaa")) # Output: 6
