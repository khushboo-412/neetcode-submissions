class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        dp = {} 
        def dfs(r,c,prevVal):
            if not(0<=r<ROWS) or not(0<=c<COLS) or matrix[r][c] <= prevVal:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            res = 1
            for d in directions:
                res =max(res, 1+dfs(r+d[0],c+d[1],matrix[r][c]))
            dp[(r,c)] = res
            return res


        LIP = 0
        for r in range(ROWS):
            for c in range(COLS):
                LIP =max(LIP, dfs(r,c,float('-inf')))
        return LIP