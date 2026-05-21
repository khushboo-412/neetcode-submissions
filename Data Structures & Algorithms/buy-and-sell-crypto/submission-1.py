class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit =0
        maxprofit = 0
        for i in range(n):
            for j in range(i+1,n):
                if prices[j]>prices[i]:
                    profit = prices[j]-prices[i]
            
                    maxprofit = max(maxprofit,profit)

        return maxprofit
        