class Solution:
    def twoSum0(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        result = []
        previous_left = None
        previous_right = None

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                if numbers[left] != previous_left and numbers[right] != previous_right:
                    result.append([numbers[left], numbers[right]])
                    previous_left = numbers[left]
                    previous_right = numbers[right]
                left += 1
                right -= 1
        
        return result
    
    def threeSum(self, nums):
        nums.sort()
        result = []
        previous = None

        for i in range(len(nums)):
            if nums[i] != previous:
                complements = self.twoSum0(nums[i+1:], nums[i] * -1)
                if complements:
                    for complement in complements:
                        result.append([nums[i], complement[0], complement[1]])
            previous = nums[i]

        return result
