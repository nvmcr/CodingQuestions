class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # Problem similar to house rober instead of neighbors here its num + or - 1
        # Will make our array look like house robber by sorting and without repitetion
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        nums = sorted(list(set(nums)))
        
        dp1, dp2 = 0, 0
        for i, num in enumerate(nums):
            points = num*count[num]
            if i > 0 and num == nums[i-1]+1: #Same as house robber
                temp = max(points+dp1, dp2)
                dp1 = dp2
                dp2 = temp
            else: #No need to ignore previous points
                temp = points+dp2
                dp1 = dp2
                dp2 = temp
        return dp2
