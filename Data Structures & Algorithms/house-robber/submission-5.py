class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        one_back = max(nums[0], nums[1])
        two_back = nums[0]
        
        for i in range(2, len(nums)):
            curr = max(nums[i] + two_back, one_back)
            two_back = one_back
            one_back = curr
        
        return one_back