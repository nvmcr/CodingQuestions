class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        #Simple but not so effective
        # while start < end:
        #     mid = (start + end) //2
        #     if nums[mid] > nums[end]: #end is small so smallest num is to towards end
        #         start = mid + 1
        #     else: #End is great than mid so small might be mid or towards left of mid
        #         end = mid
        # return nums[start]

        ans = nums[0]
        while start <= end:
            if nums[start] < nums[end]: #Array not rotated
                ans = min(ans, nums[start])
                break
            mid = (start+end) // 2
            ans = min(ans, nums[mid])
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid-1
        return ans
