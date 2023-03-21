class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # Main idea
        # If s = 'bbbab' and l(0,5) be the length of longest palindromic subsequence from 0th(i) to 5th(j) index.
        # will count palindromes coming from out to inside.
        # l(0,5) can be calculated in two scenarios.
        # 1.If 0th index and 5th index is same then know for sure that minimum 2 characters are in the subsequence and go to inner characters i.e l(0,5) = 2 + l(1,4).
        #2.If 0th idx != 6th idx then we can only consider one from 0 and 5th index. i.e l(0,5) = max(l(0,4), l(1,5)).
        table = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
          table[i][i] = 1 #Make all diagonal elements 1 as they represent single char i.e i = j
        # All our table cant be filled only the upper diagonal will be filled as i can't be < 1.
        for strlen in range(2,len(s)+1): #length of our palindrome
          for i in range(0, len(s)-strlen+1): #left pointer
            j = i+strlen-1
            if s[i] == s[j] and strlen == 2: #As max palindrome is always 2 if strlen=2
                table[i][j] = 2
            elif s[i] == s[j]:
                table[i][j] = 2+table[i+1][j-1] #l(0,5) = 2 + l(1,4)
            else:
                table[i][j] = max(table[i][j-1], table[i+1][j])
        return table[0][-1]
