class Solution:
    def isValid(self, s: str) -> bool:
        close = {")":"(", "}":"{", "]":"["}
        stack = []

        for c in s:
            if c in close:
                if stack and close[c]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if len(stack)==0 else False

            
        