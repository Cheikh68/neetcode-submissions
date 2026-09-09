class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        prefix = []
        for num in nums:
            prefix.append(product)
            product = product * num
        
        product = 1
        sufix = []
        for num in reversed(nums):
            sufix.append(product)
            product = product * num
        sufix.reverse()

        result = []
        for i in range(len(nums)):
            result.append(prefix[i] * sufix[i])

        return result