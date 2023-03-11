class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        #If the difference between numbers is same count, so creating a dp array to hold diff
        # length = len(nums)
        # if length < 3: #Doesn't matter
        #     return 0
        # dp = [0]*(length-1)
        # for i in range(1,length):
        #     dp[i-1] = nums[i]-nums[i-1]
        # res, slices = 0,1

        # for i in range(1, length-1):
        #     if dp[i] == dp[i-1]:
        #         res += slices
        #         slices += 1
        #     else:
        #         slices = 1
        # return res

        #O(1) space
        length = len(nums)
        if length < 3:
            return 0
        res, slices, curr_diff = 0, 1, 0
        diff = nums[1] - nums[0]
        for i in range(1, length-1):
            curr_diff = nums[i+1]-nums[i]
            if curr_diff == diff:
                res += slices
                slices += 1
            else:
                diff = curr_diff
                slices = 1
        return res
