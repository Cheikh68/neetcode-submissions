import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        result = max_pile

        left = 1
        right = max_pile

        while left <= right:
            mid = (left + right) // 2
            
            time_taken = 0
            for pile in piles:
                time_taken += math.ceil(pile / mid)

            if time_taken <= h:
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1

        return result
        