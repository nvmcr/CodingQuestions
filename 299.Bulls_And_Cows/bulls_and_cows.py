class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # Count the bulls first by checking the index and num
        # Then have a counter for cows

        bulls, cows = 0, 0
        s, g = list(secret), list(guess)
        j = 0
        for i in range(0, len(secret)):
            if s[j] == g[j]:
                bulls += 1
                s.pop(j)
                g.pop(j)
            else:
                j += 1
        # Having a counter
        hashmap = {}
        for num in s:
            hashmap[num] =1+hashmap.get(num, 0)
        for num in g:
            if num in hashmap and hashmap[num] != 0:
                cows += 1
                hashmap[num] -= 1
        return f"{bulls}A{cows}B"
