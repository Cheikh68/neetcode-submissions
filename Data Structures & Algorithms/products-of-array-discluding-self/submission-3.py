class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        prefix = []
        for num in nums:
            prefix.append(product)
            product = product * num
        
        product = 1
        sufix = []
        for i in range(len(nums) - 1, -1, -1):
            sufix.append(product)
            product = product * nums[i]
        sufix.reverse()

        result = []
        for i in range(len(nums)):
            result.append(prefix[i] * sufix[i])

        return result