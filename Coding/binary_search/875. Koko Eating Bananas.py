class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        max_piles = max(piles)
        l = 1
        r = max_piles
        ans = r
        while l<=r and r<=max_piles:
            speed = (l+r)//2
            ## check if  koko can finish with the above speed
            res = self.is_possible(speed, piles, h)
            if res:
                ans = speed
                r = speed-1
            else:
                l = speed+1
        return ans


    def is_possible(self, speed, piles, h):
        return sum(ceil(i/speed) for i in piles) <= h ## ceil value ceil(2.6) = 3
