class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[1000]*(m+1) for _ in range(n+1)]
        dp[n-1][m-1] = grid[n-1][m-1]
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if(i==n-1 and j==m-1):
                    continue
                dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
        return dp[0][0] 