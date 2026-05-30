class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def check(numsL):
            rob1,rob2 = 0,0

            for n in numsL:
                t = max(rob2, n+rob1)
                rob1 = rob2
                rob2 = t
            return rob2


        return max(check(nums[1:]),check(nums[:-1]))