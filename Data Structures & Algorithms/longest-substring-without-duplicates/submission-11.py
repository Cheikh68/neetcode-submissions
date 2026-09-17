class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        start = 0
        end = 0
        current_substring = set()

        while start < len(s) and end < len(s):
            if s[end] in current_substring:
                longest = max(longest, len(current_substring))
                current_substring.remove(s[start])
                start += 1
            else:
                current_substring.add(s[end])
                end += 1
        
        longest = max(longest, end - start)

        return longest