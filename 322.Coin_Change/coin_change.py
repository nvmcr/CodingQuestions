class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1]*(amount+1) #Value can be anything larger than amount
        dp[0] = 0
        for money in range(1, amount + 1):
            for coin in coins:
                if money - coin >= 0:
                    dp[money] = min(dp[money], 1+dp[money-coin])
        if dp[amount] != amount+1: #Initial value
            return dp[amount]
        else:
            return -1
