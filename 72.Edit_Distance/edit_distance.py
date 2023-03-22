class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #We can have two pointers i and j that start at word1 and word2 respectively.
        #At each step we can do three operations +1 default.
        #1. If word[i] == word[j] then we dont do any operations we just check word1[i+1] and word2[j+1].
        #2. If word[i] != word[j] then we can do any of three operations given and choose minimum operations of all 3.
        # Insert: Inserting a char in word1 is we just move one char ahead in word2 i.e 1 + word1[i], word2[j+1].
        #deletion: Deleting a char in word1 means we just move one char ahead in word1 i.e 1+word1[i+1], word2[j]
        #Replace: If we replace a char in word1 means we made both chars equal so move ahead in both i.e 1 + word1[i+1], word2[j+1]
        # Edge case: If any one of the string becomes empty, then we just add/delete all remaining characters of non-empty string i.e we add len(word2[i:]) if word1 is empty and vice-versa
        table = [[0 for j in range(len(word2)+1)]for i in range(len(word1)+1)]
        # If the word2 is empty then we add remaining length of our word 1
        for i in range(len(word1)+1):
            table[i][0] = i
        # If the word1 is empty then we add remaining length of our word 2
        for j in range(len(word2)+1):
            table[0][j] = j
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    table[i][j] = table[i-1][j-1] #no extra operations just get the before operations
                else:
                    table[i][j] = 1 + min(
                        table[i-1][j],#insert
                        table[i][j-1],#delete
                        table[i-1][j-1]#replace
                    )
        return table[-1][-1]
                
