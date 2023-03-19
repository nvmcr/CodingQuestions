class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        table = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if obstacleGrid[r][c] == 1: #If there is a obstacle, set dp to 0
                    table[r][c] = 0
                elif r == rows-1 and c == cols-1: #The goal is marked one and follow bottom-up approach
                    table[r][c] = 1
                else:
                    table[r][c] = table[r+1][c] + table[r][c+1]
        return table[0][0]
