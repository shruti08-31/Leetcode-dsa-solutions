class Solution:
    def findLucky(self, arr: List[int]) -> int:
        l = [0] * (max(arr) + 1)

        for i in range(len(arr)):
            l[arr[i]] += 1

        for i in range(len(l) - 1, 0, -1):  
            if i == l[i]:
                return i

        return -1