class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort() #Not using sorted inorder to keep space complexity low
        i = 0
        k = len(nums) - 1
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue #skip the repeated num
            #We chose one number and now do 2-sum
            left = i+1
            right = len(nums) - 1
            while left < right:
                threesum = num + nums[left] + nums[right]
                if threesum > 0:
                    right -= 1
                elif threesum < 0:
                    left += 1
                else:
                    ans.append([num, nums[left], nums[right]])
                    left += 1 #We still need to search for other solution
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return ans
