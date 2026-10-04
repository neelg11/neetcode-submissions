class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[-1]*len(s)
        def dfs(i):
            if(i==len(s)):
                return True
            if(dp[i]!=-1):
                return dp[i]
            for word in wordDict:
                if(word==s[i:i+len(word)]):
                    if dfs(i+len(word)):
                        return True
            dp[i] = False
            return False
        return dfs(0)