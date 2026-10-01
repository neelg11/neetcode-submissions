class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                
                if(matrix[i][j] == 0):
                    for col in range(m):
                        if(matrix[i][col]!=0):
                            matrix[i][col] = float('inf')
                    for row in range(n):
                        if matrix[row][j]!=0:
                            matrix[row][j] = float('inf')
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == float('inf'):
                    matrix[i][j]=0
        

                
        