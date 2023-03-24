class Solution:
    def numSquares(self, n: int) -> int:
        # We can solve min number of every number before given n
        dp = [n for _ in range(n+1)] #Using n as it is the max number of ways, we can use inf too
        dp[0] = 0 #We refer to 0 as the base case
        for num in range(1,n+1):
            for s in range(1,n):#Though the range is till n, loop runs only till sqrt(n)
                ps = s*s
                if num - ps < 0:
                    break #This will break if s>sqrt(n) Thus  time complexity is O(n.sqrt(n))
                dp[num] = min(dp[num],1+dp[num-ps]) #Adding 1 because the sum includes ps
        return dp[n]
