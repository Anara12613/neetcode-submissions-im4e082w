class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0 
        lenght = 0
        for r in range(len(s)):
            chr = s[r]
            if chr in seen and seen[chr] >=l:
                l = seen[chr] + 1
            else:
                lenght = max(lenght,r - l +1)
            seen[chr] = r
        return lenght
        