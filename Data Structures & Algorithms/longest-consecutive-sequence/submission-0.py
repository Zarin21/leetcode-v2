class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
            
        length = 0
        for n in num_set:
            curr = 1
            if n - 1 not in num_set:
                while n + curr in num_set:
                    curr += 1
            length = max(curr, length)
        return length