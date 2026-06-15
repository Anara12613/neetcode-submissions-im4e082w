class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        seen = set()
        number = 0

        for i in range(n):
            if i not in seen:
                number += 1
                seen.add(i)
            stack = [i]
            while stack:
                v = stack.pop()
                for x in graph[v]:
                    if x not in seen:
                        stack.append(x)
                        seen.add(x)
        return number
