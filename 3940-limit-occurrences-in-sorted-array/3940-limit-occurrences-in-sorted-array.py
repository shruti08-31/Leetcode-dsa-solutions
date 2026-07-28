class Solution:
    def limitOccurrences(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k:
            return nums

        j = k

        for i in range(k, len(nums)):
            if nums[i] != nums[j-k]:
                nums[j] = nums[i]
                j += 1

        return nums[:j]
