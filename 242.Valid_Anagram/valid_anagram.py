class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}
        for i in s:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i] = 1
        for j in t:
            if hashmap.get(j,0) > 0:
                hashmap[j]-=1
            else:
                return False
        return True
