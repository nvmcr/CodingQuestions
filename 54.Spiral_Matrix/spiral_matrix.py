class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        #Create 4 varaible to keep track of boundary
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])

        while left < right and top < bottom:
            #Add all top row elements
            for i in range(left, right):
                res.append(matrix[top][i])
            #Done with the top row so increment top row
            top += 1
            #Add all right col elements
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            #Done with the right col so decrement
            right -= 1
            #What if the matrix at the start of the loop is a single row or col matrix, so check
            if not (left < right and top < bottom):
                break
            #Add all bottom row elements but going from right to left
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            #Done with bottom elements, so decrement
            bottom -= 1
            #Add all left col elements but going from bottom to top
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            #Done with the left elements, so increment
            left += 1
        return res
