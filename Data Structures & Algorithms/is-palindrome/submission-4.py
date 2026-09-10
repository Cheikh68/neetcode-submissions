class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = "".join(char.lower() for char in s if char.isalnum())
        print(word)
        i = 0
        j = len(word) - 1

        while i < j:   
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        
        return True