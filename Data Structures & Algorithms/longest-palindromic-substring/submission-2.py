class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res_start, res_len = 0, 0
        dp = [ [False]*n for _ in range(n)]
        for i in range(n):
            for j in range(0,i+1):
                if s[i]==s[j]:
                    if( i-j<=2 or dp[i-1][j+1]):
                        dp[i][j] = True
                        if i-j+1>res_len:
                            res_len = i-j+1
                            res_start = j
        return s[res_start: res_start+res_len]
                    
