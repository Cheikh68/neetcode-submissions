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

            # Find the '-' separating length from the string
            while s[j] != "-":
                j += 1

            # Get the length of the string
            number = int(s[i:j])

            # Get the actual string
            string = s[j + 1 : j + 1 + number]
            result.append(string)

            # Move i to the beginning of the next encoded string
            i = j + 1 + number

        return result
