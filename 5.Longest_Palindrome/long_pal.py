class Solution:
    def longestPalindrome(self, s: str) -> str:
        #The idea is to consider each letter in the string as the center of palindrome and keep checking left and right.
        res = ""
        reslen = 0
        def checkpal(left, right, res, reslen):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right-left+1 > reslen:
                    res = s[left:right+1]
                    reslen = right - left +1
                left -= 1
                right += 1
            return res,reslen
        for i in range(len(s)):
            #If the palindrome is of odd length, the center is only one letter
            left, right = i, i #Starting at the center letter
            res, reslen = checkpal(left, right, res, reslen)
            #If the palindrome is of even length, then there are two letter at center
            left, right = i, i+1
            res, reslen = checkpal(left, right, res, reslen)
        return res
