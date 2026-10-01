class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i, element in enumerate(nums):
            if target - element in num_dict:
                return [num_dict[target - element], i]
            
            num_dict[element] = i