class Solution:
    def twoSum(self, nums, target):
        seen = {}
        result = []

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                result.append([seen[complement], i])

            seen[num] = i

        return result

    
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums)):
            duos = self.twoSum(nums, -nums[i])

            for duo in duos:
                if i not in duo:
                    trio = [nums[i], nums[duo[0]], nums[duo[1]]]
                    trio.sort()

                    if trio not in result:
                        result.append(trio)

        return result

