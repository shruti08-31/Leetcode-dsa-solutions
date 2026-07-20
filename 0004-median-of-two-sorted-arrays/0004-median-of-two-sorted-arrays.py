class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=len(nums1)
        b=len(nums2)
        c=a+b
        nums3=[0]*c
        i=0
        j=0
        k=0
        m=0
        while i<a and j<b:
            if nums1[i]<nums2[j]:
                nums3[k]=nums1[i]
                i+=1
            else:
                nums3[k]=nums2[j]
                j+=1
            k+=1
        while i<a:
            nums3[k]=nums1[i]
            i+=1
            k+=1
        while j<b:
            nums3[k]=nums2[j]
            j+=1
            k+=1
        if c%2==0:
            m=(nums3[c//2-1]+nums3[c//2])/2
            return m
        else:
            m=nums3[c//2]
            return m
        return m