class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        empty = numBottles
        while(empty>=numExchange):
            k = empty//numExchange
            res += k
            empty = k + empty%numExchange
        return res