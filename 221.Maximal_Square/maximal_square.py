class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # We can do a top-down approach
        rows, cols = len(matrix), len(matrix[0]) 
        table = [[0 for _ in range(cols+1)]for _ in range(rows+1)] #having extra padding at top
        maxlen = 0
        for r in range(1,rows+1):
            for c in range(1,cols+1):
                if matrix[r-1][c-1] == '1': # -1 as we padded at top
                    table[r][c] = 1 + min(table[r-1][c-1], table[r-1][c], table[r][c-1])
                    maxlen = max(maxlen, table[r][c])
        return maxlen ** 2
