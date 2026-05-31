class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sS = {}
        tT = {}
        for i in s:
            sS[i] = sS.get(i,0) + 1
        for j in t:
            tT[j] = tT.get(j,0) + 1
        
        if sS==tT:
            return True
        else:
            return False