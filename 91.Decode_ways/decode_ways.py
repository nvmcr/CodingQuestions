class Solution:
    def numDecodings(self, s: str) -> int:
        '''
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
        '''
        # O(1) memory
        # As we can see, above dp only uses i + 1 or i+2 to solve at each step
        # So will have three variables
        # dp0 = current state, dp1 = previous state (i+1) and dp2 = before previous(i+2)
        dp0, dp1, dp2 = 0, 1, 0 #Initializing previous state to 1 because if num exists there is atleast one way to decode.
        for i in range(len(s)-1, -1, -1):
            if s[i] != '0':
                dp0 += dp1
            if i+2 <= len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):
                dp0 += dp2
            dp0, dp1, dp2 = 0, dp0, dp1 #As we are moving back in s
        return dp1 
