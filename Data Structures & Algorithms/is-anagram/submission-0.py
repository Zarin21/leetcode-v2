class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        check = {}
        
        for i in range(len(s)):
            if s[i] not in check:
                check[s[i]] = 1
            else:
                check[s[i]] += 1
        
        for i in range(len(t)):
            if t[i] not in check:
                return False
            else:
                check[t[i]] -= 1
        
        for _ in check:
            if check[_] != 0:
                return False
        return True