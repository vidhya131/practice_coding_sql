import math
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        n = len(potions)
        potions.sort()
        # ceiling division
        for i in spells:
            if i == 0:
                res.append(0)
                continue
            minimum_potion = math.ceil(success/i)
            k = bisect_left(potions, minimum_potion)
            res.append(n-k)
            
        
        # binary search
        # for i in spells:
        #     if i == 0:
        #         res.append(0)
        #         continue
        #     # find the right most unsuccessful pair
        #     left = 0
        #     right = n-1
        #     while left <= right:
        #         mid = (left+right)//2
        #         if i*potions[mid] < success: #[0,1,3,6]
        #             left = mid+1
        #         else:            #[1,2,5,6] (i*potions[mid] >= success)
        #             right = mid-1
        #     res.append(n-left)

        return res

