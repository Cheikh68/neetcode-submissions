class Solution:    
    def threeSum(self, nums):
        result = []
        starters = set()
        nums.sort()

        for i in range(len(nums) - 2):
            if nums[i] in starters:
                continue

            starters.add(nums[i])
            target = 0 - nums[i]
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    previousJ = j
                    result.append([nums[i], nums[j], nums[k]])
                    while j < len(nums) and nums[j] == nums[previousJ]:
                        j += 1

        return result
