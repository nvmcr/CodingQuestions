class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums) < 3: return max(nums)

        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # dp[1] = max(nums[0],nums[1])

        # for i in range(2,len(nums)):
        #     dp[i] = max(nums[i]+dp[i-2],dp[i-1])
        # return dp[-1]

        #Without using extra space
        fir_dp, sec_dp = 0,0

        for num in nums:
            temp = max(num+fir_dp,sec_dp)
            fir_dp = sec_dp
            sec_dp = temp
        return sec_dp 
