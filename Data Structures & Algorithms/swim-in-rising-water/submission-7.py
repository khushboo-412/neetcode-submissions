class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        visit = set()

        minHeap = [[grid[0][0],0,0]]

        while minHeap:
            t,r,c = heapq.heappop(minHeap)

            if r==m-1 and c==n-1:
                return t

            for dr,dc in [[0,1],[0,-1],[1,0],[-1,0]]:
                nr = r+ dr
                nc = c+dc
                if not(0<=nr<m) or not(0<=nc<n) or (nr,nc) in visit:
                    continue

                visit.add((nr,nc))
                heapq.heappush(minHeap, [max(t,grid[nr][nc]),nr,nc])