class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, num in enumerate(nums):
            hashmap[num] = idx
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in hashmap and hashmap[diff] != idx:
                return [idx, hashmap[diff]] 
