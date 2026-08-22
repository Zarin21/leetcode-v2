class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        def helper(nums):
            if len(nums) == 1: return nums[0]
            if len(nums) == 2: return max(nums[0], nums[1])

            one_back = max(nums[0], nums[1])
            two_back = nums[0]

            for num in nums[2:]:
                curr = max(num + two_back, one_back)
                two_back = one_back
                one_back = curr

            return one_back
        
        return max(helper(nums[1:]), helper(nums[0:-1]))