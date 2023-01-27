class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1

        while left < right:
            for i in range(right-left): #no of elements to be shifted in each row
                top, bottom = left, right #Its a square
                #store any one of the corner variable in temp to do in-place
                temp = matrix[top][left+i]
                #Moving bottom left to top left
                matrix[top][left+i] = matrix[bottom -i][left]
                #Moving bottom right to bottom left
                matrix[bottom-i][left] = matrix[bottom][right-i]
                #Moving top right to bottom right
                matrix[bottom][right-i] = matrix[top+i][right]
                #moving temp to top right
                matrix[top+i][right] = temp
            #Going to inner layers
            left += 1
            right -= 1
