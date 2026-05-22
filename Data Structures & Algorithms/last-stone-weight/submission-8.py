class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for i in range(len(stones)):
            heapq.heappush(heap,(-1*stones[i]))


        while len(heap)>1:
            curr = (-1*heapq.heappop(heap)) - (-1*heapq.heappop(heap))
            if curr>0:
                heapq.heappush(heap,(-1*curr))

        return (-1 *heap[0]) if heap else 0

        




        