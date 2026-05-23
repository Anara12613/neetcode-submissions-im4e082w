class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        t = n * m
        l = 0
        r = t - 1
        while l<=r:
            mid = (r+l) // 2
            i = mid // m
            j = mid % m
            mid_num = matrix[i][j]
            if mid_num == target:
                return True
            elif mid_num < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
        