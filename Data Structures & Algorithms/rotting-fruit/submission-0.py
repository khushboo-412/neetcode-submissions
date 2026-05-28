class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        fresh = 0
        queue =deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j]==2:
                    queue.append((i,j))
        
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        time = 0

        while fresh>0 and queue:
            for i in range(len(queue)):
                r,c = queue.popleft()

                for dr,dc in directions:
                    nr = r+ dr
                    nc = c+dc

                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        fresh -= 1

            time += 1

        return time if fresh == 0 else -1




