class Solution:
    def longestPalindrome(self, s: str) -> int:
        #The idea is to have a count of all letters.
        #If the count is even, then letters can form a palindrome
        #Only one odd count can be considered as a center for palindrome.
        hashmap = {}
        ans = 0
        odd = 0
        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        counter = hashmap.values()
        for count in counter:
            ans += count // 2 * 2 #//2*2 is done to add only the even counts.
            if ans % 2 == 0 and count % 2 == 1: #ans%2==0 means we didnt add the centre
                ans += 1 #Add centre 
        return ans
