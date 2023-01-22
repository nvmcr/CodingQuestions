class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[start] <= nums[mid]: #left sorted
                if nums[start] <= target <= nums[mid]: #Target is in the left sorted split
                    end = mid - 1
                else: #Target is greater than mid or less than start
                    start = mid + 1
            else: #Right sorted
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
