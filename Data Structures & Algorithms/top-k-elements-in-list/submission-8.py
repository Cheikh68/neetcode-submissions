from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        
        for num in nums:
            frequency[num] += 1
        
        sorted_keys = sorted(frequency, key=frequency.get, reverse=True)
        result = []

        for key in sorted_keys:
            if len(result) >= k:
                break
            else:
                result.append(key)

        return result