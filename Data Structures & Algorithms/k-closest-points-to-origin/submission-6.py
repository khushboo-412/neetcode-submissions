class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x = point[0]
            y =point [1]
            dist = x**2 + y**2
            heapq.heappush(heap,(dist,x,y))
            
        res = []

        for i in range(k):
            d,x,y = heapq.heappop(heap)
            res.append([x,y])
         
        return res

        
