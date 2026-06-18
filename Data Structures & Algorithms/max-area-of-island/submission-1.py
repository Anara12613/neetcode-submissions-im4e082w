class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        n = len(grid)
        m = len(grid[0])

        area = 0
        def not_valid(r,c):
            return r < 0 or c < 0 or r >= n or c >= m or grid[r][c] != 1 
        for a in range(n):
            for b in range(m):
                if grid[a][b] == 1:
                    cur_area = 0
                    queue = deque([(a,b)])
                    grid[a][b] = 0
                    while queue:
                        r,c = queue.popleft()
                        cur_area += 1
                        for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                            nc,rc = r + dx, c + dy
                            if not not_valid(nc,rc):
                                queue.append((nc,rc))
                                grid[nc][rc] = 0
                    area = max(area,cur_area)
        return area


