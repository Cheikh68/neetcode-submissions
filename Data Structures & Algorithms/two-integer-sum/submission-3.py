class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        
        for i in range(len(nums)):
            complements[i] = target - nums[i]
        
        result = []
        for j in range(len(nums)):
            for key, value in complements.items():
                if nums[j] == value and j != key:
                    result.append(key)
                    result.append(j)
                    return [min(result), max(result)]