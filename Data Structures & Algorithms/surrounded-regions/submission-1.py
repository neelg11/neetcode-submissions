class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions= [ [1,0], [0,1], [-1,0], [0,-1] ]
        n, m = len(board), len(board[0])
        safe=[[0]*m for _ in range(n)]
        q=deque()
        for i in range(n):
            for j in [0, m-1]:
                safe[i][j]=1
                if board[i][j] == 'O':
                    q.append((i, j))
        for j in range(m):
            for i in [0, n-1]:
                safe[i][j]=1
                if board[i][j] == 'O':
                    q.append((i, j))
        
        while(q):
            row, col = q.popleft()
            for dr, dc in directions:
                nr, nc = row+dr, col+dc
                if(nr<0 or nc<0 or nr>=n or nc>=m or board[nr][nc]=='X' or safe[nr][nc]==1):
                    continue
                safe[nr][nc]=1
                q.append([nr,nc])
        for i in range(n):
            for j in range(m):
                if(board[i][j]=='O' and safe[i][j]==0):
                    board[i][j]='X'
        
