class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        while s and s[-1] in vowels:
            s = s[:-1]
        return s