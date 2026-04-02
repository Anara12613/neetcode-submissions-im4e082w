class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        begin = 0
        wind_state = 0
        res = 0

        for end in range(len(nums)):
            if nums[end]==0:
                wind_state +=1
            
            while wind_state > k:
                if nums[begin]==0:
                    wind_state -=1
                begin +=1
            res = max(res, end - begin+1)
        return res

        