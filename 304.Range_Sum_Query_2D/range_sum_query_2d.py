class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        #Simiilar to Matrix Block Sum
        rows, cols = len(matrix), len(matrix[0])
        self.IntegralImage = [[0 for _ in range(cols)]for _ in range(rows)]
        for r in range(rows):
            presum = 0
            for c in range(cols):
                presum += matrix[r][c]
                self.IntegralImage[r][c] = presum

                if r > 0:
                    self.IntegralImage[r][c] += self.IntegralImage[r-1][c]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Sum of region = A + D -B -C where r1,c1 is A and r2, c2 is D
        outputsum = self.IntegralImage[row2][col2] #D
        if row1 > 0:
            outputsum -= self.IntegralImage[row1-1][col2] #B
        if col1 > 0:
            outputsum -= self.IntegralImage[row2][col1-1] #C
        if row1>0 and col1>0:
            outputsum += self.IntegralImage[row1-1][col1-1]
        return outputsum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
