class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        M = len(matrix)
        if M == 0:
            return
        N = len(matrix[0])
        self.cdf = [[0]*N for _ in range(M)]
        self.matrix = matrix

        for j in range(N):
            for i in range(M):
                if i == 0:
                    self.cdf[i][j] = matrix[i][j]
                else:
                    self.cdf[i][j] = self.cdf[i-1][j] + matrix[i][j]
        return
        
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(col1,col2+1):
            sum += self.cdf[row2][i] - self.cdf[row1][i] + self.matrix[row1][i]
        return sum
