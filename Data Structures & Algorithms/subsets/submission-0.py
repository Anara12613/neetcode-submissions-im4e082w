class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for i in nums:
            res += [sub +[i] for sub in res]

        return res        