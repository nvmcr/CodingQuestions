class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        #We need just a single extra variable for col
        colZero = False
        #Marking the rows and cols for zeroing
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    #Mark the col to zero by making a zero in first row in that col
                    matrix[0][c] = 0
                    #Mark the row to zero by making a zero in first col in that row
                    #Do this only if it is not the extra variable
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        colZero = True
        #Setting the elements to zero based on the first row and first column
        #Dont involve first row and col as they are needed to set others to zero
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        #Now coming to first row and col 
        #check only matrix[0][0], this determines first column
        if matrix[0][0] == 0:
            for r in range(1, rows):
                matrix[r][0] = 0
        #Check the extra varaible, this determines first row
        if colZero:
            for c in range(cols):
                matrix[0][c] = 0

