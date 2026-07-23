class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        ans = 1
        i = 2

        while i * i <= x:
            ans = i
            i += 1
        return ans
