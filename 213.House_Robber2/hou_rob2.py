class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1: return nums[0]
        def robber(nums):
            dp1, dp2 = 0,0
            for num in nums:
                temp = max(num+dp1,dp2)
                dp1 = dp2
                dp2 = temp
            return dp2
        #If we start at first house cant include last so compare starting with first with excluding last or starting with second
        return max(robber(nums[:-1]),robber(nums[1:])) 
