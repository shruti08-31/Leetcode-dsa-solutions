class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = list(haystack)
        n = list(needle)

        start = 0

        while start <= len(h) - len(n):
            i = start
            j = 0
            l = [0] * len(n)

            while i < len(h) and j < len(n):
                if h[i] == n[j]:
                    l[j] = 1
                    i += 1
                    j += 1
                else:
                    break

            if all(x == 1 for x in l):
                return start

            start += 1

        return -1