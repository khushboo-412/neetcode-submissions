class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = Counter(s1)

        l = 0
        n = len(s2)
        window = Counter()
        for r in range(n):
            window[s2[r]] += 1

            if r-l+1>len(s1):
                window[s2[l]] -= 1

                if window[s2[l]] == 0:
                    del window[s2[l]]

                l += 1

            if r-l+1 == len(s1):
                if window == countS1:
                    return True


        return False


        
