class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        l = 0
        maxL = 0
        for r in range(len(s)):
            while s[r] in s_set:
                s_set.remove(s[l])
                l += 1
            if r - l + 1 > maxL:
                maxL = r - l + 1
            s_set.add(s[r])
        return maxL