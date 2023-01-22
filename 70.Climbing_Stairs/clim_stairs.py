class Solution:
    def climbStairs(self, n: int) -> int:
        dp0, dp1 = 1, 1
        for _ in range(n):
            dp0, dp1 = (dp0+dp1), dp0
        return dp1
