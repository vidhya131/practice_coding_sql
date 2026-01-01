import heapq
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pq = []
        indegree = [0]*numCourses
        adj_list = defaultdict(list)
        for c, p in prerequisites:
            adj_list[p].append(c)
            indegree[c] += 1
        q = deque()
        for i in range(numCourses):
            print(i)
            if indegree[i] == 0:
                q.append(i)
                print(i)
        # print(len(q))
        results = []
        while(len(q) != 0):
            l_poped = q.popleft()
            results.append(l_poped)
            # print(l_poped)
            for i in adj_list[l_poped]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        if len(results) == numCourses:
            return results
        return []
