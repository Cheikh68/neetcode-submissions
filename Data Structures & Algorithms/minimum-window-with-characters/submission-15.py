from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or len(s) == 0:
            return ""
        
        best_start = None
        best_end = None
        Tset = set(t)
        freqt = defaultdict(int)
        freqs = defaultdict(int)
        have = 0
        need = len(Tset)

        for char in t:
            freqt[char] += 1

        i = 0
        j = 0

        if len(s) > 0 and s[0] in Tset:
            freqs[s[0]] += 1
            if freqs[s[0]] == freqt[s[0]]:
                have += 1

        while i < len(s) and j < len(s):
            if have == need:
                if best_start is None:
                    best_start = i
                    best_end = j
                elif best_end + 1 - best_start > j + 1 - i:
                    best_start = i
                    best_end = j

                if s[i] in Tset:
                    freqs[s[i]] -= 1
                    if freqs[s[i]] < freqt[s[i]]:
                        have -= 1

                i += 1
                while i < len(s) and s[i] not in Tset:
                    i += 1
            else:
                j += 1
                if j < len(s) and s[j] in Tset:
                    freqs[s[j]] += 1
                    if freqs[s[j]] == freqt[s[j]]:
                        have += 1
        
        if best_start is None:
            return ""
        else:
            return s[best_start:best_end + 1]