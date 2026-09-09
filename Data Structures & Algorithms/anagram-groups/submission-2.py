from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        foundS = {}
        foundT = {}

        for char in s:
            if char in foundS:
                foundS[char] += 1
            else:
                foundS[char] = 1

        for char in t:
            if char in foundT:
                foundT[char] += 1
            else:
                foundT[char] = 1
        
        for char, freq in foundS.items():
            if freq != foundT.get(char, 0):
                return False
        
        return True
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        
        for string in strs:
            key = "".join(sorted(string))
            groups[key].append(string)
        
        return list(groups.values())