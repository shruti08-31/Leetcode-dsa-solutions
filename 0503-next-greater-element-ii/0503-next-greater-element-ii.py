class Solution:
    def nextGreaterElements(self, nums):
        l = []
        n = len(nums)

        for i in range(n):
            j = i + 1

            while j < n:
                if nums[j] > nums[i]:
                    l.append(nums[j])
                    break
                j += 1

            if j == n:
                j = 0
                while j < i:
                    if nums[j] > nums[i]:
                        l.append(nums[j])
                        break
                    j += 1

                if j == i:
                    l.append(-1)

        return l