class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashM ={}

        for i in range(len(nums)):
            hashM[nums[i]] = 1 +hashM.get(nums[i],0)
        
        
        
        heap = []

        for num, count  in hashM.items():
            heapq.heappush(heap,(count,num))
            if len(heap)>k:
                heapq.heappop(heap)
        

        res = []
        for count, num in heap:
            res.append(num)

        return res
