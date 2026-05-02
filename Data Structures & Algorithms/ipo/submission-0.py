class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(list(zip(capital,profits)))
        i = 0
        sorted_heap = []

        for _ in range(k):
            while i < len(projects) and projects[i][0]<=w:
                heapq.heappush(sorted_heap,-projects[i][1])
                i += 1
            if len(sorted_heap) ==0:
                break
            w += -heapq.heappop(sorted_heap)
        return w