class Solution:
    def countSubstrings(self, s: str) -> int:
        #Tracking from middle
        res = 0
        def count(res, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            return res
        for i in range(len(s)):
            #Checking the even palindromes
            left, right = i,i
            res = count(res, left, right)
            #Checking the odd palindromes
            left, right = i, i+1
            res = count(res, left, right)
        return res
