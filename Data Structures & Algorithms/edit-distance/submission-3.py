class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = {}

        def dfs(i,j):
            if j == n:
                return m - i

            if i == m:
                return n-j

            if (i,j) in dp:
                return dp[(i,j)]

            
            if word1[i] == word2[j]:
                dp[(i,j)] = dfs(i+1,j+1)
                return dp[(i,j)]

            res = min(dfs(i+1,j), dfs(i,j+1), dfs(i+1,j+1))
            dp[(i,j)] = res + 1
            return res +1



        return dfs(0,0)