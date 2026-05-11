class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while l<r:
            curr_sum = numbers[r] + numbers[l]
            if curr_sum==target:
                return [l+1,r+1]
            if curr_sum > target:
                r -= 1
            else:
                l +=1
        return 
        