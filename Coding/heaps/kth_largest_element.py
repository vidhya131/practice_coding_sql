import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        j, i = 0, 0
        while(True):
            if j<len(nums):
                heapq.heappush(pq, nums[j])
                j+=1
                i+=1
            else:
                break
            if i>k:
                heapq.heappop(pq)
                i -= 1
        
        return heapq.heappop(pq)
