class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        #Using O(n) space
        newstr = ""
        for letter in s:
            if letter.isalnum(): #if alphanumeric
                newstr += letter.lower()
        return newstr == newstr[::-1]
        """
        #Using O(1) space
        if len(s) <= 1:
            return True
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
