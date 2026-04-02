class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        lenght = 0

        for i in nums:
            if i-1 not in setNums:
                end = i + 1
                while end in setNums:
                    end += 1
                lenght = max(lenght, end-i)

        return lenght


        