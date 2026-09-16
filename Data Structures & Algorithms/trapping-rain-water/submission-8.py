class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0

        # For each index, find the maximum rightmost
        left = [None] * len(height)
        right = [None] * len(height)

        # Left side
        max_seen = None
        for i, x in enumerate(height):
            left[i] = max_seen if max_seen is not None and max_seen > x else None
            max_seen = x if max_seen is None else max(max_seen, x)

        # Right side
        max_seen = None
        for i in range(len(height) - 1, -1, -1):
            x = height[i]
            right[i] = max_seen if max_seen is not None and max_seen > x else None
            max_seen = x if max_seen is None else max(max_seen, x)
        
        for i in range(len(height)):
            if left[i] is not None and right[i] is not None:
                water += min(left[i], right[i]) - height[i]
        
        return water
