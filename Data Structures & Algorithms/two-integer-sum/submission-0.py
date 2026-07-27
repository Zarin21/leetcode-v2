class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i in range(len(nums)):
            num_map[nums[i]] = i
        
        for k in range(len(nums)):
            j = target - nums[k]
            if j in num_map and num_map[j] != k:
                if k > num_map[j]:
                    return [num_map[j], k]
                else:
                    return [k, num_map[j]]