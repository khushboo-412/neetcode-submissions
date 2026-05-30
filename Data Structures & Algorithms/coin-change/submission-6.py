class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = amount +1
        memo = {}
        def dfs(a):
            if a == 0:
                return 0
            if a in memo:
                return memo[a]
            
            res = n
            for c in coins:
                if a - c>=0:
                    res  = min(res, 1+ dfs(a-c))
            
            memo[a] =res

            return memo[a]

        return dfs(amount) if dfs(amount) != n else -1
