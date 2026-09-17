class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        start = 0
        longest = 0

        for end, char in enumerate(s):
            if char in last_seen:
                start = max(start, last_seen[char] + 1)

            last_seen[char] = end
            longest = max(longest, end - start + 1)

        return longest
