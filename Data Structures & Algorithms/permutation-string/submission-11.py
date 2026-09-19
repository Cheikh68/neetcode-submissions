from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1 = defaultdict(int)
        for char in s1:
            count1[char] += 1
        
        i = 0
        j = len(s1) - 1
        count2 = defaultdict(int)
        for char in s2[i:j+1]:
            count2[char] += 1

        def dicts_equal(a, b):
            keys = a.keys() | b.keys()
            return all(a.get(k, 0) == b.get(k, 0) for k in keys)

        while j < len(s2):
            if dicts_equal(count1, count2):
                return True
            else:
                count2[s2[i]] -= 1
                i += 1
                j += 1

                if j < len(s2):
                    count2[s2[j]] += 1
        
        return False