class Solution:
    def numDecodings(self, s: str) -> int:
        #similar to fibonacci
        dp = [0] * (len(s) + 1)
        dp[-1] = 1

        for i in range(len(s)-1,-1,-1):
            if s[i] == "0":
                dp[i] = 0
            else: dp[i] = dp[i+1]
            if (i+2 <= len(s)) and ((s[i] == "1") or (s[i] == "2") and s[i+1] in "0123456"):
                dp[i] += dp[i+2]
        return dp[0]
