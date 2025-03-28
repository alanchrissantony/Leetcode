class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        profit=0
        i=1
        while i<len(prices):
            profit=max(profit, prices[i]-buy)
            buy=min(buy, prices[i])
            i+=1
        return profit