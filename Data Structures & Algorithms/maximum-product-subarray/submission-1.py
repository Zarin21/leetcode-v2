class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) # 0; because there might be negative number which is the max prod
        currMin, currMax = 1, 1

        for num in nums:
            tmp = currMin
            currMin = min(num, num * tmp, num * currMax)
            currMax = max(num, num * tmp, num * currMax)

            res = max(res, currMax)

        return res