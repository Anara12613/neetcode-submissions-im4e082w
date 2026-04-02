class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for n, v in enumerate(nums):
            indices[v] = n

        for i , v in enumerate(nums):
            diff = target - v
            if diff in indices and indices[diff] != i:
                return [i,indices[diff]]
        return []

