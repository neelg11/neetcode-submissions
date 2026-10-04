#GOOD SOLUTION, CHECK BOUNDARY and move inside
class Solution:
    def countSubstrings(self, s: str) -> int:
        n, res = len(s), 0
        dp = [ [False]*n for _ in range(n)]
        for i in range(n):
            for j in range(0,i+1):
                if s[i]==s[j]:
                    if( i-j<=2 or dp[i-1][j+1]):
                        dp[i][j] = True
                        res+=1
        return res
                    
