class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)

        while start < end:
            index = start + (end - start) // 2
            number = nums[index]

            if number > target:
                end = index
            elif number < target:
                start = index + 1
            else:
                return index

        return -1
