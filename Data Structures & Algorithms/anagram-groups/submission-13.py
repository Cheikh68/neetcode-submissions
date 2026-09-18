from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        result = []

        for string in strs:
            sorted_string = "".join(sorted(string))
            anagrams[sorted_string].append(string)
        
        for anagram_group in anagrams.values():
            result.append(anagram_group)
        
        return result