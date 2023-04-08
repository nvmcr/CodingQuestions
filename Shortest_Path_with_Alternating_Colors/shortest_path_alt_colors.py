class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # The question is to find shortest paths that has alternating colors between the edges
        # The idea is to run two bfs for finding shortest paths for blue and red
        # Make the rededges and blue edges in form of adajaceny lists
        red_list = defaultdict(list)
        blue_list = defaultdict(list)

        for src, dest in redEdges:
            red_list[src].append(dest)
        for src, dest in blueEdges:
            blue_list[src].append(dest)
        
        q = deque()
        q.append([0,0,None]) #[Node, Length, Prev_Edge_Color]
        visit = set()
        visit.add((0,None)) #(Node, Color)
        answer = [-1 for _ in range(n)]

        while q:
            node, length, prev_edcolor = q.popleft()
            if answer[node] == -1: # The first time visit the node is the shortest length
                answer[node] = length
            if prev_edcolor != 'RED':
                for nei in red_list[node]:
                    if (nei, 'RED') not in visit:
                        visit.add((nei,'RED'))
                        q.append([nei,length+1,'RED'])
            #Similarly for the blue
            if prev_edcolor != 'BLUE':
                for nei in blue_list[node]:
                    if (nei, 'BLUE') not in visit:
                        visit.add((nei,'BLUE'))
                        q.append([nei,length+1,'BLUE'])
        
        return answer
