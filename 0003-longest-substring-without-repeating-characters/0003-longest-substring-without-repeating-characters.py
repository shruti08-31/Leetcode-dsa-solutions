class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = []
        r = 0

        for i in range(len(s)):

            while s[i] in l:
                l.pop(0)          

            l.append(s[i])

            r = max(r, len(l))
        return r