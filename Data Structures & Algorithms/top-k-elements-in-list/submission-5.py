class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashM ={}

        for i in range(len(nums)):
            hashM[nums[i]] = 1 +hashM.get(nums[i],0)
        
        
        
        arr = []
        for num,count in hashM.items():
            arr.append([count,num])
        arr.sort()
        arr.reverse()

        res = []
        for i in range(k):
            res.append(arr[i][1])

        return res
