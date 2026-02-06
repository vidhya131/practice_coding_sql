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
        
# Counting sort or bucket sort solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count of each element
        m = {}
        max_freq = 0
        for i in nums:
            m[i] = 1+m.get(i,0)
            max_freq = max(max_freq, m[i])
        
        freq = [[] for i in range(max_freq+1)]
        for key,val in m.items():
            freq[val].append(key)
        res = []
        for i in range(max_freq,-1,-1):
            res.extend(freq[i])
            if len(res)>=k:
                return res[:k]
        




