class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = float('inf')
        max_prof = 0
        for price in prices:
            #Alwaystry to buy the cheapest
            if price < min_buy:
                min_buy = price
            #If we already have cheapest, go for max profit
            elif price - min_buy > max_prof:
                max_prof = price - min_buy
        return max_prof
