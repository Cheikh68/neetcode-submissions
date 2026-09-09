class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = "".join(sorted(s))
        t_letters = "".join(sorted(t))
        return s_letters == t_letters