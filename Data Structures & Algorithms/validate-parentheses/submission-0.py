class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(": ")","{": "}", "[": "]"}
        stack = []

        for _ in s:
            if _ in brackets:
                stack.append(_)
            else:
                if stack:
                    if _ != brackets[stack.pop()]: 
                        return False
                else:
                    return False
        if stack:
            return False
        return True