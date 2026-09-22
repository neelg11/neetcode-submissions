class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n, m = len(grid), len(grid[0])
        directions = [[0,1], [1,0], [-1,0], [0,-1]]

        def bfs(i, j, distance):
            q = deque()
            q.append([i, j, distance])

            while q:
                row, col, distance = q.popleft()

                for dr, dc in directions:
                    new_r = row + dr
                    new_c = col + dc
                    new_distance = distance + 1

                    if (new_r < 0 or new_c < 0 or
                        new_r >= n or new_c >= m or
                        grid[new_r][new_c] == -1 or
                        grid[new_r][new_c] == 0 or
                        grid[new_r][new_c] <= distance+1 ):
                        continue

                    grid[new_r][new_c] = new_distance
                    q.append([new_r, new_c, new_distance])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    bfs(i, j, 0)