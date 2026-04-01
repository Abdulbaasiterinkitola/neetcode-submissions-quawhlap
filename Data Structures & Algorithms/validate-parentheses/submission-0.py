class Solution:
    def isValid(self, s: str) -> bool:
        par_map = {")":"(", "}":"{", "]":"["}
        stack = []

        for char in s:
            if char in par_map:
                if stack and stack[-1] == par_map[char]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(char)

        return not stack
        
        
        """par_map = {"(":")", "{":"}", "[":"]"}
        l, r = 0, len(s)-1

        if len(s)%2 != 0:
            return False
        else:
            while l<r:
                while par_map[s[l]] == s[r]:
                    l, r = l+1, r-1
                return True
        return False
        #wrong, doesn't account for cases like (){}[]
        """
