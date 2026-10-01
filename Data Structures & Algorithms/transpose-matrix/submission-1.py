class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n , m = len(matrix),  len(matrix[0])

        if (n==m):
            for r in range(n):
                for c in range(r,m):
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            return matrix

        ans = [[0]*n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                ans[j][i] = matrix[i][j]
        return ans