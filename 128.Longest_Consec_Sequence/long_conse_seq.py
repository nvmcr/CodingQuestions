class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Since we cant sort the list
        #We should find the start of sequence and find the length
        hashset = set(nums)
        res = 0
        for num in nums:
            if num-1 not in hashset:#start of the sequence
                length = 0
                while (num + length) in hashset:
                    length += 1
                res = max(res, length)
        return res
