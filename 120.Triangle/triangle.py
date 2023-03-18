class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Similar to min falling path
        rows = len(triangle)
        for i in range(1, rows):
            for j in range(0, i+1):
                if j == 0:# The above row doesn't have j-1 term
                    triangle[i][j] += triangle[i-1][j]
                elif j == i: #The above row doesn;t have j term
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
        return min(triangle[-1])
