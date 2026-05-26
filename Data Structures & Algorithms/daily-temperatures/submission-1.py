class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s=[]
        r=[0]*len(temperatures)
        for i in range(len(temperatures)):
            if not s:
                s.append(i)
            while s and temperatures[i]>temperatures[s[-1]]:
                r[s[-1]]=(i-s[-1])
                s.pop()
            s.append(i)
        return r
        