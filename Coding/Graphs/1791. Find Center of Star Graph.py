class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = dict()
        for i in edges:
            if i[0] not in graph:
                graph[i[0]] = []
            graph[i[0]].append(i[1])
            if i[1] not in graph:
                graph[i[1]] = []
            graph[i[1]].append(i[0])

        n = len(graph)
        for i in graph:
            if n-1 == len(graph[i]):
                return i
