class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create a hashmap
        hashmap = {}
        #Add all nums to hashmap O(n) time and space complexity
        for idx, num in enumerate(nums):
            hashmap[num] = idx
        #Go through hashmap if difference of target and num is in hashmap
        for idx, num in enumerate(nums):
            diff = target - num
            #Check if diff in hashmap and make sure its not the present number
            if diff in hashmap and hashmap[diff] != idx:
                return [idx, hashmap[diff]]
