class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #Trying to do same as cooldown
        memo = {}
        def dfs(index, buy):
            if index >= len(prices):
                return 0
            if (index, buy) in memo:
                return memo[(index, buy)]
            
            if buy:
                buy_profit = dfs(index+1, not buy) - prices[index] - fee
                cool_profit = dfs(index+1, buy)
                memo[(index, buy)] = max(buy_profit, cool_profit)
            else:
                sell_profit = dfs(index+1, not buy) + prices[index]
                cool_profit = dfs(index+1, buy)
                memo[(index, buy)] = max(sell_profit, cool_profit)
            return memo[(index, buy)]
        return dfs(0, True)
