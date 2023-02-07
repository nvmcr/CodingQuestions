class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_range = len(nums)
        #Sum of all numbers in range - Sum of given list gives missing number
        total_sum = sum(range(len(nums)+1))
        given_sum = sum(nums)
        return (total_sum - given_sum)
      
