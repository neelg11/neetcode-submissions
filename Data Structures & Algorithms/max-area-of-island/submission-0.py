class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        n,m=len(grid), len(grid[0])
        def dfs(i,j):
            if(i<0 or j<0 or i>=n or j>=m or grid[i][j]==0):
                return 0
            grid[i][j]=0
            sum=1
            for dr,dc in directions:
                sum+=dfs(i+dr,j+dc)
            return sum
        ans=0
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==1):
                    ans=max(ans,dfs(i,j))
        return ans