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
        '''
        table = [[0 for _ in range(n + 1)] for _ in range(m+1)]
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                if row == m-1 and col == n-1:
                    table[row][col] = 1
                else:
                    table[row][col] = table[row+1][col] + table[row][col+1]
        
        return table[0][0]
        '''
        #O(1) space
        dp = [1 for _ in range(n+1)] #Length = No.of cols +1
        dp[-1] = 0 #It is a padding bit and it is always 0 in all rows
        # We can keep incrementing from last row to first row in the same dp
        for row in range(m-2,-1,-1): #dp represents m-1th row so start from m-2
            for col in range(n-1,-1,-1): 
                dp[col] = dp[col] + dp[col+1]
        return dp[0]
