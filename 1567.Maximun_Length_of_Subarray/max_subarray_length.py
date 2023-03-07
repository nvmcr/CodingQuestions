class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # We need to check when a number gives a positive result
        res, pos, neg = 0, 0, 0 #pos tracks positive prod and neg tracks neg prod
        for num in nums:
            if num > 0: # Multiplying with a positive num
                pos += 1 #pos*pos gives pos
                neg = neg + 1 if neg > 0 else 0 #neg*pos = neg but there should be a neg in first place
            elif num < 0:
                temp = pos
                pos = 1 + neg if neg > 0 else 0 #neg*neg=pos
                neg = 1 + temp #pos*neg = neg
            else: #num=0
                pos, neg = 0, 0
            res = max(res, pos)
        return res
