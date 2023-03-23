class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # We can have many subproblems with dfs(i, a) similar to coin change where i is the coins say if coins=[1,2,5] and dfs(4,1) means number of ways we can amount=4 with coins 1 and 2.
        '''
        # We make this into a dp problem with O(a.i) time and O(a.i) space.
        table = [[0 for _ in range(amount+1)]for _ in range(len(coins))]
        # Note that number of ways we make amount 0 with any number of coins is 1.
        for i in range(len(coins)):
            table[i][0] = 1
        for i in range(len(coins)):
            for a in range(1,amount+1): #First row is for amount 0 which is already filled
                if a-coins[i] >= 0:
                    table[i][a] = table[i][a-coins[i]]
                if i > 0:
                    table[i][a] += table[i-1][a]
        return table[-1][-1]
        '''

        #O(a) solution
        #Make a dp array just for a single coin and will update for next coins in place
        dp = [0 for a in range(amount+1)] 
        dp[0] = 1 #amount = 0
        for i in coins:
            for a in range(1,amount+1):
                if a - i >= 0:
                    dp[a] += dp[a-i]
        return dp[-1]
