class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        res = []

        for i in range(n):
            target = -nums[i]
            le = i+1
            re = n -1
            while le < re:
                total = nums[le] + nums[re]
                if total == target:
                    if [nums[i],nums[le],nums[re]] not in res:
                        res.append([nums[i],nums[le],nums[re]])
                if total<target:
                    le +=1
                else:
                    re-=1
        return res
        