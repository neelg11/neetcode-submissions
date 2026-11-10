class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,  m = len(grid), len(grid[0])
        def dfs(i, j):
            nonlocal grid
            if (i<0 or i>=n or j<0 or j>=m or grid[i][j]=='0'):
                return 
            if grid[i][j]=='1':
                grid[i][j] = '0'
                for x in [-1, 1]:
                    dfs(i+x,j)
                    dfs(i,j+x)
            return 
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    ans+=1
                    dfs(i,j)
        return ans