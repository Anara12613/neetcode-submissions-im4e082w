class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        length = 0

        for i in setNums:
            if i - 1 not in setNums:
                end = i + 1
                while end in setNums:
                    end +=1
                length = max(length, end - i)

        return length 
        