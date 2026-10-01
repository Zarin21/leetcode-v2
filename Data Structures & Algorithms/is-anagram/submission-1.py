class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = {}

        for i in s:
            if i in check:
                check[i] += 1
            else:
                check[i] = 1
        
        for j in t:
            if j not in check:
                return False
            check[j] -= 1
        
        for _ in check:
            if check[_] != 0:
                return False
        return True