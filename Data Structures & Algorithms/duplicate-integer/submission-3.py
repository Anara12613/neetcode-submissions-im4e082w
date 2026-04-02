class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        k = sorted(nums)
        for i in range(len(k)-1):
            if k[i]==k[i+1]:
                return True
                
        return False





        