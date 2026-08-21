class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxVolume = 0

        while left < right:
            tmp = (right - left) * min(heights[left], heights[right])
            if tmp > maxVolume:
                maxVolume = tmp

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return maxVolume