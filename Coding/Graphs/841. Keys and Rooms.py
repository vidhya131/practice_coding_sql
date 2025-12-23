class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False]*len(rooms)
        def visit(i):
            visited[i] = True
            for j in rooms[i]:
                if visited[j] == False:
                    visit(j)
            return
        
        visit(0)
        for i in visited:
            if i == False:
                return False
        return True
