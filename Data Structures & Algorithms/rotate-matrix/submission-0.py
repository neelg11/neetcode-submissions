class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        mat=[]
        n=len(matrix)
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(matrix[n-j-1][i])
            mat.append(row)
        matrix[:]=mat