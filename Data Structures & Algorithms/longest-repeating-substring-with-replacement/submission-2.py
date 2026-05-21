class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        n = len(s)

        l = 0
        r =0
        count = {}
        maxF = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] = 1+ count.get(s[r],0)
            maxF = max(maxF, count[s[r]])

            if (r-l+1) - maxF <= k:
                res= max(res,r-l+1)
            else:
                count[s[l]] -= 1
                l += 1

            
        return res

            



        