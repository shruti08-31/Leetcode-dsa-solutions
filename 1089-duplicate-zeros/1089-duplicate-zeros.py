class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr1 = []
        for i in arr:
            arr1.append(i)
            if i == 0:
                arr1.append(0)
        arr[:] = arr1[:len(arr)]  