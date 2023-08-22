class TrieNode():
    def __init__(self):
        self.child = {}
        self.isEnd = False
    def add(self, word):
        cur = self
        for c in word:
            if c not in cur.child:
                cur.child[c] = TrieNode()
            cur = cur.child[c]
        cur.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        for w in words:
            trie.add(w)
        rows, cols = len(board), len(board[0])
        res, visit = set(),set()
        def dfs(r,c,node, word):
            if r < 0 or c<0 or r == rows or c == cols or (r,c) in visit or board[r][c] not in node.child:
                return
            visit.add((r,c))
            word += board[r][c]
            node = node.child[board[r][c]]
            if node.isEnd:
                res.add(word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,trie,"")
        return res
