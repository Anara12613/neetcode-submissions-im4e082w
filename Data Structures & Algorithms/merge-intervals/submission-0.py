class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]

        for i in range(1,len(intervals)):
            prev = merged[-1]
            curr = intervals[i]

            if curr[0] <= prev[1]:
                merged[-1][1] = max(curr[1],prev[1])
            else:
                merged.append(curr)
        return merged
