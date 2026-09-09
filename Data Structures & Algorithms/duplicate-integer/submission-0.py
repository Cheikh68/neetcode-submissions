class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        found = []
        for num in nums:
            if num not in found:
                found.append(num)
            else:
                return True
        
        return False