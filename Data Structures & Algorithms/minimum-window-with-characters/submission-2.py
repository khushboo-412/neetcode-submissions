class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""

        tmap = {}
        for c in t:
            tmap[c] = 1+ tmap.get(c,0)
        
        have = 0
        need = len(tmap)
        l = 0

        res = [-1,-1]
        resLen =float('inf')
        
        smap = {}
        for r in range(len(s)):
            smap[s[r]] =  1 + smap.get(s[r],0)

            if s[r] in tmap and smap[s[r]] == tmap[s[r]]:
                have += 1

            while have == need:

                if (r-l+1)<resLen:
                    res =[l,r]
                    resLen = r-l+1

                smap[s[l]] -= 1
                if s[l] in tmap and smap[s[l]] < tmap[s[l]]:
                    have -= 1

                l += 1

        l,r = res
        return s[l:r+1] if resLen != float('inf') else ""



        