class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit =0
        maxprofit = 0
        l = 0
        r = 1

        minBuy = prices[0]

        for sell in prices:

            maxprofit = max(maxprofit, sell - minBuy)
            minBuy = min(minBuy, sell)
        
        return maxprofit 
       
        
        
        