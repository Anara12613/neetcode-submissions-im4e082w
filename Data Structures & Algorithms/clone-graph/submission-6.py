"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        stack = [node]
        seen = {}
        seen[node] = Node(node.val, [])

        while stack:
            v = stack.pop()
            for i in v.neighbors:
                if i not in seen:
                    seen[i] = Node(i.val, [])
                    stack.append(i)
                seen[v].neighbors.append(seen[i])
                
        return seen[node]