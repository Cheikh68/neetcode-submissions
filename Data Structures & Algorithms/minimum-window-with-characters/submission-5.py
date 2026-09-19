from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = None
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
                if result is None:
                    result = s[i:j+1]
                elif len(result) > j + 1 - i:
                    result = s[i:j+1]

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
        
        if result is None:
            return ""
        else:
            return result

            

"""
results = []

        reference = set(t)
        tcount = defaultdict(int)
        scount = defaultdict(int)
        template = defaultdict(int)
        for char in t:
            tcount[char] += 1
            scount[char] = 0
            template[char] = 0
        
        i = 0
        while i < len(s) and s[i] not in reference:
            i += 1
        
        j = i
        if i < len(s):
            scount[s[i]] += 1

        while i < len(s) and j < len(s):
            print(scount)
            if scount == tcount:
                results.append(s[i:j+1])
                scount[s[i]] -= 1
                i += 1
                while i < len(s) and s[i] not in reference:
                    i += 1
            else:
                j += 1
                if j < len(s) and s[j] in reference:
                    scount[s[j]] += 1
                else:
                    scount[s[i]] -= 1
                    i += 1
                    while i < len(s) and s[i] not in reference:
                        i += 1
                    j = i
                    if i < len(s):
                        scount = template.copy()
                        scount[s[i]] += 1
        
        if results:
            return min(results, key=len)
        
        return ""
"""