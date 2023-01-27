class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        ans = 0
        lp = 0
        for rp in range(len(s)):
            hashmap[s[rp]] = 1 + hashmap.get(s[rp],0)
            if (rp-lp+1) - max(hashmap.values()) > k:
                hashmap[s[lp]] -= 1
                lp += 1

            ans = max(ans, rp-lp+1)
        return ans
