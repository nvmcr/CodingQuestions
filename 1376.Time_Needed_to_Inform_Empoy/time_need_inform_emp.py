class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # No need of visit set as all edges are directed and not more than one manager exists for each employee.
        self.res = 0 #Using self so that res can be manipulated inside dfs function

        # Since the manager column is not exactly in type of adj_list will change that
        head_list = defaultdict(list) #Using a hashmap instead of list as we only have one way edges
        for emp, head in enumerate(manager):
            head_list[head].append(emp)
        '''
        Without using default dict:
        for emp, head in enumerate(mmanager):
            if head not in head_list:
                head_list[head] = []
            head_list[head].append(emp)
        '''

        def dfs(head, time):
            self.res = max(self.res, time)
            for emp in head_list[head]:
                dfs(emp, time + informTime[head])
            
        dfs(headID, 0)
        return self.res
