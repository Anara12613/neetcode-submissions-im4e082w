class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [] 
        for index, value in enumerate(nums*2):
            ans.append(value)
        return ans
            
            



        