class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        strs = sorted(strs)
        first_str = strs[0]
        last_str = strs[-1]
        idx = 0
        res = ""
        
        while idx < len(first_str) and idx < len(last_str) and first_str[idx] == last_str[idx]:
            
            res += first_str[idx]
            idx += 1
        return res