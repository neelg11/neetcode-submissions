class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n, m = len(grid), len(grid[0])
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        q=deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    q.append([i,j,0])
        while q:
            row, col, dist = q.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if(nr<0 or nc<0 or nr>=n or nc>=m or grid[nr][nc]<=dist+1):
                    continue
                grid[nr][nc]=dist+1
                q.append( [ nr, nc, dist+1 ] )

                