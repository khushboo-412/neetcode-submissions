class Solution:
    def countSubstrings(self, s: str) -> int:
        resIdx = 0
        resLen = 0
        count = 0
        for i in range(len(s)):

            #odd
            l=i
            r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                count += 1
                if (r-l+1)>resLen:
                    resIdx =l
                    resLen = r-l+1

                l -= 1
                r += 1

            #even
            l=i
            r=i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                count += 1
                if (r-l+1)>resLen:
                    resIdx =l
                    resLen = r-l+1

                l -= 1
                r += 1

        return count

            
