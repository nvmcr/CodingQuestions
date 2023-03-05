class Solution:
    def tribonacci(self, n: int) -> int:
        dp0, dp1, dp2 = 0, 1, 1
        if n == 0:
            return 0
        elif n < 3:
            return 1 

        for i in range(2,n):
            dp0, dp1, dp2 = dp1, dp2, dp0+dp1+dp2
        return dp2
