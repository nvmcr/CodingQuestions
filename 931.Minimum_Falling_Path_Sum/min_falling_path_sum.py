class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        #Given (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1)
        for row in range(1, len(matrix)): #Leaving 0th row as there is no path ending there
            for col in range(len(matrix[0])):
                if col == 0: #There is no left diagonal
                    matrix[row][col] = matrix[row][col] + min(matrix[row-1][col], matrix[row-1][col+1])
                elif col == (len(matrix[0])-1): #There is no right diagonal
                    matrix[row][col] = matrix[row][col] + min(matrix[row-1][col-1], matrix[row-1][col])
                else:
                    matrix[row][col] = matrix[row][col] + min(matrix[row-1][col-1], matrix[row-1][col], matrix[row-1][col+1])
        return min(matrix[-1]) #Last row will have all the path endings sum
        
