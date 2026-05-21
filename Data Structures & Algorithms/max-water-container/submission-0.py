class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n =len(heights)
        l = 0
        area =0
        maxA = 0
        r = n-1

        while l<r:
            area = (r-l) * min(heights[l],heights[r])
            maxA = max(area,maxA)

            if heights[l]<heights[r]:
                l += 1
            else:
                r -= 1
        return maxA


