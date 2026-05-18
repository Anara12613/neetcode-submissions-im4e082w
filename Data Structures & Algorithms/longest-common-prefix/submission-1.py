class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        base = strs[0]
        for i in range(len(base)):
            for w in strs[1:]:
                if i == len(w) or base[i]!=w[i]:
                    return base[0:i]
        return base