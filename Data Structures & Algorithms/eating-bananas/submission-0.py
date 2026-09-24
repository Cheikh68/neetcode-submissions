import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        speeds = range(1, max_pile + 1)
        result = max_pile

        left = 0
        right = len(speeds) - 1

        while left <= right:
            mid = (left + right) // 2
            
            time_taken = 0
            for pile in piles:
                time_taken += math.ceil(pile / speeds[mid])

            if time_taken <= h:
                result = min(result, speeds[mid])
                right = mid - 1
            else:
                left = mid + 1

        return result
        