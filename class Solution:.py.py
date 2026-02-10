class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        n = len(prices)
        profit = 0
        while l<r and r<n:
            if prices[l]>prices[r]:
                l = r
                r += 1
            else:
                profit = max(profit, prices[r]-prices[l])
                r += 1
        return profit
            