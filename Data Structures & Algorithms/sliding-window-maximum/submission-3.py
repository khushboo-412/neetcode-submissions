class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        queue = deque()
        l = 0
        r = 0
        res = []

        for r in range(len(nums)):
            while queue and nums[queue[-1]] <nums[r]:
                queue.pop()

            queue.append(r)

            if r+1>=k:
                res.append(nums[queue[0]])
                l += 1

            if l>queue[0]:
                queue.popleft()



        return res