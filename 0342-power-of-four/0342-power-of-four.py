class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        p=0
        if n==1:
            return True
        while n>1:
            if n%4==0:
                p+=1
                n=n//4
            else:
                p=0
                break
        if p!=0:
            return True
        return False