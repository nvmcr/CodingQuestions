class Solution:
    def fib(self, n: int) -> int:
        if n < 1:
            return 0
        dp0, dp1 = 0, 1
        for _ in range(n-1):
            dp0, dp1 = dp1, (dp0+dp1)
        return dp1
        
