class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #This is similar to max subarray (LC 53) except subarray can be cicular
        #The idea is to maintain currsum_max and maxsum (LC53). maxsum gives the answer for the linear array.
        #As it is a circular case, will keep track of currsum_min and minsum. If the minsum is negative then Total array - minsum will give the maxsum_2. Comparing maxsum_2 and maxsum gives the maxsum of circular array.
        curr_max, curr_min = 0,0
        max_sum, min_sum = nums[0], nums[0] #If the max sum is < 0
        total = 0
        for num in nums:
            curr_max = max(curr_max+num, num)
            max_sum = max(max_sum, curr_max)
            curr_min = min(curr_min+num, num)
            min_sum = min(min_sum, curr_min)
            total += num
        #res = max(max_sum, total - min_sum) #This doesn't work if all numbers are negative
        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum 
        
