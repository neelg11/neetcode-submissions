class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        area = 0
        def bfs(i,j):
            q=deque()
            q.append([i,j])
            grid[i][j]=0
            ans=1
            while(q):
                row,col=q.popleft()
                for dr,dc in directions:
                    nr=row+dr
                    nc=col+dc
                    if(nr<0 or nc<0 or nr>=ROWS or nc>=COLS or grid[nr][nc]==0):
                        continue
                    ans+=1
                    q.append([nr,nc])
                    grid[nr][nc]=0
            return ans
        for i in range(ROWS):
            for j in range(COLS):
                if(grid[i][j]==1):
                    area=max(area,bfs(i,j))
        return area
