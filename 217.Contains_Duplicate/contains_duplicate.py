class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #create a set
        newset = set()
        #Add all elements of list to set; O(n) time and space complexity
        for num in nums:
            #If the number is already in the set, it is a duplicate
            if num in newset:
                return True
            newset.add(num)

        '''
        Alternatively
        hashmap = {}
        for num in nums:
            if num in hashmap:
                return True
            hashmap[num] = num
        return False
        '''
