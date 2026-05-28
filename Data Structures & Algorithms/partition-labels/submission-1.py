class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        size = 0
        end = 0

        lastIdx ={}
        for i, c in enumerate(s):
            lastIdx[c] = i

        for i,c in enumerate(s):
            size +=1
            end = max(end,lastIdx[c])

            if i == end:
                res.append(size)
                size = 0
        
        return res