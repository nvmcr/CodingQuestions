class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Idea is to have two hashmaps one for s and p and both should be of length p. If both are equal, append the index
        if len(p) > len(s):
            return []
        ans = []
        s_hash, p_hash = {}, {}
        #Creating counts of each string
        for letter in range(len(p)): #Only first p letters of s
            p_hash[p[letter]] = 1 + p_hash.get(p[letter],0) #Using get to avoid error
            s_hash[s[letter]] = 1 + s_hash.get(s[letter],0)
        if p_hash == s_hash: ans.append(0)
        leftp = 0
        for rightp in range(len(p), len(s)):
            s_hash[s[rightp]] = 1 + s_hash.get(s[rightp],0) #Include the new letter
            s_hash[s[leftp]] -= 1 #Remove the previous letter
            if s_hash[s[leftp]] == 0: #Remove the count of letter that is not in s
                s_hash.pop(s[leftp])
            leftp += 1
            if p_hash == s_hash:
                ans.append(leftp)
        return ans
