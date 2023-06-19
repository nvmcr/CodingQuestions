class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr1, ptr2 = 0, 0
        #merged = "" Not using string because strings are immutable in python and any cincatenation to string creates a new string
        res = []
        while ptr1 < len(word1) or ptr2 < len(word2):
            if ptr1<len(word1):
                res.append(word1[ptr1])
                ptr1 += 1
            if ptr2<len(word2):
                res.append(word2[ptr2])
                ptr2 += 1
        return "".join(res)

        # TC - O(m+n)
        #SC - O(1)
