class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # memo = {}
        # def rec(row, col):
        #     key = (row, col)
        #     if key in memo:
        #         return memo[key]
        #     else:
        #         if row >= m or col >= n:
        #             return 0
        #         if row == m-1 and col == n-1:
        #             return 1
        #         memo[key] = rec(row+1,col) + rec(row,col+1)
        #     return memo[key]
        # paths = rec(0,0)
        # return paths

        table = [[0 for _ in range(n + 1)] for _ in range(m+1)]
        for row in range(1,m+1):
            for col in range(1,n+1):
                if row == 1 and col == 1:
                    table[row][col] = 1
                else:
                    table[row][col] = table[row-1][col] + table[row][col-1]
        
        return table[-1][-1]
            
