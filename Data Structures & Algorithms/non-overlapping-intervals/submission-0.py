class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        prev = intervals[0][1]
        res=0

        for i in range(1,len(intervals)):
            curr = intervals[i]

            if curr[0]< prev:
                res +=1
            else:
                prev = curr[1]
        return res

        