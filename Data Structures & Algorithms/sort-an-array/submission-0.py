class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums
        m = n // 2
        L = nums[:m]
        R = nums[m:]
        
        L_l = self.sortArray(L)
        R_r = self.sortArray(R)

        l_len = len(L)
        r_len = len(R)

        l,r = 0,0
        sorted_array = [0] * n

        i = 0
        while l < l_len and r < r_len:
            if L_l[l] < R_r[r]:
                sorted_array[i] = L_l[l]
                l += 1
            else:
                sorted_array[i] = R_r[r]
                r += 1
            i += 1
        while l < l_len:
            sorted_array[i] = L_l[l]
            i+=1
            l+=1

        while r < r_len:
            sorted_array[i] = R_r[r]
            i+=1
            r+=1
            
        return sorted_array



    

        