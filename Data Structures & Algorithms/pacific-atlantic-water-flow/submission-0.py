class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pacific=[[False]*m for _ in range(n)]
        atlantic=[[False]*m for _ in range(n)]
        pac_start, atl_start = [], []
        for j in range(m):

            pac_start.append((0,j))
            pacific[0][j]=True

            atl_start.append((n-1,j))
            atlantic[n-1][j]=True

        for i in range(n):

            pac_start.append((i,0))
            pacific[i][0]=True

            atl_start.append((i,m-1))
            atlantic[i][m-1]=True

        def bfs(start_queue,ocean):
            q=deque(start_queue)
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if(nr<0 or nc<0 or nr>=n or nc>=m):
                        continue
                    if(ocean[nr][nc] or heights[nr][nc]<heights[row][col]):
                        continue
                    ocean[nr][nc]=True
                    q.append([nr,nc])
    

        bfs(pac_start, pacific)
        bfs(atl_start, atlantic)
        ans=[]
        for i in range(n):
            for j in range(m):
                if(pacific[i][j] and atlantic[i][j]):
                    ans.append([i,j])
                    
        return ans










            