class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        rows, cols = len(grid), len(grid[0])
        table = [[float('inf') for _ in range(cols+1)]for _ in range(rows+1)] # Always set the default values to worst
        table[rows][cols-1] = 0 #table[rows-1][cols]=0 will also work
        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                table[r][c] = grid[r][c] + min(table[r+1][c], table[r][c+1])
        return table[0][0]
        '''
        # O(1) space
        rows, cols = len(grid), len(grid[0])
        for row in range(1, rows):
            grid[row][0] += grid[row-1][0] #The first column path only invloves sum from above rows
        for col in range(1, cols):
            grid[0][col] += grid[0][col-1] #The first row path only invloves sum from before columns
        # Leaving first row and first column, follow the constraint of down and right
        for r in range(1, rows):
            for c in range(1, cols):
                grid[r][c] += min(grid[r-1][c], grid[r][c-1])
        return grid[-1][-1] #grid[rows-1][cols-1]
