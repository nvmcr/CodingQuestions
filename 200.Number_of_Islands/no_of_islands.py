class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        no_of_islands = 0
        def dfs(grid, row, col):
            if row<0 or col<0 or row>=len(grid) or col>=len(grid[0]) or grid[row][col] != "1":
                return
            grid[row][col] = "2" #visited
            #tarverse in all 4 directions
            dfs(grid,row+1, col)
            dfs(grid, row, col+1)
            dfs(grid, row-1, col)
            dfs(grid, row, col-1)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    no_of_islands += 1
                    dfs(grid, row, col)
        return no_of_islands
