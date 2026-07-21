class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        l=list(allowed)
        r=0
        for s in words:
            i =  all(char in allowed for char in s)
            if i:
                r+=1
        return r