class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)

        while n>1:

            stones.sort()
            last = stones.pop()
            secondlast = stones.pop()
            curr = last-secondlast
            if curr > 0:
                stones.append(curr)
            n = len(stones)
        
        return stones[0] if stones else 0




        