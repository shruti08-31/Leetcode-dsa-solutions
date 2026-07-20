class Solution:
    def minElement(self, nums: List[int]) -> int:
        r=[]
        for i in nums:
            if i<10:
                r.append(i)
            else: 
                s=str(i)
                t=0
                for j in s:
                    t+=int(j)
                r.append(t)
        return min(r)