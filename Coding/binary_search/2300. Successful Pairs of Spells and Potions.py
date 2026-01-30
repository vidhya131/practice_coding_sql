class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        # binary search
        potions.sort()
        n = len(potions)
        for i in spells:
            if i == 0:
                res.append(0)
                continue
            # find the right most unsuccessful pair
            left = 0
            right = n-1
            while left <= right:
                mid = (left+right)//2
                if i*potions[mid] < success: #[0,1,3,6]
                    left = mid+1
                else:            #[1,2,5,6] (i*potions[mid] >= success)
                    right = mid-1
            res.append(n-left)

        return res


        
        