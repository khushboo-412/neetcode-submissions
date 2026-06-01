class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        

        n = len(points)

        adj = {i: [] for i in range(n)}

        for i  in range(n):
            x1,y1 = points[i]
            for j in range(i,n):
                x2,y2 = points[j]

                dist = abs(x2-x1) + abs(y2-y1)
                adj[i].append([dist,j])
                adj[j].append([dist,i])

        total = 0
        visit = set()
        minHeap = [[0,0]] #cost, node

        while len(visit) <n:
            cost,node = heapq.heappop(minHeap)

            if node in visit:
                continue

            visit.add(node)
            total += cost

            for ct, nei in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap,[ct,nei])

        if len(visit) != n:
            return -1
        
        return total

