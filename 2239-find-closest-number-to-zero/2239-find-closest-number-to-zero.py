class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        c = nums[0]
        for i in nums:
            if abs(i) < abs(c):
                c = i
            elif abs(i) == abs(c):
                if i > c:
                    c = i
        return c