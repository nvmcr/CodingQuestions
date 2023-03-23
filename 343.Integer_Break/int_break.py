class Solution:
    def integerBreak(self, n: int) -> int:
        # The idea is to break a number into two parts and broken parts can again be broken to two parts so it doesnt matter if max product is from 2 or more broken parts. Ex: n = 10 will be first broken to 3 and 7 and 7 is again broken to 3 and 4.
        # So to solve n, we will first solve all numbers before n
        dp = [0 for _ in range(n+1)]
        for num in range(n):
            dp[num] = num #Max product can be the num itself except for given n as it must be broken down
        
        for num in range(2,n+1):
            for i in range(1,num):
                prod = dp[i]*dp[num-i]
                dp[num] = max(dp[num],prod) #Finding max product of every num.
        return dp[n]
