class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = 0
        p2 = 0
        res = []

        while p1<m and p2 < n:
            if nums1[p1]<nums2[p2]:
                res.append(nums1[p1])
                p1 +=1
            else:
                res.append(nums2[p2])
                p2 +=1
        
        for i in range(p1,m):
            res.append(nums1[i])
        
        for i in range(p2,n):
            res.append(nums2[i])

        for k in range(len(res)):
            nums1[k] = res[k]
        
        return
        


