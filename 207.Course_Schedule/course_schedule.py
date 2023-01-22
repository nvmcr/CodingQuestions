class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Creating an adjacency list where each course is mapped to its prerequisites
        adjList = {course:[] for course in range(numCourses)}
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if adjList[course] == []: #No prereq
                return True
            visited.add(course)
            for pre in adjList[course]:
                if not dfs(pre): #if dfs(pre) return False due to a circle discovered by visited
                    return False
            adjList[course] = [] #Emptying because it returned True and no need to go through above loop again.
            visited.remove(course) #Orlse it will return False for another course
            return True

        for course in range(numCourses): #This for loop is if there are any courses at are not in same graph like 1-> 2->3 and 4->5. 4 and 5 are not covered in 1,2,3 graph.
            if not dfs(course):
                return False
        return True
