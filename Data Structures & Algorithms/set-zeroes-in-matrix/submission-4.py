class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        FirstRowZero, FirstColZero = False, False
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if(matrix[i][j]==0):
                    if(i==0):
                        FirstRowZero = True
                    if(j==0):
                        FirstColZero = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for j in range(1, m):
            if matrix[0][j]==0:
                for i in range(1,n):
                    matrix[i][j]=0

        for i in range(1,n):
            if matrix[i][0]==0:
                for j in range(1,m):
                    matrix[i][j]=0

        if FirstRowZero:
            matrix[0] = [0]*m
        
        if FirstColZero:
            for i in range(n):
                matrix[i][0]=0
        
        