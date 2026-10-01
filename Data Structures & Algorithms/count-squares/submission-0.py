class CountSquares:

    def __init__(self):
        self.matrix = [ [0]*1001 for _ in range(1001)]

    def add(self, point: List[int]) -> None:
        x, y = point
        self.matrix[x][y]+=1

    def count(self, point: List[int]) -> int:
        count = 0
        x, y = point
        for j in range(1001):
            if(self.matrix[x][j] > 0 and j!=y):
                a = 1
                b = self.matrix[x][j]
                side = abs(y - j)
                if(x-side>=0 and self.matrix[x-side][j]>0 and self.matrix[x-side][y]>0):
                    c = self.matrix[x-side][j]
                    d = self.matrix[x-side][y]
                    count+= (a*b*c*d)
                if(x+side<1001 and self.matrix[x+side][j]>0 and self.matrix[x+side][y]>0):    
                    c = self.matrix[x+side][j]
                    d = self.matrix[x+side][y]
                    count+= (a*b*c*d)
        return count
