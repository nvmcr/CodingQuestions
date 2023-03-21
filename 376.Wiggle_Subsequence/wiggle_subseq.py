class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # We make an array with differences and then check if it is wiggling.
        # There is an exception case of getting a zero. If the differences are constantly zero the max length of wiggle is 1.
        
        dp = [nums[i]-nums[i-1] for i in range(1,len(nums)) if nums[i]-nums[i-1]!=0]
        if not dp: return 1 #If len ==1 or its zeros.
        res = 2 #Minimum result if there are two sequences
        for i in range(1, len(dp)):
            if (dp[i] < 0 and dp[i-1] > 0) or (dp[i] > 0 and dp[i-1] < 0):
                res += 1
        return res
