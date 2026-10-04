class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        q = deque()
        q.append([0,0])
        while(q):
            i, j = q.popleft()
            if(i+1<m):
                if(dp[i+1][j]==0):
                    q.append([i+1, j])
                dp[i+1][j] += dp[i][j]
            if(j+1<n):
                if(dp[i][j+1]==0):
                    q.append([i, j+1])
                dp[i][j+1] += dp[i][j]
        return dp[m-1][n-1]