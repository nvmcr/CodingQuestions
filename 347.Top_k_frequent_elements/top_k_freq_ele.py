class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {} #to get the counts
        #The index represents the count values and the inner list is the elements
        freq = [[] for i in range(len(nums)+1)] #Max freq len in the len of nums (every numcount is 1)
        res=[]
        #Getting counts
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        #filling res
        for num, count in hashmap.items():
            freq[count].append(num)
        #Note: The first index(0) in freq is always empty
        for ele in range(len(freq)-1, 0, -1):
            for elelist in freq[ele]:
                res.append(elelist)
                if len(res)==k: #Result contains k frequent elements
                    return res
            
