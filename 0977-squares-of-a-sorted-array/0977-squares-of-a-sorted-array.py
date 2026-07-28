class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        r = [x ** 2 for x in nums]
        r.sort()
        return r