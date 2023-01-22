class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0] #Incase only the first number is max sum
        curr_sum = 0
        
        for num in nums:
            if curr_sum < 0:
                curr_sum = 0 #Resetting to zero means starting from present num
            curr_sum += num
            max_sum = max(curr_sum, max_sum)
        return max_sum

    # def maxSubArray(self, nums):
	  # 	dp = [0]*len(nums)
    #     for i,num in enumerate(nums):            
    #         dp[i] = max(dp[i-1] + num, num)
    #     return max(dp)
