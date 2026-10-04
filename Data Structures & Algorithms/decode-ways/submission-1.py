class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1]*len(s)
        def dfs(i):
            if(i==len(s)):
                return 1
            if(i>len(s) or s[i]=='0'):
                return 0
            if dp[i]!=-1:
                return dp[i]
            res = dfs(i+1)
            if(s[i]=='1'):
                res+=dfs(i+2)
            if(s[i]=='2' and i+1<len(s) and s[i+1] < '7'):
                res+=dfs(i+2)
            dp[i] = res
            return dp[i]

        return dfs(0)
