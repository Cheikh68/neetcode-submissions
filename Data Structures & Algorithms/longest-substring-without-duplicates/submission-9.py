class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        longest = 1
        start = 0
        end = 1

        while start < len(s) and end < len(s):
            if s[end] in s[start:end]:
                longest = max(longest, end - start)
                start += 1
            else:
                end += 1
        
        longest = max(longest, end - start)

        return longest