class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashset = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in hashset:
                return [hashset[diff],i]
            hashset[v] = i
        return

        # l = 0
        # r = len(nums) - 1
        # while l < r:
        #     cur_sum = nums[l]+nums[r]
        #     if cur_sum<target:
        #         l+=1
        #     else:
        #         r-=1
        #     if cur_sum==target:
        #         return [l,r+1]
        # return []



        