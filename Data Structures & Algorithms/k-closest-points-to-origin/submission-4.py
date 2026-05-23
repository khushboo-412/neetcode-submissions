class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x = point[0]
            y =point [1]
            dist = x**2 + y**2
            heapq.heappush(heap,(dist,x,y))
            
        res = []

        while k>0:
            d,x,y = heapq.heappop(heap)
            res.append([x,y])
            k -= 1
        
        return res

        
