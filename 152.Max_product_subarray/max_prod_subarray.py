class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums) #Incase single number is greater than prod of any subarray
        #Consider both max and min beacuse of negative numbers
        currmax, currmin = 1,1 #to avoid zero
        for num in nums:
            temp = currmax*num
            currmax = max(temp, currmin*num, num)
            currmin = min(temp, currmin*num, num)
            ans = max(ans, currmax)
        return ans
