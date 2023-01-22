class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #If there are no duplicates
        if len(nums) == len(set(nums)):
            return False
        #create a hashmap
        hashmap = {}
        for idx, num in enumerate(nums):
            if num in hashmap and idx - hashmap[num] <= k:
                return True
            hashmap[num] = idx
        return False
