class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for i in range(numCourses)]
        for i in prerequisites:
            adj_list[i[1]].append(i[0])
        
        rec_path = [False]*numCourses
        vis = [False]*numCourses
        def dfs(k):
            vis[k] = True
            rec_path[k] = True
            for i in adj_list[k]:
                if vis[i] != True:
                    if dfs(i):
                        return True
                elif(rec_path[i]):
                    return True
            rec_path[k] = False
            return False
        for i in range(numCourses):
            if vis[i] == False and dfs(i):
                return False
        return True
            