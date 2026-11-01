class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[1], nums[0])

        def houserobber(nums):
            if len(nums) == 1: return nums[0]
            if len(nums) == 2: return max(nums[1], nums[0])

            one_back = max(nums[0], nums[1])
            two_back = nums[0]

            for i in range(2, len(nums)):
                tmp = one_back
                one_back = max(nums[i] + two_back, one_back)
                two_back = tmp
            
            return one_back
        
        return max(houserobber(nums[1:]), houserobber(nums[:-1]))