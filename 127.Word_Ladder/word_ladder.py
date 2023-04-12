class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # We have two steps here, one is to make an adjaceny list with neighbor words and bf
        # If endword not in wordlist return 0
        if endWord not in wordList:
            return 0
        
        adjlist = defaultdict(list)
        # Step 1
        # Make an adjaceny list with neighbor words in a single list
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "#" + word[i+1:] # Replacing each letter in word with #
                adjlist[pattern].append(word) #Every word with same pattern is placed in respective list


        # BFS
        q, visit = deque(), set()
        q.append(beginWord)
        visit.add(beginWord)
        res = 1 #Counting the first word
        while q:
            for j in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + "#" + word[i+1:]
                    for neiWords in adjlist[pattern]:
                        if neiWords not in visit:
                            visit.add(neiWords)
                            q.append(neiWords)
            res += 1
        return 0
