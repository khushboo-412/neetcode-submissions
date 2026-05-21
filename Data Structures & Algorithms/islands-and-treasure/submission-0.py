class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return 
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        visit = set()

        def addRoom(r,c):
            if r<0 or c<0 or r>=m or c>=n or grid[r][c] == -1 or (r,c) in visit:
                return 

            queue.append([r,c])
            visit.add((r,c))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append([i,j])
                    visit.add((i,j))

        dist = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()

                grid[r][c] = dist

                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c-1)
                addRoom(r,c+1)

            dist +=1 

