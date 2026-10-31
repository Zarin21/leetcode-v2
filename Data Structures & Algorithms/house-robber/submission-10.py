class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        one_back = max(nums[1], nums[0])
        two_back = nums[0]
        curr = 0
        for i in range(2, len(nums)):
            curr = max(one_back, nums[i] + two_back)
            two_back = one_back
            one_back = curr
        
        return curr