class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set()
        stack = [0]
        visit.add(0)
        while stack:
            key = stack.pop()
            for child in rooms[key]:
                if child not in visit:
                    stack.append(child)
                    visit.add(child)
        return True if len(visit) == len(rooms) else False
