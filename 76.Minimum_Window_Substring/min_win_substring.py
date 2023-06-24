class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case
        if not t or len(t) > len(s):
            return ""
        countS, countT = {}, {}

        for ch in t:
            countT[ch] = 1 + countT.get(ch, 0)

        res, resLen = [0,0], float('inf')
        l = 0
        match, total = 0, len(countT)
        for r in range(len(s)):
            ch = s[r]
            countS[ch] = 1 + countS.get(ch,0)
            if ch in countT and countS[ch] == countT[ch]:
                match += 1
            
            while match == total:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = (r-l+1)
                
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    match -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen < float('inf') else ""
