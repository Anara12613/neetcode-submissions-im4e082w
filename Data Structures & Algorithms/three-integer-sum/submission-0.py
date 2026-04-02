class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        n = len(nums)
        for i in range(n):
            target = -nums[i]
            left = i+1
            right =n-1
            while left < right:
                cur_sum = nums[left] + nums[right]
                if cur_sum == target:
                    if [nums[i],nums[left],nums[right]] not in res:
                        res.append([nums[i],nums[left],nums[right]])
                if cur_sum < target:
                    left +=1
                else:
                    right -=1
        return res

        