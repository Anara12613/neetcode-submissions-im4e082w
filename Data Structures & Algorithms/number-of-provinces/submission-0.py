class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(isConnected)

        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        
        seen = set()
        number = 0

        for u in range(n):
            if u not in seen:
                number += 1
                seen.add(u)
            stack = [u]
            while stack:
                v = stack.pop()
                for i in graph[v]:
                    if i not in seen:
                        stack.append(i)
                        seen.add(i)
        return number 

        