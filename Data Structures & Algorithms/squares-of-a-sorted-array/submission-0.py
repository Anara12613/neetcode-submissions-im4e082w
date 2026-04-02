class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left = 0
        right = n-1
        for i in range(n-1,-1,-1):# откуда начинаем, до куда доходим, какой делаем шаг
            if abs(nums[left])<abs(nums[right]):
                res[i]=nums[right]*nums[right]
                right -=1
            else:
                res[i] = nums[left]* nums[left]
                left +=1
        return res

        