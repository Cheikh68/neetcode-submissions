class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        
        for string in strs:
            result += str(len(string)) + "-" + string

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "-":
                j += 1
            number = int(s[i:j])
            string = s[j + 1 : j + 1 + number]
            result.append(string)
            i = j + 1 + number

        return result
