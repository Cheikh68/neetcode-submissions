class Solution:
    def maxArea(self, heights: List[int]) -> int:
        current_best = 0
        left = 0
        right = len(heights) - 1

        while left != right:
            current_best = max(current_best, (right - left) * min(heights[right], heights[left]))
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return current_best