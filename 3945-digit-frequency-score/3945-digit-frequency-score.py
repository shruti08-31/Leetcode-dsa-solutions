class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        frequency = {}
        for digit in str(n):
            if digit in frequency:
                frequency[digit] += 1
            else:
                frequency[digit] = 1
        score = 0
        for digit, count in frequency.items():
            score += int(digit) * count
        return score