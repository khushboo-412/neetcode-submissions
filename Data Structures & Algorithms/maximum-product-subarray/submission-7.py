class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)
        curMax =1
        curMin =1

        for n in nums:
            if n==0:
                curMax= 1
                curMin = 1
                continue

            curMax, curMin = max(n*curMax, n*curMin , n), min(n*curMax, n*curMin , n)
            res = max(res,curMax,curMin)

        return res

