from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        found = []
        for num in nums:
            if num in found:
                return True
            else:
                found.append(num)
        return False