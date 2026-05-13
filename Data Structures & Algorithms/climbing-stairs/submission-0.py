class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        
        one_step = 1
        two_step = 1
        total = 0
        for i in range(2, n+1):
            total = one_step + two_step
            two_step = one_step
            one_step = total
        return total
        