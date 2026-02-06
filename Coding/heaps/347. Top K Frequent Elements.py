class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count of each element
        m = {}
        for i in nums:
            m[i] = 1+m.get(i,0)

        # Priority Queue
        pq = []
        for i in m:
            heapq.heappush(pq, (-m[i], i))
        
        # pop top k elements from queue
        res = []
        for i in range(k):
            res.append(heapq.heappop(pq)[1])
        
        return res
        


