class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # General dfs with memoization
        # For every index we have a choice of buy, sell or cooldown
        memo = {} #Key will be (Index, Buy/Sell) and value is profit
        
        def dfs(index, buy): #buy represents the state. The state changes if we buy/sell
            #Edge cases first
            if index >= len(prices):
                return 0
            if (index, buy) in memo:
                return memo[(index, buy)]
            
            #Choices we have is buy/cooldown or sell/cooldown at each index
            if buy:
                buy_profit = dfs(index+1, not buy) - prices[index] #buy and then can't buy again
                cool_profit = dfs(index+1, buy)
                memo[(index, buy)] = max(buy_profit, cool_profit)
            else:
                sell_profit = dfs(index+2, not buy) + prices[index]
                cool_profit = dfs(index+1, buy)
                memo[(index, buy)] = max(sell_profit, cool_profit)
            return memo[(index, buy)]
        
        return dfs(0, True)
