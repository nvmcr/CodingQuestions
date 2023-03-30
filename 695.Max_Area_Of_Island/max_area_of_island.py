class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        area = 0
        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                return 0
            
            grid[r][c] = 2
            return 1 + dfs(r+1, c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r, c-1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = max(area,dfs(row, col))
        return area
