class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        if len(s) == 1:
            return num

        digit_sum = 0
        i = 0
        while i < len(s):
            digit_sum += int(s[i])
            i += 1

        return self.addDigits(digit_sum)
