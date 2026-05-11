class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        m = len(nums)

        for i in range(m):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            target = - nums[i]
            l = i + 1
            r = m - 1
            while l < r:
                curr_sum = nums[l]+nums[r]
                if curr_sum == target:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r -= 1
                elif curr_sum > target:
                    r -= 1
                else:
                    l += 1
        return res


        
        