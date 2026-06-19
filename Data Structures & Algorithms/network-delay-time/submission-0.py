class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for a,b,c in times:
            graph[a].append((b,c))
        
        min_heap = [(0,k)]
        dist = {}
        dist[k] = 0

        while min_heap:
            dst,node = heapq.heappop(min_heap)
            if dst > dist.get(node,float('inf')):
                continue
            
            for ngh, dist_to_ngh in graph[node]:
                new_dist = dst + dist_to_ngh
                if new_dist <  dist.get(ngh,float('inf')):
                    dist[ngh] = new_dist
                    heapq.heappush(min_heap,(new_dist,ngh))

        if n != len(dist):
            return -1
        return dist[max(dist, key = lambda x: dist[x])]
        