class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

        while len(stones) >1:

            stones.sort()
            last = stones.pop()
            secondlast = stones.pop()
            curr = last-secondlast
            if curr > 0:
                stones.append(curr)
        
        return stones[0] if stones else 0




        