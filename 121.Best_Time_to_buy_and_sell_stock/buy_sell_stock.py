class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = float('inf')
        max_prof = 0
        for i in range(len(prices)):
            #Alwaystry to buy the cheapest
            if prices[i] < min_buy:
                min_buy = prices[i]
            #If we already have cheapest, go for max profit
            elif prices[i] - min_buy > max_prof:
                max_prof = prices[i] - min_buy
        return max_prof
