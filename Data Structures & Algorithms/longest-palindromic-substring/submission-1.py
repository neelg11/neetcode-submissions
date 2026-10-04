class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        r = s[::-1]
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        best_len, best_end = 0, 0

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i-1] == r[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    L = dp[i][j]
                    # Only accept if the reversed match maps back to the same position
                    if L > best_len and i - L == n - j:
                        best_len, best_end = L, i

        return s[best_end - best_len : best_end]