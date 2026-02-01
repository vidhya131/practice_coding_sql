class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # as the graph can be unconnected
        adj_list = [[] for i in range(0,n+1)]
        for i in roads:
            adj_list[i[0]].append((i[1],i[2]))
            adj_list[i[1]].append((i[0],i[2]))
        vis = set()
        def dfs(i):
            vis.add(i)
            score = 100000
            for j in adj_list[i]:
                score = min(score, j[1])
                if j[0] not in vis:
                    score = min(score,dfs(j[0]))
            return score
        return dfs(1)


