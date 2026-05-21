class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit =0
        maxprofit = 0
        l = 0
        r = 1
        while r < n:
            if prices[r]>prices[l]:
                profit = prices[r] -prices[l]
                maxprofit =max(maxprofit,profit)
            else:
                l = r

            r +=1
        
        return maxprofit
        
        
        