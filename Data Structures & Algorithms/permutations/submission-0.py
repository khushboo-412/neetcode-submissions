class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm =[[]]

        for num in nums:
            newp = []
            for p in perm:
                for i in range(len(p)+1):
                    pc = p.copy()
                    pc.insert(i,num)
                    newp.append(pc)
            perm = newp

        return perm